import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from gui.app import SokobanApp


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Sokoban AI")
    parser.add_argument('--map', default='maps/example_map.txt')
    parser.add_argument('--algo', default='ucs', choices=['ucs', 'astar'])
    args = parser.parse_args()

    app = SokobanApp(args.map, args.algo)
    app.run()


if __name__ == "__main__":
    main()