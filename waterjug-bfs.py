from collections import deque

# Utility function to check if the current state is a goal state
def is_goal_state(state):
    if state[0] == 2 or state[1] == 2:
        return True
    return False

# Utility function to get all possible states from the current state
def get_next_states(current_state):
    next_states = []
    # Fill Jug1
    next_states.append((5, current_state[1]))
    # Fill Jug2
    next_states.append((current_state[0],4))
    # Empty Jug1
    next_states.append((0, current_state[1]))
    # Empty Jug2
    next_states.append((current_state[0], 0))
    # Pour water from Jug1 to Jug2
    remaining_space_jug2 = 5 - current_state[1]
    pour_amount = min(current_state[0], remaining_space_jug2)
    next_states.append((current_state[0] - pour_amount, current_state[1] + pour_amount))
    # Pour water from Jug2 to Jug1
    remaining_space_jug1 = 4 - current_state[0]
    pour_amount = min(current_state[1], remaining_space_jug1)
    next_states.append((current_state[0] + pour_amount, current_state[1] - pour_amount))

    return next_states

def bfs(start_state):
    queue = deque()
    queue.append(start_state)
    visited = set()
    visited.add(start_state)
    parent = {}
    parent[start_state] = None
    while queue:
        current_state = queue.popleft()
        print("Traversed:",current_state) #printing traversed state
        if is_goal_state(current_state):
            print("Found goal state:", current_state) #printing goal state
            return parent
        next_states = get_next_states(current_state)
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parent[state] = current_state

# Starting state
start_state = (0, 0)
# Perform BFS
parent = bfs(start_state)

# Print the path from start state to goal state
print("Final Path:")
current_state = (2, 0)
while current_state != start_state:
    print(current_state)
    if current_state == (2,0) or current_state == (0,2):
        break
print(start_state)
