stack = []

while True:
    user_input = input("Enter the number to store in stack and stack will break if entered character : ")
    try:
        user_input = int(user_input)
        stack.append(user_input)
    except:
        break

smallest = min(stack)
print(smallest)