"""
蒙特卡罗法策略评估
"""
from gridworldpy import GridWorldEnv


# --- 算法核心参数 ---
gamma = 0.8                     # 奖励折扣因子
is_first_visit = False          # True表示首次访问蒙特卡罗法，False表示每次访问蒙特卡罗法
num_episodes = 500              # 模拟的回合数
max_steps_per_episode = 2000    # 每个回合的最大步数


# --- 环境定义 ---
# 3x3的网格环境
env = GridWorldEnv(
    grid_size=(3, 3),
    start_state=(0, 0),
    cell_size=170,
    keyboard_control=False,
    terminal_condition=max_steps_per_episode,
    show_cell_pos=True)



# 动作概率表示: [keep, up, down, left, right]
policy = [
    ((0, 0), [0.1, 0.0, 0.2, 0.0, 0.7]),
    ((0, 1), [0.1, 0.0, 0.5, 0.1, 0.3]),
    ((0, 2), [0.1, 0.0, 0.7, 0.2, 0.0]),
    ((1, 0), [0.1, 0.1, 0.4, 0.0, 0.4]),
    ((1, 1), [0.1, 0.2, 0.3, 0.2, 0.2]),
    ((1, 2), [0.1, 0.2, 0.5, 0.2, 0.0]),
    ((2, 0), [0.1, 0.2, 0.0, 0.0, 0.7]),
    ((2, 1), [0.1, 0.2, 0.0, 0.3, 0.4]),
    ((2, 2), [0.8, 0.1, 0.0, 0.1, 0.0]),
]

rewards = [
    ((0, 0), 3),  # 状态 (0,0) 的奖励
    ((0, 1), 1),  # 状态 (0,1) 的奖励
    ((0, 2), 2),  # 状态 (0,2) 的奖励
    ((1, 0), 0),  # 状态 (1,0) 的奖励
    ((1, 1), 0),  # 状态 (1,1) 的奖励
    ((1, 2), 5),  # 状态 (1,2) 的奖励
    ((2, 0), 10), # 状态 (2,0) 的奖励
    ((2, 1), -1), # 状态 (2,1) 的奖励
    ((2, 2), -5)  # 状态 (2,2) 的奖励
]


state_returns = {pos: 0.0 for pos, _ in rewards}
state_visit_count = {pos: 0 for pos, _ in rewards}


# --- 开始模拟 ---
for episode_num in range(num_episodes):
    # 重置环境到初始状态
    env.reset()
    env.set_rewards(rewards)
    env.set_policy(policy)

    # 记录当前回合的 (状态, 奖励)
    episode_history = []
    done = False

    # --- 1. 生成一个完整的轨迹 ---
    while not done:
        # env.render()
        action = env.rand_action()
        state, reward, done, _, info = env.step(action)
        episode_history.append((info['prev_state'], reward))

    # --- 2. 蒙特卡罗法计算状态价值 ---
    G = 0
    returns = []
    # 第一步：从后向前，计算出每个时间步t对应的回报G_t
    for _, reward in reversed(episode_history):
        G = reward + gamma * G
        returns.insert(0, G) # 反向构建回报列表

    # 第二步：从前向后，找到每个状态的首次访问或每次访问
    visited_states = set()
    for i, (state, _) in enumerate(episode_history):
        if is_first_visit:
            # 如果是首次访问模式，只在第一次遇到该状态时更新
            if state not in visited_states:
                state_returns[state] += returns[i]
                state_visit_count[state] += 1
                visited_states.add(state)
        else:
            # 如果是每次访问模式，每次遇到都更新
            state_returns[state] += returns[i]
            state_visit_count[state] += 1

    if (episode_num + 1) % 10 == 0:
        print(f"已完成 {episode_num + 1}/{num_episodes} 回合")

    # --- 3. 计算每个状态的平均价值 ---
    state_values = {s: r / state_visit_count[s]
                    if state_visit_count[s] > 0 else 0
                    for s, r in state_returns.items()}

    env.render(state_values=state_values)


print("\n--- 蒙特卡罗法估计的状态价值 ---")
for state, value in state_values.items():
    print(f"状态 {state}: 价值 = {value:.4f}")

input("按回车键退出...")
env.close()
