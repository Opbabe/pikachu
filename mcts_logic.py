import random
import math

class MCTS:
    def __init__(self, game_board, player, max_iterations = 1000):
        self.game_board = game_board
        self.player = player
        self.max_iterations = max_iterations
        self.tree = {}

    def run(self):
        for _ in range(self.max_iterations):
            self.simulate()

        best_move = max(self.tree.items(), key = lambda item: item[1]['visits'])[0]
        return best_move
    def simulate(self):
        current_state = self.game_board
        player = self.player
        path = []
        while not current_state.is_winner(player) and path:
            column = random.choice(range(7))  # Pick a random column
            result = current_state.apply_move(column, player)
            path.append((column, result))
            if not result:
                break

        for move in path:
            column, result = move
            if column not in self.tree:
                self.tree[column] = {'visits': 0, 'wins': 0}
            self.tree[column]['visits'] += 1
            if current_state.is_winner(player):
                self.tree[column]['wins'] += 1


