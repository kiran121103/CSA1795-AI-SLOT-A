from collections import deque
def get_all_states(state,max_x,max_y):
    res=[]
    # 1. Fill the first jug
    res.append((max_x,state[1]))
    # 2. Fill the second jug
    res.append((state[0],max_y))
    # 3. Empty the first jug
    res.append((0,state[1]))
    # 4. Empty the second jug
    res.append((state[0],0))
    # 5. Pour water from the first jug to the second until the second jug is full
    res.append((state[0]-min(state[0],max_y-state[1]),state[1]+min(state[0],max_y-state[1])))
    # 6. Pour water from the second jug to the first until the first jug is full
    res.append((state[0]+min(state[1],max_x-state[0]),state[1]-min(state[1],max_x-state[0])))
    return res
def water_jug_bfs(start,target,max_x,max_y):
    visited = set()
    queue = deque([(start,[])])
    while queue:
        state,path = queue.popleft()
        if state == target:
            return path
        for new_state in get_all_states(state,max_x,max_y):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state,path+[new_state]))
    return None
start_state = (0,0)
target_state = (2,0)
max_x = 4
max_y = 3
result = water_jug_bfs(start_state,target_state,max_x,max_y)
if result:
    print(f"Steps to reach {target_state}: {result}")
else:
    print(f"No solution found for {target_state} with the given jug capacities.")
