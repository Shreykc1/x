def minimax(nodes, depth, alpha, beta, player, index=0):
    if depth == 0 or 2*index >= len(nodes): return nodes[index]

    if player == 1:
        maximum = float('-inf')
        maximum = max(maximum, minimax(nodes, depth-1, alpha, beta, False, 2*index))
        alpha = max(alpha, maximum)
        if beta <= alpha: return maximum
        maximum = max(maximum, minimax(nodes, depth-1, alpha, beta, False, 2*index+1))
        alpha = max(alpha, maximum)
        return maximum

    else:
        minimum = float('inf')
        minimum = min(minimum, minimax(nodes, depth-1, alpha, beta, True, 2*index))
        beta = min(beta, minimum)
        if beta <= alpha: return minimum
        minimum = min(minimum, minimax(nodes, depth-1, alpha, beta, True, 2*index+1))
        beta = min(beta, minimum)
        return minimum

def main():
    player = int(input("Player 1 or 2? "))
    depth = int(input("Enter depth of tree: "))
    nodes = [0 for _ in range(2 ** depth)]
    for i in range(len(nodes)):
        nodes[i] = int(input(f"Enter value of terminal node {i+1}: "))
    best = minimax(nodes, depth, float('-inf'), float('inf'), player)
    print(f"\nBest for Player {player}: {best}")

main()
