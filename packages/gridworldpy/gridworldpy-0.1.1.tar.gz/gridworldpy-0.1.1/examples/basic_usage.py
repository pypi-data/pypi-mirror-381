import numpy as np
from gridworldpy import GridWorldEnv
import time

np.random.seed(5)

# 创建一个4x4的网格世界
env = GridWorldEnv(
    grid_size=(4, 4),        # 网格环境大小
    keyboard_control=True,  # 是否启用键盘控制
    show_cell_pos=True       # 是否显示单元格坐标
    )

env.set_rewards('random')  # 设置随机奖励
env.set_policy('random')   # 设置随机策略

print(f"初始状态: {env.state}")
for _ in range(100):
    env.render()                                          # 1. --- 渲染
    time.sleep(0.2)                                       # 2. --- 暂停
    action = env.rand_action()                            # 3. --- 动作
    obs, reward, done, effective, info = env.step(action) # 4. --- 执行动作

    if not effective:
        print(f"动作 {action} 无效，位置未改变")
    else:
        print(f"前一状态: {info['prev_state']}, 执行动作: {action}, 当前状态: {obs}, 当前奖励: {reward:.2f}")
    if done:
        print(f"经过 {env.step_count} 步到达目标，获得目标奖励：{info['goal_reward']:.2f}，游戏结束")
        break
env.close()
