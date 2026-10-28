
import math
minimax_count = 0
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global minimax_count
    if curDepth == targetDepth:
        minimax_count += 1
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

alphabeta_count = 0
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global alphabeta_count

    if depth == target:
        alphabeta_count += 1
        return scores[index]

    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(
                value,
                alphabeta(
                    depth + 1, index * 2 + i, False,
                    scores, target, alpha, beta
                )
            )

            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(
                value,
                alphabeta(
                    depth + 1, index * 2 + i, True,
                    scores, target, alpha, beta
                )
            )

            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))

minimax_result = minimax(0, 0, True, scores, depth)

print("Minimax Optimal Value;  ", minimax_result)
print("Minimax Leaf Evaluations:", minimax_count)

alphabeta_result = alphabeta(
    0, 0, True, scores, depth,
    float('-inf'), float('inf')
)

print("Alpha-Beta Optimal Value:   ", alphabeta_result)
print("Alpha-Beta Leaf Evaluations:   ", alphabeta_count)
