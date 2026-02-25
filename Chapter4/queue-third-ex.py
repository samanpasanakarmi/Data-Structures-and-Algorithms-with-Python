def round_robin(tasks):
    queue = tasks[:]
    finished = []

    while queue:
        name, time_needed = queue.pop(0)
        time_needed -= 2

        if time_needed > 0:
            queue.append((name, time_needed))
        else:
            finished.append(name)

    return finished


# Example usage
tasks = [("A", 3), ("B", 6), ("C", 1)]
print(round_robin(tasks))