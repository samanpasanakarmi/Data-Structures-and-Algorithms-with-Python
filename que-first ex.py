Q1 = []

while True:
    num = input("Enter the number you want to add in queue: ")
    try:
        if num == "":
            break
        else:
            num = int(num)
            Q1.append(num)
    except:
        print(f"Please enter a number or press enter to end")
stack = []
Q2 = []
for i in range(len(Q1)):
    if i <=2:
        stack.append(Q1[i])
    else:
        Q2.append(Q1[i])
print(Q2)
reversed_queue = []

while stack:
    reversed_queue.append(stack.pop())
for i in Q2:
    reversed_queue.append(i)

print(reversed_queue)