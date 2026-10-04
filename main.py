from source.game_app import GameApp
from source.shared.map_parser import parse_map


def main():
    app = GameApp()

    mode, map_path = app.run()

    if map_path is None:
        return

    state = parse_map(map_path)

    print("Mode:", mode)
    print("Map:", map_path)

    print("Agent 1:", state.agent1)
    print("Agent 2:", state.agent2)
    print("Boxes:", state.boxes)
    print("Goals:", state.goals)
    print("Walls:", state.walls)


if __name__ == "__main__":
    main()