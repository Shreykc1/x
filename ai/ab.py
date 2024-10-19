import math


def minimax(node, depth, is_maximizing, alpha, beta):

    if depth == 0 or isinstance(node, int):
        return node

    if is_maximizing:
        max_eval = -math.inf

        for child in node:
            eval = minimax(child, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf

        for child in node:
            eval = minimax(child, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            if beta <= alpha:
                break
        return min_eval

# Example game tree: a depth-3 tree where leaf nodes represent game outcomes
game_tree = [
    [3, 5, 6],
    [9, 1, 2],
    [0, -1, -2],      
    [-6, -4, -3]      # Fourth child of root (for the maximizing player)
]

# Start the minimax with Alpha-Beta pruning
result = minimax(game_tree, 3, True, -math.inf, math.inf)
print("Best outcome for maximizer:", result)
