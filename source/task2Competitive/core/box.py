class Box:
    def __init__(self, position, owner = None):
        self.position = position
        self.owner = owner
    #tuowng lai caanf suawr laij Agent gần nhất/agent cuối cùng đưa box vào goal và được tính điểm cho box đó.