import numpy as np


class QTable:
    def __init__(self, grid_size, enable_keep=False):
        self.grid_size = grid_size
        if enable_keep:
            self.table = np.zeros((grid_size[0] * grid_size[1], 5))  # 5个动作: KEEP, UP, DOWN, LEFT, RIGHT
        else:
            self.table = np.zeros((grid_size[0] * grid_size[1], 4))  # 4个动作: UP, DOWN, LEFT, RIGHT
        self.enable_keep = enable_keep
        self.rand_best_actions = [np.random.randint(self.table.shape[1]) for _ in range(self.table.shape[0])]

    def state2idx(self, state):
        """ 将二维状态 (row, col) 转换为一维索引 """
        return state[0] * self.grid_size[1] + state[1]

    def idx2state(self, idx):
        """ 将一维索引转换为二维状态 (row, col) """
        return (idx // self.grid_size[1], idx % self.grid_size[1])

    def get(self, state, action_idx):
        """ 获取指定状态和动作的 Q 值 """
        return self.table[self.state2idx(state), action_idx]

    def update(self, state, action_idx, value):
        self.table[self.state2idx(state), action_idx] = value

    def best_action(self, state):
        idx = self.state2idx(state)
        q_values = self.table[idx]
        if q_values.sum() == 0:
            return self.rand_best_actions[idx]  # 如果所有 Q 值都为 0，则随机选择一个动作
        return np.argmax(q_values)

    def best_policy(self):
        def f(idx):
            state = self.idx2state(idx)
            policy = self._id2policy(self.best_action(state))
            return state, policy
        return [f(idx) for idx in range(len(self.table))]

    def _id2policy(self, action_idx):
        p = [0, 0, 0, 0, 0] if self.enable_keep else [0, 0, 0, 0]
        p[action_idx] = 1
        return p

    def best_values(self):
        return np.max(self.table, axis=1)

    def epsilon_greedy_action(self, state, epsilon):
        action_num = 5 if self.enable_keep else 4
        if np.random.rand() < epsilon:  # 探索：随机选择一个动作
            return np.random.randint(action_num)
        else:
            return self.best_action(state)  # 利用：选择当前状态下 Q 值最大的动作


    def best_state_values(self):
        V_optimal = np.max(self.table, axis=1)
        return [(self.idx2state(idx), v) for idx, v in enumerate(V_optimal)]
