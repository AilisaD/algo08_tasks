def solution(node, idx):
    if idx == 0:
        return node.next_item
    i = idx - 1
    prev_node = node
    while i:
        prev_node = prev_node.next_item
        i -= 1
    prev_node.next_item = prev_node.next_item.next_item
    return node
