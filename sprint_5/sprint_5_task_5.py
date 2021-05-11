def solution(node) -> bool:
    l = []
    while node:
        next_node = node.left
        if next_node:
            node.left, next_node.right = next_node.right, node
            node = next_node
        else:
            if len(l) and node.value <= l[len(l) - 1]:
                return False
            l.append(node.value)
            node = node.right
    return True

