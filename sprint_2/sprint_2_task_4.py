def solution(node, elem):
    index = 0
    while node:
        if node.value == elem:
            return index
        node = node.next_item
        index += 1
    return -1
