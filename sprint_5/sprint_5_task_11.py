def print_range(node, l: int, r: int):
    if node is None:
        return
    if r >= node.value >= l:
        print_range(node.left, l, r)
        print(node.value)
        print_range(node.right, l, r)
    elif node.value < l:
        print_range(node.right, l, r)
    else:
        print_range(node.left, l, r)
