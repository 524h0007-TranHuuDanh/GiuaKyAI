import heapq #dùng để taoh hàng đợi ưu tiên vì USC luôn lấy node có cost nhỏ 1
from ..shared.action import Action
from .node import Node
from ..mode.Competitive.core.competitive_rules import CompetitiveRules
from ..mode.Competitive.core.competitive_movement import CompetitiveMovement

class USC:
    def chooseAction(self, state, agentId):
        if state.is_solved():#game giải xong thì ngừng
            return Action.STAY
        rules = CompetitiveRules(state.walls) #luật di chuyển
        movement = CompetitiveMovement(rules)

        #node dau tien
        startNode = Node(state.copy(), cost = 0)

        frontier = [] #node chowf ddc khams phas
        counter = 0

        #đưa node đầu tiên vào hàng đợi, counter là dùng để cho trường hợp có những node = cost nhau
        heapq.heappush(frontier, (startNode.cost, counter, startNode))
        #lưu trạng thái có chi phí nhỏ nhất đã biết
        bestCost = {self._state_key(startNode.state): 0}

        actions = [
            Action.NORTH,
            Action.SOUTH,
            Action.EAST,
            Action.WEST,
            Action.STAY
        ]
        #lặp đến khi hết node chờ khám phá
        while frontier:
            #lấy node có cost nhỏ nhất
            currentCost, _, currentNode = heapq.heappop(frontier)
            currentKey = self._state_key(currentNode.state)
            #bỏ qua node ko còn tối ưu(ví dụ Ban đầu state A có cost = 10 sau tìm đc cost nhỏ hơn thì nó ss cost của node A vẫn đc chứa trong frontier 10 != 5 => bỏ qua)
            if currentCost != bestCost.get(currentKey):
                continue

            #kt đã giải đc chưa
            if currentNode.state.is_solved():
                return self._get_first_action(currentNode)# trả về 1 action
            
            for action in actions:
                #TH A1 đang dùng thuật toán
                if agentId == 1:
                    nextState = movement.move_two_agents(currentNode.state, action, Action.STAY)
                else: nextState = movement.move_two_agents(currentNode.state, Action.STAY, action)

                #tính cost
                nextCost = currentNode.cost + 1#mỗi bước đi là 1 chi phí => chọn trạng thái có tổng số bươc nhỏ nhất
                #tạo key cho trạng thái mới
                nextKey = self._stay_key(nextState)

                #kt có đường đi tốt hơn(vd quá khứ có cost là 5, hiện tại tìm đc cost = 2 thì cập nhật ngược lại thì bỏ qua)
                if nextCost >= bestCost.get(nextKey, float("inf")):
                    continue

                #luu lại cost tốt nhất
                bestCost[nextKey] = nextCost
                #tạo node con
                childNode = Node(
                        nextState,
                        parent=currentNode,
                        action=action,
                        cost=nextCost
                )

                counter += 1
                heapq.heappush(frontier, (startNode.cost, counter, childNode))
            #nếu lặp hết mà vẫn chưa tìm đc đường đến đích thì đứng yên
            return Action.STAY

    #hàm chuyển state thành key để so sánh
    def _state_key(self, state):
        return(state.agent1, state.agent2, tuple(sorted(state.boxes)))


    def _get_first_action():
        #nếu node goal là start thì đứng yên
        if Node.parent is None:
            return Action.STAY
        #đi ngược lại từ goal về start
        while node.parent.parent is not None:
            node = node.parent

        return node.action
