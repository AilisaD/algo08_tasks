def solution(node) -> bool:
    if node.left is not None:
        yield from solution(node.left)
    yield node.value
    if node.right is not None:
        yield from solution(node.right)
