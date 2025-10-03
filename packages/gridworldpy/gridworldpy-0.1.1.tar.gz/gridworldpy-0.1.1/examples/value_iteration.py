"""
价值迭代寻找最优策略
"""
import numpy as np
from gridworldpy import GridWorldEnv
import time

# --- 环境和模型参数 ---
grid_size = (3, 3)
rows, cols = grid_size
num_states = rows * cols
gamma = 0.8  # 奖励折扣因子
env = GridWorldEnv(grid_size=grid_size, start_state=(0, 0), cell_size=135, show_cell_pos=True, terminal_condition=100, color_alpha=0.8)

# 定义奖励
rewards_def = [
    ((0, 0), 3), ((0, 1), 1), ((0, 2), 2),
    ((1, 0), 0), ((1, 1), 0), ((1, 2), 5),
    ((2, 0), 10), ((2, 1), -1), ((2, 2), -5)
]
env.set_rewards(rewards_def)
# 将奖励转换为与状态索引对齐的向量
rewards_vec = np.array([r for _, r in sorted(rewards_def)])

# --- 价值迭代 ---
# 1. 初始化状态价值 V(s) = 0
state_values_vec = np.zeros(num_states)
action_effects = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # keep, up, down, left, right

iteration = 0
while True:
    iteration += 1

    v_old = state_values_vec.copy()

    # 遍历每一个状态，更新其价值
    for current_state_idx in range(num_states):
        current_row, current_col = current_state_idx // cols, current_state_idx % cols

        # 计算当前状态下，采取每个动作能获得的Q值
        q_values_for_actions = []
        for action_idx, (dr, dc) in enumerate(action_effects):
            next_row, next_col = current_row + dr, current_col + dc

            # 处理撞墙：如果撞墙，则停在原地
            if not (0 <= next_row < rows and 0 <= next_col < cols):
                next_row, next_col = current_row, current_col

            next_state_idx = next_row * cols + next_col

            # Q(s,a) = R(s) + gamma * V_k(s')
            q_value = rewards_vec[current_state_idx] + gamma * v_old[next_state_idx]
            q_values_for_actions.append(q_value)

        # 贝尔曼最优方程：V_{k+1}(s) = max_a Q(s,a)
        state_values_vec[current_state_idx] = np.max(q_values_for_actions)

    # 渲染并检查收敛
    state_values_mat = state_values_vec.reshape(grid_size)
    state_values_render = [((i, j), v) for (i, j), v in np.ndenumerate(state_values_mat)]
    env.render(state_values=state_values_render)
    print(f"第 {iteration} 次价值迭代，状态价值：{'  '.join(f'{v:.2f}' for v in state_values_vec)}")

    time.sleep(0.5)

    if np.max(np.abs(state_values_vec - v_old)) < 1e-2:
        print("\n价值函数已收敛，找到最优价值！")
        break


# --- 3. 提取最优策略 ---
print("提取最优策略...")
optimal_policy = {}
optimal_policy_print = {}
action_names = ["保持", "上", "下", "左", "右"]
for current_state_idx in range(num_states):
    current_row, current_col = current_state_idx // cols, current_state_idx % cols

    # 使用收敛后的 V* 计算Q值
    q_values_for_actions = []
    for action_idx, (dr, dc) in enumerate(action_effects):
        next_row, next_col = current_row + dr, current_col + dc
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            next_row, next_col = current_row, current_col
        next_state_idx = next_row * cols + next_col
        q_value = rewards_vec[current_state_idx] + gamma * state_values_vec[next_state_idx]
        q_values_for_actions.append(q_value)

    # 贪心选择最优动作
    p = [0, 0, 0, 0, 0]
    best_action_idx = np.argmax(q_values_for_actions)
    p[best_action_idx] = 1.0
    optimal_policy[(current_row, current_col)] = p
    optimal_policy_print[(current_row, current_col)] = action_names[best_action_idx]

env.set_policy(optimal_policy)
env.render(state_values=state_values_render)

# --- 显示最终结果 ---
print("\n--- 最优状态价值 ---")
for i, v in enumerate(state_values_vec):
    print(f"状态 ({i//cols}, {i%cols}): 价值 = {v:.4f}")

print("\n--- 最优策略 ---")
for (r, c), action in sorted(optimal_policy_print.items()):
    print(f"状态 ({r}, {c}): {action}")

input("\n按回车键退出...")
env.close()
