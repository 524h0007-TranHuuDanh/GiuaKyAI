from collections import deque


def build_state_graph(problem, limit):
    start = problem.initial_state
    start_key = start.key()

    states = [start]
    key_to_id = {start_key: 0}
    edges = []
    queue = deque([0])
    partial = False

    while queue:
        nid = queue.popleft()
        state = states[nid]

        for action in problem.actions(state):
            next_state = problem.result(state, action)
            next_key = next_state.key()

            if next_key not in key_to_id:
                if len(states) >= limit:
                    partial = True
                    continue
                key_to_id[next_key] = len(states)
                states.append(next_state)
                queue.append(key_to_id[next_key])

            edges.append((nid, key_to_id[next_key]))

        if len(states) >= limit:
            partial = True
            break

    return states, edges, partial, key_to_id


def true_costs(states, edges, problem):
    reverse_adj = {i: [] for i in range(len(states))}

    for u, v in edges:
        reverse_adj[v].append(u)

    dist = {i: float("inf") for i in range(len(states))}
    queue = deque()

    for i, s in enumerate(states):
        if problem.goal_test(s):
            dist[i] = 0
            queue.append(i)

    while queue:
        u = queue.popleft()
        for v in reverse_adj[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist