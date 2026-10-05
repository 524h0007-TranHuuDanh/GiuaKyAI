from ....shared.sokoban_state import SokobanState


class CompetitiveState(SokobanState):
    def __init__(self, agent1, agent2, boxes, goals, walls, width, height, box_owners=None):
        super().__init__(agent1, agent2, boxes, goals, walls, width, height)

        if box_owners is None:
            self.box_owners = {}
        else:
            self.box_owners = dict(box_owners)

    def get_score(self, agent_id):
        score = 0

        for box in self.boxes:
            if box in self.goals and self.box_owners.get(box) == agent_id:
                score += 1

        return score

    def get_box_owner(self, position):
        return self.box_owners.get(position)

    def move_box(self, old_position, new_position, agent_id):
        self.boxes.remove(old_position)
        self.boxes.add(new_position)

        if old_position in self.box_owners:
            del self.box_owners[old_position]

        self.box_owners[new_position] = agent_id

    def key(self):
        owners = tuple(sorted(self.box_owners.items()))
        return (self.agent1, self.agent2, tuple(sorted(self.boxes)), owners)

    def copy(self):
        return CompetitiveState(self.agent1, self.agent2, self.boxes, self.goals, self.walls, self.width, self.height, self.box_owners)