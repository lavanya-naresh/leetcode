def find_forged_ticket(log):
    slow = fast = 0
    while True:
        slow = log[slow]
        fast = log[log[fast]]
        if slow == fast:
            break

    slow = 0
    while slow != fast:
        slow = log[slow]
        fast = log[fast]
    return slow


# Test Case
tc = [
    [3, 1, 4, 5, 2, 4],
    [1, 4, 3, 2, 5, 1],
    [5, 5, 5, 5, 5, 5],
    [2, 4, 2, 2, 1],
    [1, 1],
    [5, 5, 3, 2, 1, 4],
]
for c in tc:
    print("The forged ticket number is:", find_forged_ticket(c))
