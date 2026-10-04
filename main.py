from source.gameApp import GameApp
from source.shared.mapParser import parse_map


def main():
    app = GameApp()

    mode, mapPath = app.run()

    if mapPath is None:
        return

    state = parse_map(mapPath)

    print("Mode:", mode)
    print("Map:", mapPath)

    print("Agent 1:", state.agent1)
    print("Agent 2:", state.agent2)
    print("Boxes:", state.boxes)
    print("Goals:", state.goals)
    print("Walls:", state.walls)


if __name__ == "__main__":
    main()