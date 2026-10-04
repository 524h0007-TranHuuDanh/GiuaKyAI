def get_next_position(position, action):
    x = position[0]
    y = position[1]

    dx = action.value[0]
    dy = action.value[1]

    new_x = x + dx
    new_y = y + dy

    new_position = (new_x, new_y)

    return new_position