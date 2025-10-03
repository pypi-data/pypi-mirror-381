import tkinter as tk
import numpy as np
import time
from .utils import *


class GridWorldEnv:
    """
    一个简单的网格世界环境，支持自定义奖励、策略和状态禁用
    使用tkinter进行可视化
    """

    def __init__(self, grid_size=(5, 5), start_state=(0, 0), render_mode="human", keyboard_control=False, terminal_condition=None,
                 cell_size=135, circle_radius=35, font_size=16, max_arrow_length=30, show_cell_pos=False, color_alpha=0.0):
        """
        Args:
            grid_size:          (rows, cols) 网格大小
            start_state:        (x, y) 初始状态位置
            render_mode:        渲染模式，"human"表示可视化
            keyboard_control:   是否启用键盘控制
            terminal_condition: 终止条件
                - None:  目标位置为右下角
                - int:   最大步数限制
                - tuple: 目标位置坐标 (x, y)
            cell_size:          每个单元格的像素尺寸
            circle_radius:      显示奖励/价值的圆半径
            font_size:          圆内文本字号
            max_arrow_length:   策略箭头最大长度
            show_cell_pos:      是否在单元格内显示坐标
            color_alpha:        取值[0, 1)，用于控制颜色敏感区域，值越大对大值越敏感，值越小对小值越敏感，取0.5时为敏感度为线性
        """
        self.grid_size = grid_size
        self.render_mode = render_mode
        self.keyboard_control = keyboard_control
        self.show_cell_pos = show_cell_pos
        assert 0 <= color_alpha < 1, "color_alpha 取值为[0, 1)，值越大对大值越敏感，值越小对小值越敏感，取0.5时为敏感度为线性！"
        self.color_alpha = color_alpha

        # 设置终止条件
        if terminal_condition is None:
            # 默认：目标位置为右下角
            self.terminal_condition = (grid_size[0]-1, grid_size[1]-1)
            self.goal_pos = self.terminal_condition
            self.max_steps = None
        elif isinstance(terminal_condition, int):
            # 整数：最大步数限制
            self.terminal_condition = terminal_condition
            self.goal_pos = None
            self.max_steps = terminal_condition
        elif isinstance(terminal_condition, tuple):
            # 元组：目标位置坐标
            self.terminal_condition = terminal_condition
            self.goal_pos = terminal_condition
            self.max_steps = None
        else:
            raise ValueError("terminal_condition must be None, int (max_steps), or tuple (goal_position)")

        # 动作空间：停留(0), 上(1), 下(2), 左(3), 右(4)
        self.action_space = [0, 1, 2, 3, 4]

        # 初始状态
        self.start_state = start_state

        # 初始化各变量
        self.reset()

        # 可视化初始化
        self.cell_size = cell_size
        self.circle_radius = circle_radius
        self.max_arrow_length = max_arrow_length
        self.font_size = font_size

        # tkinter相关
        self.root = None
        self.canvas = None
        self._current_state_values = None
        self._last_circle_color_rgb = None
        self.is_closed = False  # 添加一个标志来表示窗口是否关闭

        if self.render_mode == "human":
            self._init_gui()

    def reset(self):
        """重置环境到初始状态"""
        # 当前动作
        self.action = None

        # 记录上一步动作
        self.previous_action = None

        # 当前状态
        self.state = self.start_state

        # 记录上一步状态
        self.previous_state = None

        # 运行总步数
        self.step_count = 0

        # 初始化奖励矩阵 - 每个cell的奖励值
        self.rewards = None  # np.zeros(grid_size)

        # 初始化策略矩阵 - 每个cell的动作概率分布 [停留,上,下,左,右]
        self.policy = None  # 初始化放在 set_policy 方法之中

        # 初始化禁用状态集合
        self.disabled_states = set()

        # 键盘控制相关
        self.space_pressed = False

        # step 方法是否曾被运行
        self._do_step = False

        self.is_closed = False  # 重置关闭标志
        return self._get_obs()

    def _init_gui(self):
        """初始化tkinter GUI"""
        self.root = tk.Tk()
        self.root.title("GridWorld")
        if self.keyboard_control:
            self.root.title("GridWorld - 按空格键执行下一步")
        self.root.wm_attributes('-topmost', 1)

        # 设置窗口大小
        width = self.grid_size[1] * self.cell_size
        height = self.grid_size[0] * self.cell_size + 50  # 额外空间用于显示信息

        # 计算屏幕中心位置
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(False, False)

        # 创建信息标签
        self.info_label = tk.Label(self.root, text="", font=('Arial', 12))
        self.info_label.pack()

        # 创建画布
        self.canvas = tk.Canvas(self.root, width=width, height=height-50, bg='white')
        self.canvas.pack()

        # 绑定键盘事件
        if self.keyboard_control:
            self.root.bind('<KeyPress-space>', self._on_space_press)
            self.root.focus_set()  # 确保窗口能接收键盘事件
        # 处理窗口关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def _on_space_press(self, event):
        """空格键事件处理"""
        self.space_pressed = True

    def rand_action(self, by_policy=True):
        """根据当前策略随机选择一个动作，或者直接随机选择一个动作"""
        if not by_policy:
            return np.random.choice(self.action_space)

        if self.policy is None:
            raise ValueError("Policy is not set.")
        probs = self.policy[self.state]
        return np.random.choice(self.action_space, p=probs)

    def get_current_policy(self,):
        """获取当前策略"""
        return self.policy[self.state]

    def set_rewards(self, reward_config):
        """设置或更新奖励
        Args:
            reward_config: 
                - 'random': 随机设置奖励
                - list: [((x,y),reward), ...] 以列表方式指定坐标和奖励的列表
                - dict: {(x,y): reward, ...}  以字典方式指定坐标和奖励的字典
        """
        if reward_config == 'random':
            self.rewards = np.random.uniform(-1, 1, self.grid_size)
        elif isinstance(reward_config, (list, dict)):
            if self.rewards is None:
                self.rewards = np.zeros(self.grid_size)
            reward_config = reward_config if isinstance(reward_config, list) else reward_config.items()
            for (x, y), reward in reward_config:
                self.rewards[x, y] = reward

    def set_policy(self, policy_config):
        """设置或更新策略
        Args:
            policy_config:
                - 'random': 随机设置每个cell的动作概率
                - list: [((x,y),[keep,up,down,left,right]), ...]  指定坐标和概率的列表
                - dict: {(x,y): [keep,up,down,left,right], ...} 指定坐标和概率的字典
        """
        # 若策略未初始化，则使用均匀分布
        if self.policy is None:
            self.policy = np.ones((self.grid_size[0], self.grid_size[1], 5)) * 0.2

        if policy_config == 'random':
            # 为每个cell随机生成概率分布
            for i in range(self.grid_size[0]):
                for j in range(self.grid_size[1]):
                    probs = np.random.uniform(0, 1, 5)
                    probs = probs / np.sum(probs)  # 归一化
                    self.policy[i, j] = probs
        elif isinstance(policy_config, (list, dict)):
            # 兼容list和dict两种输入格式
            policy_config = policy_config if isinstance(policy_config, list) else policy_config.items()
            for (x, y), probs in policy_config:
                assert len(probs) == 5, "Policy must have 5 values: [keep, up, down, left, right]"
                probs = np.array(probs)
                if np.sum(probs) > 0:
                    self.policy[x, y] = probs / np.sum(probs)  # 归一化
                else:
                    # 所有概率都为0，保持为0
                    self.policy[x, y] = probs

        # 调整禁用状态的概率分布
        self._adjust_policy_for_disabled_states()

    def get_policy(self):
        """获取当前策略"""
        if self.policy is None:
            return None
        policy_list = []
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                policy_list.append(((i, j), self.policy[i, j].tolist()))
        return policy_list

    def disable_states(self, disabled_poses):
        """禁用指定坐标的状态
        Args:
            disabled_poses: [(x,y), ...] 要禁用的坐标列表
        """
        self.disabled_states = set()
        for x, y in disabled_poses:
            if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1]:
                self.disabled_states.add((x, y))

        # 调整策略概率分布
        if self.policy is not None:
            self._adjust_policy_for_disabled_states()

    def _adjust_policy_for_disabled_states(self):
        """调整策略，将转移到禁用状态或边界外的概率添加到停留(keep)动作的概率上"""
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if (i, j) in self.disabled_states:
                    self.policy[i, j] = np.zeros(5)  # 禁用状态无动作
                    continue

                # 获取当前策略 [keep, up, down, left, right]
                current_policy = self.policy[i, j].copy()
                blocked_prob = 0.0

                # 检查上方动作 (index 1)
                next_x = i - 1
                if next_x < 0 or (next_x, j) in self.disabled_states:
                    blocked_prob += current_policy[1]
                    current_policy[1] = 0

                # 检查下方动作 (index 2)
                next_x = i + 1
                if next_x >= self.grid_size[0] or (next_x, j) in self.disabled_states:
                    blocked_prob += current_policy[2]
                    current_policy[2] = 0

                # 检查左方动作 (index 3)
                next_y = j - 1
                if next_y < 0 or (i, next_y) in self.disabled_states:
                    blocked_prob += current_policy[3]
                    current_policy[3] = 0

                # 检查右方动作 (index 4)
                next_y = j + 1
                if next_y >= self.grid_size[1] or (i, next_y) in self.disabled_states:
                    blocked_prob += current_policy[4]
                    current_policy[4] = 0

                # 将所有被阻挡的概率加到keep动作上 (index 0)
                current_policy[0] += blocked_prob

                self.policy[i, j] = current_policy

    def _get_obs(self):
        return self.state

    def step(self, action):
        """
        Args:
            action: 动作索引 0-4
        Returns: (observation, reward, terminated, info)
        """
        if action not in self.action_space:
            raise ValueError(f"Invalid action {action}. Must be one of {self.action_space}.")

        self._do_step = True

        effective_action = False  # 标记动作是否有效

        x, y = self.state
        new_x, new_y = x, y

        if action == 0:   # 停留
            pass  # 保持当前位置
        elif action == 1:   # 上
            new_x = max(x-1, 0)
        elif action == 2:  # 下
            new_x = min(x+1, self.grid_size[0]-1)
        elif action == 3:  # 左
            new_y = max(y-1, 0)
        elif action == 4:  # 右
            new_y = min(y+1, self.grid_size[1]-1)

        # 如果新位置被禁用则为无效动作，返回0奖励，并且不改变任何信息
        if (new_x, new_y) in self.disabled_states:
            return self._get_obs(), 0.0, False, effective_action, {}
        else:
            effective_action = True

        self.step_count += 1  # 更新步数

        # 保存返回信息的字典
        info = {}

        # 非初始步的情况下，更新上一步动作和状态
        self.previous_action = self.action
        self.previous_state = self.state
        self.is_init = False

        info['prev_state'] = self.previous_state
        info['prev_action'] = self.previous_action

        # 离开上一状态后得到的奖励
        if self.previous_state is not None:
            received_reward = self.rewards[self.previous_state] if self.rewards is not None else None
        else:
            received_reward = 0.0  # 初始状态没有离开奖励

        # 更新当前状态和动作
        self.state = (new_x, new_y)
        self.action = action

        # 判断是否终止
        done = False
        info['goal_reward'] = None
        if self.goal_pos is not None:
            # 基于目标位置的终止
            done = self.state == self.goal_pos
            if done:
                info['exit_reason'] = 'done'
                info['goal_reward'] = self.rewards[self.state] if self.rewards is not None else None
        elif self.max_steps is not None:
            # 基于最大步数的终止
            done = self.step_count >= self.max_steps
            if done:
                info['exit_reason'] = 'max_steps'
                info['goal_reward'] = 0.0
        else:
            info['exit_reason'] = None

        # 当前状态的奖励
        info['reward'] = received_reward
        info['state'] = self.state
        info['step_count'] = self.step_count
        info['action'] = self.action

        # observation, reward, terminated, effective_action, info
        return self._get_obs(), received_reward, done, effective_action, info

    def render(self, state_values=None, policy_config=None, reward_config=None):
        """
        渲染环境
        Args:
            state_values: 可选的状态价值列表
                - list: [((x,y), value), ...] 指定坐标和价值的列表
                - dict: {(x,y): value, ...} 指定坐标和价值的字典
            policy_config: 设置或更新策略
                - 'random': 随机设置每个cell的动作概率
                - list: [((x,y),[keep,up,down,left,right]), ...] 指定坐标和概率的列表
                - dict: {(x,y): [keep,up,down,left,right], ...} 指定坐标和概率的字典
            reward_config: 设置或更新奖励
                - 'random': 随机设置奖励
                - list: [((x,y),reward), ...] 指定坐标和奖励的列表
                - dict: {(x,y): reward, ...}  指定坐标和奖励的字典
        """
        if self.render_mode != "human" or self.is_closed:
            return

        # 更新策略
        if policy_config is not None:
            self.set_policy(policy_config)

        # 更新奖励
        if reward_config is not None:
            self.set_rewards(reward_config)

        # 存储状态价值以便在绘制时使用
        if state_values is not None:
            state_values = state_values if isinstance(state_values, list) else state_values.items()
        self._current_state_values = state_values

        if self.keyboard_control:
            self._render_and_wait_for_keyboard()
        else:
            self._render_once()

    def _render_once(self):
        """渲染一次，不等待输入"""
        if self.canvas is None or self.is_closed:
            return
        try:
            self._draw_screen()
            if self.root:
                self.root.update()
        except tk.TclError:
            self.is_closed = True

    def _render_and_wait_for_keyboard(self):
        """渲染并等待空格键输入"""
        if self.canvas is None or self.is_closed:
            return

        self.space_pressed = False
        self._draw_screen()

        while not self.space_pressed and not self.is_closed:
            try:
                if self.root:
                    self.root.update_idletasks()
                    self.root.update()
                time.sleep(0.01)  # 小延时避免CPU过度使用
            except tk.TclError:
                # 窗口已关闭
                self.is_closed = True
                break

    def _draw_screen(self):
        """绘制整个屏幕"""
        if self.canvas is None:
            return

        # 清空画布
        self.canvas.delete("all")

        # 绘制网格和cell内容
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                self._draw_cell(i, j)

        # 绘制智能体
        self._draw_agent()

        # 更新信息标签
        if self._do_step:
            self.info_label.config(text=f"Steps: {self.step_count}")

    def _draw_cell(self, i, j):
        """绘制单个格子"""
        x_pixel = j * self.cell_size
        y_pixel = i * self.cell_size
        center_x = x_pixel + self.cell_size // 2
        center_y = y_pixel + self.cell_size // 2

        # 确定背景颜色
        if (i, j) in self.disabled_states:
            bg_color = "gray"
        elif self.goal_pos is not None and (i, j) == self.goal_pos:
            bg_color = "yellow"
        else:
            bg_color = "white"

        # 绘制格子背景
        self.canvas.create_rectangle(
            x_pixel, y_pixel, x_pixel + self.cell_size, y_pixel + self.cell_size,
            fill=bg_color, outline="lightgray", width=2
        )

        # 如果不是禁用状态，绘制奖励圆和策略箭头
        if (i, j) not in self.disabled_states:
            self._draw_reward_circle(i, j, center_x, center_y)
            self._draw_policy_arrows(i, j, center_x, center_y)
            self._draw_cell_text(i, j, center_x, center_y)

    def _draw_reward_circle(self, i, j, center_x, center_y):
        """绘制奖励圆圈"""
        reward_val = 0 if self.rewards is None else self.rewards[i, j]

        # 获取状态价值
        state_value = None
        if self._current_state_values is not None:
            for (x, y), value in self._current_state_values:
                if x == i and y == j:
                    state_value = value
                    break

            all_state_values = [sv[1] for sv in self._current_state_values]
            max_sv, min_sv = max(all_state_values), min(all_state_values)

            # 当有状态价值时，根据状态价值映射颜色
            if state_value is not None:
                circle_color_rgb = value_to_rgb(state_value, min_sv, max_sv, self.color_alpha)
                circle_color = rgb_to_hex(circle_color_rgb)
            else:
                circle_color_rgb = (150, 150, 150)
                circle_color = rgb_to_hex(circle_color_rgb)
        else:
            # 当没有状态价值时，根据奖励值映射到颜色
            max_sv = self.rewards.max() if self.rewards is not None else 1
            min_sv = self.rewards.min() if self.rewards is not None else -1
            circle_color_rgb = value_to_rgb(reward_val, min_sv, max_sv, self.color_alpha)
            circle_color = rgb_to_hex(circle_color_rgb)

        # 绘制圆圈
        radius = self.circle_radius
        self.canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            fill=circle_color, outline="black", width=1
        )

        # 存储颜色信息用于文本颜色计算
        self._last_circle_color_rgb = circle_color_rgb

    def _draw_one_arrow(self, x0, y0, x1, y1, arrow_color, outline_color):
        """绘制带轮廓的箭头"""
        self.canvas.create_line(x0, y0, x1, y1, fill=outline_color, width=5, arrow=tk.LAST)
        self.canvas.create_line(x0, y0, x1, y1, fill=arrow_color, width=3, arrow=tk.LAST)

    def _draw_policy_arrows(self, i, j, center_x, center_y):
        """绘制策略箭头"""
        if self.policy is None:
            return

        probs = self.policy[i, j]
        max_arrow_length = self.max_arrow_length
        min_prob_threshold = 0.001  # 最小概率阈值，低于此值不显示箭头
        arrow_color = "lightgreen"
        outline_color = "black"

        # 显示keep概率（在圆圈中心附近显示一个小点）
        if probs[0] > min_prob_threshold:
            keep_radius = int(self.max_arrow_length/3 * probs[0])  # 根据概率调整点的大小
            if keep_radius > 1:
                self.canvas.create_oval(
                    center_x - keep_radius, center_y - keep_radius,
                    center_x + keep_radius, center_y + keep_radius,
                    fill=arrow_color, outline=arrow_color
                )

        # 上箭头 (index 1)
        if probs[1] > min_prob_threshold:
            length = int(max_arrow_length * probs[1])
            if length > 3:
                start_y = center_y - self.circle_radius
                end_y = start_y - length
                self._draw_one_arrow(center_x, start_y, center_x, end_y, arrow_color, outline_color)

        # 下箭头 (index 2)
        if probs[2] > min_prob_threshold:
            length = int(max_arrow_length * probs[2])
            if length > 3:
                start_y = center_y + self.circle_radius
                end_y = start_y + length
                self._draw_one_arrow(center_x, start_y, center_x, end_y, arrow_color, outline_color)

        # 左箭头 (index 3)
        if probs[3] > min_prob_threshold:
            length = int(max_arrow_length * probs[3])
            if length > 3:
                start_x = center_x - self.circle_radius
                end_x = start_x - length
                self._draw_one_arrow(start_x, center_y, end_x, center_y, arrow_color, outline_color)

        # 右箭头 (index 4)
        if probs[4] > min_prob_threshold:
            length = int(max_arrow_length * probs[4])
            if length > 3:
                start_x = center_x + self.circle_radius
                end_x = start_x + length
                self._draw_one_arrow(start_x, center_y, end_x, center_y, arrow_color, outline_color)

    def _draw_cell_text(self, i, j, center_x, center_y):
        """在格子中绘制文本（奖励和状态价值）"""
        reward_val = None if self.rewards is None else self.rewards[i, j]

        # 获取状态价值
        state_value = None
        if self._current_state_values is not None:
            for (x, y), value in self._current_state_values:
                if x == i and y == j:
                    state_value = value
                    break

        # 确定文本颜色
        if self._last_circle_color_rgb is not None:
            text_color_rgb = foreground_color(self._last_circle_color_rgb)
            text_color = rgb_to_hex(text_color_rgb)
        else:
            text_color = "black"

        font_size = self.font_size - 2 if state_value is not None else self.font_size

        if state_value is not None:
            # 显示两行：奖励和状态价值
            reward_text = '' if reward_val is None else f"R: {reward_val: .2f}"
            value_text = f"V: {state_value: .2f}"

            # 第一行（奖励）
            self.canvas.create_text(
                center_x, center_y - font_size//2,
                text=reward_text, fill=text_color, font=('Arial', font_size)
            )

            # 第二行（状态价值）
            self.canvas.create_text(
                center_x, center_y + font_size//2,
                text=value_text, fill=text_color, font=('Arial', font_size)
            )
        else:
            # 只显示奖励
            if reward_val is not None:
                reward_text = f"R: {reward_val: .2f}"
                self.canvas.create_text(
                    center_x, center_y,
                    text=reward_text, fill=text_color, font=('Arial', font_size)
                )

        # 显示格子坐标
        if self.show_cell_pos:
            self.canvas.create_text(
                center_x - self.cell_size//2 + font_size + 2, center_y - self.cell_size//2 + font_size//2 + 3,
                text=f"({i},{j})", fill="gray", font=('Arial', font_size-2)
            )

    def _draw_agent(self):
        """绘制智能体"""
        agent_center_x = self.state[1] * self.cell_size + self.cell_size // 2
        agent_center_y = self.state[0] * self.cell_size + self.cell_size // 2

        # 绘制红色圆圈轮廓表示智能体
        radius = self.circle_radius + 5
        self.canvas.create_oval(
            agent_center_x - radius, agent_center_y - radius,
            agent_center_x + radius, agent_center_y + radius,
            outline="red", width=3, fill=""
        )

    def close(self):
        """关闭环境"""
        if self.root is not None and not self.is_closed:
            self.is_closed = True
            try:
                self.root.destroy()
            except tk.TclError:
                # 捕获当根窗口已销毁时可能发生的 TclError
                pass
            self.root = None
            self.canvas = None
