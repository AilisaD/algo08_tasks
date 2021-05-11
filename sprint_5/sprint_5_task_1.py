class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(node: Node) -> int:
    answer = node.value
    answer_l, answer_r = 0, 0
    if node.left is not None:
        answer_l = solution(node.left)
    if node.right is not None:
        answer_r = solution(node.right)
    answer_rl = answer_l if answer_l > answer_r else answer_r
    return answer if answer > answer_rl else answer_rl
