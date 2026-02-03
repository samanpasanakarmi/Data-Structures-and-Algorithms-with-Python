def undo_actions(actions, n):
    stack = actions[:]
    undone = []

    for _ in range(n):
        if not stack:
            break
        undone.append(stack.pop())

    return undone, stack


# Example usage
actions = ["open", "edit", "save", "close"]
n = 2

undone, remaining = undo_actions(actions, n)

print("Undone:", undone)
print("Left in stack:", remaining)