def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Move disk from {source} to {target}: {disk}")
        print(f"Intermediate state: {state}")
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Move disk from {source} to {target}: {disk}")
        print(f"Intermediate state: {state}")
        hanoi(n - 1, auxiliary, target, source, state)

def main():
    n = int(input("Enter the number of disks: "))

    state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    print(f"Initial state: {state}")

    hanoi(n, 'A', 'C', 'B', state)

    print(f"Final state: {state}")

if __name__ == "__main__":
    main()