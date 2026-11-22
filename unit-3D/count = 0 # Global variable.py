count = 0  # Global variable

def increment():
    global count
    count += 1
    print("Counter:", count)

increment()
increment()
increment()