from node import Node  # Attention!


def insert(root: Node, key: int) -> Node:
    if root is None:
        return Node(value=key)
    elif key < root.value:
        root.left = insert(root.left, key)
    elif key >= root.value:
        root.right = insert(root.right, key)
    return root


