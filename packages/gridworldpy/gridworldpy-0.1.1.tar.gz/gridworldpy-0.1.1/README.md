# GridWorldPy

[![PyPI version](https://badge.fury.io/py/gridworldpy.svg)](https://badge.fury.io/py/gridworldpy)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个灵活且交互式的网格世界环境，专为强化学习实验和教育目的设计。

## ✨ 特性

- 🎯 **灵活的环境配置**：支持自定义网格大小、奖励函数和终止条件
- 🎨 **实时可视化**：基于tkinter的直观图形界面，支持实时渲染
- ⚡ **交互控制**：支持键盘控制和自动执行模式
- 🎮 **策略可视化**：直观显示动作概率分布和状态价值
- 🚫 **状态禁用**：支持禁用特定状态创建障碍物
- 📊 **颜色映射**：根据奖励值和状态价值自动调整颜色显示

## 🚀 安装

使用pip从PyPI安装：

```bash
pip install gridworldpy
```

或者从源码安装：

```bash
git clone https://github.com/hitlic/gridworldpy.git
cd gridworldpy
pip install -e .
```

## 📖 快速开始

### 基本使用

```python
from gridworldpy import GridWorldEnv

# 创建一个5x5的网格世界
env = GridWorldEnv(grid_size=(5, 5), keyboard_control=True)
# 设置随机奖励
env.set_rewards('random')
# 设置随机策略
env.set_policy('random')
# 渲染环境
env.render()
# 执行一个动作
obs, reward, done, is_effective, info = env.step(1)  # 向上移动

```

### 自定义配置

```python
from gridworldpy import GridWorldEnv

# 创建带自定义配置的环境
env = GridWorldEnv(
    grid_size=(4, 4),
    keyboard_control=True,      # 启用键盘控制
    terminal_condition=(3, 3),  # 目标位置为(3,3)
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
env.disable_states([(1, 2), (2, 1)])

# 渲染环境
env.render()
```

### 带状态价值的可视化

```python
# 创建状态价值列表
state_values = [
    ((0, 0), 0.1), ((0, 1), 0.2), ((0, 2), 0.3),
    ((1, 0), 0.4), ((1, 1), -0.5), ((1, 2), 0.6),
    ((2, 0), 0.7), ((2, 1), 0.8), ((2, 2), 0.9),
]

# 渲染时包含状态价值
env.render(state_values=state_values)
```

## 🎮 控制方式

### 键盘控制模式

当`keyboard_control=True`时，使用空格键控制执行：

- 按**空格键**执行下一步
- 窗口会显示当前步数和环境状态
- 程序会等待用户输入后继续

### 自动模式

当`keyboard_control=False`时，可以连续调用`render()`方法：

```python
for step in range(10):
    env.render()
    action = np.random.randint(0, 5)  # 随机选择动作
    obs, reward, done, is_effective,info = env.step(action)
    if done:
        break
```

## 🎯 API 参考

### GridWorldEnv

主要的环境类，提供网格世界的完整功能。

#### 初始化参数

```python
GridWorldEnv(
    grid_size=(5, 5),           # 网格大小 (行, 列)
    render_mode="human",        # 渲染模式
    keyboard_control=True,      # 是否启用键盘控制
    terminal_condition=None,    # 终止条件
    cell_size=130,              # 每个格子的像素大小
    circle_radius=35,           # 奖励圆圈半径
    font_size=16,               # 字体大小
    max_arrow_length=50,        # 策略箭头最大长度
    show_cell_pos=True,         # 在每个单元上显示位置坐标
    color_alpha=0.0             # 控制色彩敏感度
)
```

#### 主要方法

- `step(action)`: 执行动作，返回(observation, reward, done, info)
- `render(state_values=None, policy_config=None, reward_config=None)`: 渲染环境
- `set_rewards(reward_config)`: 设置奖励配置
- `set_policy(policy_config)`: 设置策略配置
- `disable_states(disabled_poses)`: 禁用指定状态
- `close()`: 关闭环境

#### 动作空间

- 0: 停留在当前位置
- 1: 向上移动
- 2: 向下移动  
- 3: 向左移动
- 4: 向右移动

## 🎨 可视化说明

### 颜色编码

- **冰蓝色**: 负值（奖励或状态价值）
- **火橙色**: 正值（奖励或状态价值）
- **浅蓝色**: 零值或中性值
- **黄色**: 目标状态
- **灰色**: 禁用状态
- **红色边框**: 智能体当前位置

### 显示元素

- **圆圈**: 显示奖励值和状态价值
- **箭头长短**: 当前策略中转移至相邻状态的动作概率
- **圆心大小**：停留在当前状态的概率
- **文本**: 显示具体的数值

## 📝 示例

查看`examples/`目录获取更多使用示例：

- `basic_usage.py`：基本使用示例
- `policy_evaluation.py`：蒙特卡罗法策略评估
- `value_iteration.py`：价值迭代寻找最优策略

## 📄 许可

本项目使用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。
