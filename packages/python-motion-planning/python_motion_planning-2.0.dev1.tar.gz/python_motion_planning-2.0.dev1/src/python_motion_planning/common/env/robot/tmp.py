"""
multiagent_nav.py

依赖: gymnasium, numpy, matplotlib

保存并运行后，可通过 demo_2d() / demo_3d() 运行演示。
"""

from typing import List, Dict, Tuple, Optional
import numpy as np
import gymnasium as gym
from gymnasium import spaces
import math
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------------------
# Base classes: Agent / Controller / Environment
# ---------------------------

class BaseAgent:
    """
    Agent 基类：只包含物理参数和状态容器，负责定义观测格式。
    - dim: 空间维度（N）
    - mass: 质量
    - radius: 形状半径（用于碰撞）
    - pos, vel: 当前状态（numpy arrays）
    - acc: 当前瞬时加速度（set by controller before env.step 使用）
    """
    def __init__(self, dim: int = 2, mass: float = 1.0, radius: float = 0.1,
                 pos: Optional[np.ndarray] = None, vel: Optional[np.ndarray] = None,
                 action_min: Optional[np.ndarray] = None, action_max: Optional[np.ndarray] = None):
        self.dim = dim
        self.mass = float(mass)
        self.radius = float(radius)
        self.pos = np.zeros(dim) if pos is None else np.array(pos, dtype=float)
        self.vel = np.zeros(dim) if vel is None else np.array(vel, dtype=float)
        # acceleration is set externally by controller each step
        self.acc = np.zeros(dim)
        # action bounds per-dim (controller output bounds)
        if action_min is None:
            action_min = -np.ones(dim) * 1.0
        if action_max is None:
            action_max = np.ones(dim) * 1.0
        self.action_min = np.array(action_min, dtype=float)
        self.action_max = np.array(action_max, dtype=float)

    def observation_size(self, env) -> int:
        """
        默认观测：自身 pos, vel (2*dim) + 所有其他 agent 的相对位置 ( (n-1)*dim )
        你可以重载该函数改变观测结构。
        """
        n_agents = len(env.agents)
        return 2 * self.dim + (n_agents - 1) * self.dim

    def get_observation(self, env) -> np.ndarray:
        """
        返回观测向量（1D numpy array）。
        默认格式： [pos, vel, rel_pos_agent1, rel_pos_agent2, ...]
        相对位置按照 env.agents 列表顺序（跳过 self）。
        """
        obs = []
        obs.extend(self.pos.tolist())
        obs.extend(self.vel.tolist())
        for a in env.agents:
            if a is self:
                continue
            rel = (a.pos - self.pos)
            obs.extend(rel.tolist())
        return np.array(obs, dtype=float)

    def clip_action(self, a: np.ndarray) -> np.ndarray:
        return np.minimum(np.maximum(a, self.action_min), self.action_max)


class SimpleAgent(BaseAgent):
    """一个简单的圆/球体 agent（继承 BaseAgent）。"""
    pass


class BaseController:
    """
    Controller 基类（与环境解耦）
    - 控制器只知道：observation_space, action_space（由 agent 定义）
    - get_action(obs) -> acceleration vector (dim,)
    """
    def __init__(self, observation_space: spaces.Space, action_space: spaces.Box):
        self.observation_space = observation_space
        self.action_space = action_space

    def reset(self):
        """可选：用于在每个 episode 开始时清理内部状态。"""
        pass

    def get_action(self, obs: np.ndarray) -> np.ndarray:
        """子类必须实现：返回与 action_space.shape 匹配的 ndarray（加速度）"""
        raise NotImplementedError


class RandomController(BaseController):
    """默认随机控制器：在 action_space 内均匀采样。"""
    def get_action(self, obs: np.ndarray) -> np.ndarray:
        return self.action_space.sample()


# ---------------------------
# Environment
# ---------------------------

class MultiAgentNavEnv(gym.Env):
    """
    多智能体导航环境（可 N 维）
    - agents: list of BaseAgent 的实例
    - bounds: environment boundary as (min_vec, max_vec) each of length dim
    - dt: 时间步长
    - friction: 线性阻尼系数（v * (-friction) force），模型里转成加速度影响
    - restitution: 边界/碰撞弹性系数 [0,1]
    - max_episode_steps: 可选终止步数
    """
    metadata = {"render.modes": ["human"]}

    def __init__(self, dim: int = 2,
                 bounds: Tuple[np.ndarray, np.ndarray] = None,
                 dt: float = 0.05,
                 friction: float = 0.1,
                 restitution: float = 0.9,
                 max_episode_steps: int = 1000):
        super().__init__()
        self.dim = dim
        if bounds is None:
            lo = -np.ones(dim) * 5.0
            hi = np.ones(dim) * 5.0
            bounds = (lo, hi)
        self.bounds = (np.array(bounds[0], dtype=float), np.array(bounds[1], dtype=float))
        self.dt = float(dt)
        self.friction = float(friction)
        self.restitution = float(restitution)
        self.max_episode_steps = int(max_episode_steps)

        self.agents: List[BaseAgent] = []
        self.step_count = 0
        # observation_space and action_space are per-agent; environment doesn't expose global spaces
        # 但为了兼容 gym，提供 a dummy space
        self.observation_space = spaces.Box(-np.inf, np.inf, shape=(1,), dtype=float)
        self.action_space = spaces.Box(-np.inf, np.inf, shape=(1,), dtype=float)

    def add_agent(self, agent: BaseAgent):
        if agent.dim != self.dim:
            raise ValueError("Agent dimension must match environment dimension")
        self.agents.append(agent)

    def reset(self, seed: Optional[int] = None):
        self.step_count = 0
        # optionally randomize initial states or rely on agents' initial pos/vel
        # 返回 dict of observations keyed by agent index
        obs = {}
        for i, a in enumerate(self.agents):
            obs[i] = a.get_observation(self)
        return obs, {}

    def step(self, actions: Dict[int, np.ndarray]):
        """
        actions: dict mapping agent_index -> acceleration ndarray (dim,)
        1) clip to agent action bounds
        2) apply environment forces (friction) and integrate via semi-implicit Euler
        3) handle collisions (agent-agent, agent-boundary)
        返回：obs_dict, reward_dict, done_dict, info
        """
        self.step_count += 1
        # 1. assign actions (accelerations) to agents
        for i, a in enumerate(self.agents):
            act = actions.get(i, np.zeros(self.dim))
            a.acc = a.clip_action(np.array(act, dtype=float))

        # 2. apply environment forces -> compute net acceleration: a_net = a.acc + a_env (friction)
        for a in self.agents:
            # friction as linear damping: a_fric = -friction * v / mass
            a_env_acc = - self.friction * a.vel / (a.mass + 1e-12)
            a_net = a.acc + a_env_acc
            # semi-implicit Euler: v += a_net*dt, pos += v*dt
            a.vel = a.vel + a_net * self.dt
            a.pos = a.pos + a.vel * self.dt

        # 3. collisions: pairwise agent-agent elastic collisions (simple impulse) and boundary collisions
        self._resolve_agent_collisions()
        self._resolve_boundary_collisions()

        obs = {i: a.get_observation(self) for i, a in enumerate(self.agents)}
        # no rewards by default; you can extend
        rewards = {i: 0.0 for i in range(len(self.agents))}
        dones = {i: False for i in range(len(self.agents))}
        terminated = False
        truncated = self.step_count >= self.max_episode_steps
        info = {}
        return obs, rewards, dones, {"terminated": terminated, "truncated": truncated, **info}

    def _resolve_agent_collisions(self):
        n = len(self.agents)
        for i in range(n):
            for j in range(i + 1, n):
                a = self.agents[i]
                b = self.agents[j]
                delta = b.pos - a.pos
                dist = np.linalg.norm(delta)
                min_dist = a.radius + b.radius
                if dist < 1e-8:
                    # numeric edge-case: jitter them slightly
                    delta = np.random.randn(self.dim) * 1e-6
                    dist = np.linalg.norm(delta)
                if dist < min_dist:
                    # push them apart and compute elastic collision impulse
                    # normal vector
                    nvec = delta / dist
                    # relative velocity along normal
                    rel_vel = np.dot(b.vel - a.vel, nvec)
                    # compute impulse scalar (elastic) with restitution
                    e = self.restitution
                    j_impulse = -(1 + e) * rel_vel / (1 / a.mass + 1 / b.mass)
                    if j_impulse < 0:
                        # apply impulse
                        a.vel = a.vel - (j_impulse / a.mass) * nvec
                        b.vel = b.vel + (j_impulse / b.mass) * nvec
                    # positional correction (simple)
                    overlap = min_dist - dist
                    corr = nvec * (overlap / 2.0 + 1e-6)
                    a.pos = a.pos - corr
                    b.pos = b.pos + corr

    def _resolve_boundary_collisions(self):
        lo, hi = self.bounds
        for a in self.agents:
            for d in range(self.dim):
                if a.pos[d] - a.radius < lo[d]:
                    a.pos[d] = lo[d] + a.radius
                    if a.vel[d] < 0:
                        a.vel[d] = -a.vel[d] * self.restitution
                elif a.pos[d] + a.radius > hi[d]:
                    a.pos[d] = hi[d] - a.radius
                    if a.vel[d] > 0:
                        a.vel[d] = -a.vel[d] * self.restitution

    def render(self, mode="human", ax=None):
        # delegated to demo functions; keep signature for Gym compatibility
        raise NotImplementedError("render(): use provided demo_2d/demo_3d functions for visualization.")

    def close(self):
        pass

    # helper to build spaces per-agent
    def build_agent_spaces(self, agent: BaseAgent) -> Tuple[spaces.Box, spaces.Box]:
        """
        返回 (observation_space, action_space) for given agent
        observation_space: shape (observation_size,)
        action_space: shape (dim,) bounded by agent.action_min / action_max
        """
        obs_dim = agent.observation_size(self)
        obs_low = -np.inf * np.ones(obs_dim)
        obs_high = np.inf * np.ones(obs_dim)
        obs_space = spaces.Box(obs_low, obs_high, dtype=float)
        act_low = agent.action_min
        act_high = agent.action_max
        act_space = spaces.Box(act_low, act_high, dtype=float)
        return obs_space, act_space

# ---------------------------
# Demos: 2D & 3D visualization
# ---------------------------

def demo_2d():
    """
    2D 演示：生成 N 个圆形 agent，RandomController 控制，使用 matplotlib 动画绘制。
    """
    dim = 2
    env = MultiAgentNavEnv(dim=dim, bounds=(np.array([-5, -5]), np.array([5, 5])),
                           dt=0.03, friction=0.2, restitution=0.8, max_episode_steps=1000)

    # add agents with different masses/radii and action limits per-dim
    agents = [
        SimpleAgent(dim=dim, mass=1.0, radius=0.25, pos=np.array([-3.0, -3.0]), vel=np.zeros(dim),
                    action_min=np.array([-2.0, -2.0]), action_max=np.array([2.0, 2.0])),
        SimpleAgent(dim=dim, mass=2.0, radius=0.35, pos=np.array([3.0, -3.0]), vel=np.zeros(dim),
                    action_min=np.array([-1.5, -1.5]), action_max=np.array([1.5, 1.5])),
        SimpleAgent(dim=dim, mass=1.2, radius=0.2, pos=np.array([0.0, 3.0]), vel=np.zeros(dim),
                    action_min=np.array([-3.0, -3.0]), action_max=np.array([3.0, 3.0])),
    ]
    for a in agents:
        env.add_agent(a)

    # build controllers per-agent (Random by default)
    controllers = []
    for i, a in enumerate(env.agents):
        obs_space, act_space = env.build_agent_spaces(a)
        controllers.append(RandomController(obs_space, act_space))

    obs, _ = env.reset()

    # matplotlib setup
    fig, ax = plt.subplots(figsize=(6, 6))
    lo, hi = env.bounds
    ax.set_xlim(lo[0], hi[0])
    ax.set_ylim(lo[1], hi[1])
    ax.set_aspect('equal')
    patches = []
    texts = []
    colors = ['C0', 'C1', 'C2', 'C3', 'C4']
    for i, a in enumerate(env.agents):
        p = plt.Circle(tuple(a.pos), a.radius, color=colors[i % len(colors)], alpha=0.8)
        patches.append(p)
        ax.add_patch(p)
        t = ax.text(*a.pos, f"{i}", color='white', ha='center', va='center')
        texts.append(t)

    # animation update
    def update(frame):
        actions = {}
        for i, a in enumerate(env.agents):
            ob = a.get_observation(env)
            act = controllers[i].get_action(ob)
            actions[i] = act
        obs, rewards, dones, info = env.step(actions)
        for i, a in enumerate(env.agents):
            patches[i].center = tuple(a.pos)
            texts[i].set_position(tuple(a.pos))
        return patches + texts

    ani = animation.FuncAnimation(fig, update, frames=400, interval=30, blit=False)
    plt.title("Multi-Agent Navigation 2D Demo (Random Controllers)")
    plt.show()


def demo_3d():
    """
    3D 演示：类似 2D，但用 mpl_toolkits.mplot3d 展示球体（用 scatter 表示）。
    注意：matplotlib 3D 动画较慢，但用于快速验证足够。
    """
    dim = 3
    env = MultiAgentNavEnv(dim=dim, bounds=(np.array([-5, -5, -2]), np.array([5, 5, 2])),
                           dt=0.05, friction=0.15, restitution=0.85, max_episode_steps=1000)

    agents = [
        SimpleAgent(dim=dim, mass=1.0, radius=0.25, pos=np.array([-3.0, -3.0, 0.0]),
                    action_min=np.array([-2.0, -2.0, -1.0]), action_max=np.array([2.0, 2.0, 1.0])),
        SimpleAgent(dim=dim, mass=1.5, radius=0.3, pos=np.array([3.0, -3.0, 0.5]),
                    action_min=np.array([-1.5, -1.5, -1.0]), action_max=np.array([1.5, 1.5, 1.0])),
        SimpleAgent(dim=dim, mass=0.8, radius=0.2, pos=np.array([0.0, 3.0, -0.5]),
                    action_min=np.array([-3.0, -3.0, -1.0]), action_max=np.array([3.0, 3.0, 1.0])),
    ]
    for a in agents:
        env.add_agent(a)

    controllers = []
    for i, a in enumerate(env.agents):
        obs_space, act_space = env.build_agent_spaces(a)
        controllers.append(RandomController(obs_space, act_space))

    obs, _ = env.reset()

    # matplotlib 3d setup
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    lo, hi = env.bounds
    ax.set_xlim(lo[0], hi[0])
    ax.set_ylim(lo[1], hi[1])
    ax.set_zlim(lo[2], hi[2])
    scat = ax.scatter([a.pos[0] for a in env.agents],
                      [a.pos[1] for a in env.agents],
                      [a.pos[2] for a in env.agents],
                      s=[(a.radius * 1000) for a in env.agents])

    # annotation labels
    annotations = [ax.text(a.pos[0], a.pos[1], a.pos[2], str(i)) for i, a in enumerate(env.agents)]

    def update(frame):
        actions = {}
        for i, a in enumerate(env.agents):
            ob = a.get_observation(env)
            act = controllers[i].get_action(ob)
            actions[i] = act
        obs, rewards, dones, info = env.step(actions)
        xs = [a.pos[0] for a in env.agents]
        ys = [a.pos[1] for a in env.agents]
        zs = [a.pos[2] for a in env.agents]
        scat._offsets3d = (xs, ys, zs)
        for i, ann in enumerate(annotations):
            ann.set_position((xs[i], ys[i]))
            # can't directly set z of text easily; remove & redraw would be heavy
        return scat, *annotations

    ani = animation.FuncAnimation(fig, update, frames=400, interval=50, blit=False)
    plt.title("Multi-Agent Navigation 3D Demo (Random Controllers)")
    plt.show()


# ---------------------------
# Example usage
# ---------------------------

if __name__ == "__main__":
    # 运行 2D 或 3D demo
    # print("Running 2D demo...")
    demo_2d()
    # 若要运行 3D，注释上两行，解除下一行注释：
    # demo_3d()
