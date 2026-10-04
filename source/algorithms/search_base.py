class SearchResult:
    def __init__(self, solved, actions, total_cost,
                 nodes_expanded, max_frontier, explored_states=None):
        self.solved = solved
        self.actions = actions
        self.total_cost = total_cost
        self.nodes_expanded = nodes_expanded
        self.max_frontier = max_frontier
        self.explored_states = explored_states


class SearchAlgorithm:
    def reconstruct(self, node):
        actions = []
        while node.parent is not None:
            actions.append(node.action)
            node = node.parent
        actions.reverse()
        return actions