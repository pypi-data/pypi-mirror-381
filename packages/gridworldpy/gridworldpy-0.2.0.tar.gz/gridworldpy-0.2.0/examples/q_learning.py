"""Q-learning 算法实现

Q-learning 是一种异策略（off-policy）算法。
它的更新规则不依赖于下一个实际执行的动作，而是直接使用下一状态能带来的最大化收益来更新 Q 值。

Q-learning 更新规则:
Q(s, a) <- Q(s, a) + alpha * (reward + gamma * max_{a'} Q(s', a') - Q(s, a))
"""
from gridworldpy import GridWorldEnv, QTable


# 1. 环境设置
grid_size = (7, 7)
# 奖励设置
rewards_def = [
    ((6, 6), 1),
    ((4, 0), -1),
    ((0, 4), -1)
]

disable_def = [(2, 2), (3, 2), (4, 2), (2, 3), (2, 4)]

# 2. 超参数设置
gamma = 0.8          # 折扣因子
alpha = 0.05         # 学习率
epsilon = 0.99       # ε-贪婪策略中的探索率
min_epsilon = 0.15   # ε的最小值
decay_rate = 0.99    # ε的衰减率
num_episodes = 1000  # 训练的回合数

# 3. 初始化环境与 Q-table
env = GridWorldEnv(grid_size=grid_size, enable_keep=False, start_state=(0, 0), target_state=(6, 6),
                   cell_size=80, show_cell_pos=True, max_arrow_length=15, circle_radius=20, font_size=10,
                   max_steps=500, show_step_num=True,
                   )


q_table = QTable(grid_size, enable_keep=env.enable_keep)


# 4. Q-learning 算法主循环
for episode in range(num_episodes):
    print(f"第 {episode + 1} 回合， epsilon: {epsilon:.4}")
    state = env.reset()
    env.set_rewards(rewards_def)
    env.set_disable_states(disable_def)

    while True:
        # 根据当前状态选择动作（ε-贪婪策略）
        action = q_table.epsilon_greedy_action(state, epsilon)

        # 执行动作，获取新状态和奖励
        next_state, reward, done, _, info = env.step(action)
        reward = reward if reward is not None else 0.0

        # Q-learning 更新规则
        current_q = q_table.get(state, action)
        # 核心步骤：使用下一状态的最大Q值，而不是下一个实际动作的Q值
        next_max_q = q_table.best_q_value(next_state) if not done else 0.0
        td_target = reward + gamma * next_max_q
        td_error = td_target - current_q
        q_table.update(state, action, current_q + alpha * td_error)

        # 如果到达终止状态，则结束当前回合
        if done:
            break

        # 更新状态
        state = next_state

        optimal_policy = q_table.best_policy()
        env.set_policy(optimal_policy)
        env.render(q_table.best_state_values())

    # 更新 ε
    epsilon = max(min_epsilon, epsilon * decay_rate)


optimal_policy = q_table.best_policy()
env.set_policy(optimal_policy)
env.render(q_table.best_state_values())

input("按回车键退出...")
env.close()
