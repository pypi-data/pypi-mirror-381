import numpy as np


def value_to_rgb(value, vmin=-1, vmax=1, alpha = 1.0, neutral=(245, 255, 255)):
    """
    把 value 映射到 RGB：
    Args:
        value: float值
            - value < 0: 浅蓝 (neutral) -> 蓝
            - value > 0: 浅蓝 (neutral) -> 橙
        vmin: 最大值
        vmax: 最小值
        alpha: 取值(0, 1)，用于控制颜色敏感区域，值越大对大值越敏感，值越小对小值越敏感，取0.5时为敏感度为线性
    """
    def trans_value(v, alpha):
        k = 1/(2*(1-alpha))
        return v ** k

    if value == 0:
        return neutral
    v = value

    if value < 0:
        # 负值：浅蓝 (neutral) -> 冰蓝
        t = trans_value(v/vmin, alpha)  # vmin ≤ v ≤ 0, t ∈ [0,1]
        cold = (0, 180, 255)
        R = int(neutral[0] * (1 - t) + cold[0] * t)
        G = int(neutral[1] * (1 - t) + cold[1] * t)
        B = int(neutral[2] * (1 - t) + cold[2] * t)
    else:
        # 正值：浅蓝 (neutral) -> 火橙
        t = trans_value(v/vmax, alpha)  # 0 ≤ v ≤ vmax, t ∈ [0,1]
        hot = (255, 100, 0)
        R = int(neutral[0] * (1 - t) + hot[0] * t)
        G = int(neutral[1] * (1 - t) + hot[1] * t)
        B = int(neutral[2] * (1 - t) + hot[2] * t)

    return (R, G, B)


def rgb_to_hex(rgb):
    """将RGB元组转换为十六进制颜色字符串"""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def foreground_color(bg_rgb):
    """
    给定背景色 RGB，返回与背景对比度最大的前景色
    Args:
        bg_rgb: tuple(int,int,int)，背景颜色 (R, G, B)，取值范围 0~255
    Returns:
        tuple(int,int,int): 推荐的前景色 (R, G, B)
    """
    def srgb_to_linear(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    def luminance(rgb):
        r, g, b = [srgb_to_linear(v) for v in rgb]
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def contrast(rgb1, rgb2):
        L1, L2 = luminance(rgb1), luminance(rgb2)
        L_light, L_dark = max(L1, L2), min(L1, L2)
        return (L_light + 0.05) / (L_dark + 0.05)

    # 候选前景色（黑白 + 常见彩色）
    candidates = [
        (0, 0, 0),       # 黑
        (255, 255, 255),  # 白
        (255, 0, 0),     # 红
        (0, 255, 0),     # 绿
        (0, 0, 255),     # 蓝
        (255, 255, 0),   # 黄
        (0, 255, 255),   # 青
        (255, 0, 255),   # 洋红
        (255, 165, 0),   # 橙
        (128, 0, 128),   # 紫
    ]

    # 选出对比度最大的颜色
    best_color = max(candidates, key=lambda fg: contrast(bg_rgb, fg))
    return best_color


def policy_to_transition_matrix(policy, grid_size=(3, 3)):
    """
    将格子世界的策略定义转换为状态转移概率矩阵 P。
    Args:
        policy (list): 策略定义列表。
            - 列表 [((row, col), [p_keep, p_up, p_down, p_left, p_right]), ...]
            - 字典 {(row, col): [p_keep, p_up, p_down, p_left, p_right], ... }
        grid_size (tuple): 格子世界的尺寸 (rows, cols)。
    Returns:
        numpy.ndarray: 一个 (N*M) x (N*M) 的状态转移矩阵 P，其中 P[i, j] 是从状态 i 转移到状态 j 的概率。
    """
    if isinstance(policy, dict):
        policy = list(policy.items())
    rows, cols = grid_size
    num_states = rows * cols

    # 初始化一个 num_states x num_states 的零矩阵
    transition_matrix = np.zeros((num_states, num_states))

    # 定义动作对坐标的改变效果 (dr, dc)
    # 顺序必须与策略中的概率列表严格对应: [keep, up, down, left, right]
    action_effects = [
        (0, 0),   # keep
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    # 状态坐标 (r, c) 到一维索引的转换函数
    def state_to_idx(r, c):
        return r * cols + c

    # 遍历策略中的每一条规则
    for (r, c), probabilities in policy:
        from_idx = state_to_idx(r, c)

        # 遍历该状态下的每一种动作及其概率
        for i, prob in enumerate(probabilities):
            if prob == 0:
                continue                # 跳过概率为0的动作
            dr, dc = action_effects[i]                          # 获取动作导致的位置变化
            next_r, next_c = r + dr, c + dc                     # 计算理论上的下一个状态坐标
            if not (0 <= next_r < rows and 0 <= next_c < cols): # 检查边界条件（撞墙），如果撞墙，则停在原地
                next_r, next_c = r, c  # 停在原地
            to_idx = state_to_idx(next_r, next_c) # 计算最终的目标状态索引
            transition_matrix[from_idx, to_idx] += prob

    return transition_matrix
