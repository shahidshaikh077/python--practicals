# Pattern 1
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Pattern 2
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Pattern 3
for i in range(1, 6):
    for j in range(1, i + 1):
        print("👍", end=" ")
    print()

print()

# Pattern 4
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

print()

# Pattern 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
