from gridworldpy import GridWorldEnv

# 创建带自定义配置的环境
env = GridWorldEnv(
    grid_size=(4, 4),
    keyboard_control=True,      # 启用键盘控制
    enable_keep= True,          # 启用停留动作
    target_state=(3, 3),        # 目标位置为(3,3)
    cell_size=150,              # 每个格子150像素
    circle_radius=40,           # 奖励圆圈半径40像素
)

# 设置特定位置的奖励
rewards = [
    ((0, 0), -0.1),  # 起始位置小负奖励
    ((1, 1), -1.0),  # 陷阱：大负奖励
    ((3, 3), 1.0),   # 目标：大正奖励
]
env.set_rewards(rewards)

# 设置特定的策略
policy = [
    ((0, 0), [0.1, 0.2, 0.2, 0.2, 0.3]),  # 位置(0,0)的动作概率
    ((1, 0), [0.0, 0.0, 0.5, 0.0, 0.5]),  # 位置(1,0)的动作概率
]
env.set_policy(policy)

# 禁用某些状态（创建障碍物）
env.set_disable_states([(1, 2), (2, 1)])

# 渲染环境
env.render()