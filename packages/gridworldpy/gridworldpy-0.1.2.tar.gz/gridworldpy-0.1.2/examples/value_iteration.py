"""
价值迭代 (Value Iteration) 寻找最优策略
"""
import numpy as np
from gridworldpy import GridWorldEnv
import time

# --- 环境和模型参数 ---
grid_size = (3, 3)
rows, cols = grid_size
num_states = rows * cols
gamma = 0.8  # 奖励折扣因子
env = GridWorldEnv(grid_size=grid_size, enable_keep=False,
                   start_state=(0, 0), cell_size=135, show_cell_pos=True,
                   max_steps=100, color_alpha=0.8)

# 定义奖励
rewards_def = [
    ((0, 0), 3), ((0, 1), 1), ((0, 2), 2),
    ((1, 0), 0), ((1, 1), 0), ((1, 2), 1),
    ((2, 0), 10), ((2, 1), -1), ((2, 2), -5)
]
env.set_rewards(rewards_def)
# 将奖励转换为与状态索引对齐的向量
rewards_vec = np.array([r for _, r in sorted(rewards_def)])

# --- 价值迭代 ---
# 1. 初始化状态价值 V(s) = 0
state_values_vec = np.zeros(num_states)
if env.enable_keep:
    action_effects = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # keep, up, down, left, right
else:
    action_effects = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

num_actions = len(action_effects)
transition_table = np.zeros((num_states, num_actions), dtype=int)
for state_idx in range(num_states):
    row, col = divmod(state_idx, cols)
    next_indices = []
    for dr, dc in action_effects:
        next_row, next_col = row + dr, col + dc
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            next_row, next_col = row, col
        next_indices.append(next_row * cols + next_col)
    transition_table[state_idx] = next_indices

iteration = 0
while True:
    iteration += 1

    v_old = state_values_vec.copy()

    # 基于上一次的价值函数整体更新 Q(s,a) 并取最大值
    q_values_mat = rewards_vec[:, None] + gamma * v_old[transition_table]
    state_values_vec = np.max(q_values_mat, axis=1)

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
    optimal_policy = {}
    optimal_policy_print = {}
    action_names = ["保持", "上", "下", "左", "右"] if env.enable_keep else ["上", "下", "左", "右"]

    greedy_q_values = rewards_vec[:, None] + gamma * state_values_vec[transition_table]
    best_action_indices = np.argmax(greedy_q_values, axis=1)

    for current_state_idx, best_action_idx in enumerate(best_action_indices):
        current_row, current_col = divmod(current_state_idx, cols)
        probs = [0.0] * env.action_num
        probs[int(best_action_idx)] = 1.0
        optimal_policy[(current_row, current_col)] = probs
        optimal_policy_print[(current_row, current_col)] = action_names[int(best_action_idx)]

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
