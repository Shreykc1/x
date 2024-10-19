from collections import deque

def water_jug_solver(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()
        (x, y) = current_state

        if x == target or y == target:
            return True

        if current_state in visited:
            continue

        visited.add(current_state)

        next_states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x)),
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    return False

def main():
    jug1 = 5
    jug2 = 4
    target = 2

    if water_jug_solver(jug1, jug2, target):
        print(f"Yes, it's possible to measure exactly {target} liters.")
    else:
        print(f"No, it's not possible to measure {target} liters.")

if __name__ == "__main__":
    main()
