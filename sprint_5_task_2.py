class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> bool:
    pass


r = Node(7,
         left=Node(5, left=Node(3), right=Node(7)),
         right=Node(9, left=Node(8),
                    right=Node(10, right=Node(11))))