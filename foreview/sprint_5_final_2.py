def remove(root, key: int):
    if root is None:
        return root
    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    elif root.left is not None and root.right is not None:
        max_left_subtree = root.left
        while max_left_subtree.right:
            max_left_subtree = max_left_subtree.right
        root.value = max_left_subtree.value
        root.left = remove(root.left, max_left_subtree.value)
    else:
        if root.left is not None:
            root = root.left
        elif root.right is not None:
            root = root.right
        else:
            root = None
    return root
