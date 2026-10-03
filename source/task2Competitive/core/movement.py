class Movement:
    def __init__(self, rules):
        self.rules = rules

    def applyActions(self, state, action1, action2):
        # Rules chỉ quyết định, không sửa state gốc
        plans = self.rules.resolActions(
            state,
            action1,
            action2
        )

        p1 = plans[1]
        p2 = plans[2]

        # Tạo state mới
        new = state.copy()

        # Áp dụng kế hoạch của 2 Agent
        self._applyPlan(new, 1, p1)
        self._applyPlan(new, 2, p2)

        # Kết thúc một bước
        new.stepCount += 1

        return new

    def _applyPlan(self, state, agentId, plan):

        # Action bị hủy -> Agent đứng yên
        if not plan["valid"]:
            return

        agent = state.getAgent(agentId)

        # Nếu có box bị đẩy
        if plan["box"] is not None:

            oldBoxPosition = plan["box"].position

            # Tìm box tương ứng trong state mới
            box = state.boxPosition(oldBoxPosition)

            if box is not None:

                box.position = plan["boxNextPosition"]

                # Box nằm trên goal -> thuộc agent đẩy
                if state.isGoal(plan["boxNextPosition"]):
                    box.owner = agentId

                # Box không còn trên goal
                else:
                    box.owner = None

        # Di chuyển agent
        agent.position = plan["nextPosition"]