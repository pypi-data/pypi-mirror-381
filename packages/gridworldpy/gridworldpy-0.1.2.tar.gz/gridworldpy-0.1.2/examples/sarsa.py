"""SARSA 算法"""
from gridworldpy import GridWorldEnv, QTable


# 1. 环境设置
grid_size = (7, 7)
# 奖励设置
rewards_def = [
    ((3, 5), 1),
    # ((4, 0), -1),
    # ((0, 4), -1)
]

disable_def = [(3, 1), (3, 2), (1, 4), (2, 4), (3, 4), (4, 4)]

# 2. 超参数设置
gamma = 0.8  # 折扣因子
alpha = 0.05  # 学习率
epsilon = 0.99  # ε-贪婪策略中的探索率
min_epsilon = 0.15  # ε的最小值
decay_rate = 0.99  # ε的衰减率
num_episodes = 1000  # 训练的回合数

# 3. 初始化环境与 Q-table
env = GridWorldEnv(grid_size=grid_size, enable_keep=False, start_state=(0, 0), target_state=(3, 5),
                   cell_size=80, show_cell_pos=True, max_arrow_length=15, circle_radius=20, font_size=10,
                   max_steps=500, color_alpha=0.6, show_step_num=True,
                   )

q_table = QTable(grid_size, enable_keep=env.enable_keep)


# 5. SARSA 算法主循环
for episode in range(num_episodes):
    print(f"第 {episode + 1} 回合， epsilon: {epsilon:.4}")
    state = env.reset()
    env.set_rewards(rewards_def)
    env.set_disable_states(disable_def)

    # 根据初始状态选择第一个动作
    action = q_table.epsilon_greedy_action(state, epsilon)

    while True:
        # 执行动作，获取新状态和奖励
        next_state, reward, done, _, info = env.step(action)
        reward = reward if reward is not None else 0.0
        # 在新状态下，根据策略选择下一个动作
        if done:
            next_action = None
            next_q = 0.0
        else:
            next_action = q_table.epsilon_greedy_action(next_state, epsilon)
            next_q = q_table.get(next_state, next_action)

        # SARSA 更新规则
        current_q = q_table.get(state, action)
        td_target = reward + gamma * next_q
        td_error = td_target - current_q
        q_table.update(state, action, current_q + alpha * td_error)

        # 如果到达终止状态，则不需要更新状态和动作，直接结束
        if done:
            break

        # 更新状态和动作为下一次迭代做准备
        state = next_state
        action = next_action

        optimal_policy = q_table.best_policy()
        env.set_policy(optimal_policy)
        env.render(q_table.best_state_values())


    # 更新 ε
    epsilon = max(min_epsilon, epsilon * decay_rate)


input("按回车键退出...")
env.close()
