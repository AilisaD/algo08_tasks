def solution(node):
    tmp = None
    while node:
        tmp = node.prev
        node.prev = node.next
        node.next = tmp
        node = node.prev
    if tmp:
        node = tmp.prev
    return node
