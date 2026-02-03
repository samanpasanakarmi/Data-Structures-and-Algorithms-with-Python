queue = []

while True:
    user_input = input("Enter the number to store in queue and queue will break if entered character : ")
    try:
        user_input = int(user_input)
        queue.append(user_input)
        if len(queue) > 5:
            queue.pop(0)
    except:
        break

print(queue)