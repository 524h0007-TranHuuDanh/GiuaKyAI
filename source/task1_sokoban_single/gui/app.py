import sys
import pygame
from pathlib import Path

HERE = Path(__file__).parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from shared.constants import (
    CELL_SIZE, FPS,
    WALL, AGENT, BOX, GOAL, BOX_ON_GOAL,
    COLOR_FLOOR, COLOR_WALL, COLOR_BOX, COLOR_BOX_GOAL,
    COLOR_GOAL, COLOR_AGENT, COLOR_TEXT,
)
from core.map_parser import parse_map
from core.problem import SokobanProblem
from algorithms.ucs import UCS
from algorithms.astar import AStar


class SokobanApp:
    def __init__(self, map_path, algo='ucs'):
        self.state = parse_map(map_path)
        self.problem = SokobanProblem(self.state)
        self.algo = algo

        self.width = self.state.width * CELL_SIZE
        self.height = self.state.height * CELL_SIZE + 80

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sokoban - AI")
        self.font = pygame.font.SysFont('consolas', 18)
        self.clock = pygame.time.Clock()

        # Search
        self.result = None
        self.path = []          # danh sach state theo tung buoc
        self.step = 0
        self.paused = True
        self.running = True
        self.solved = False

        self.solve()

    def solve(self):
        if self.algo == 'ucs':
            solver = UCS()
        else:
            solver = AStar()

        self.result = solver.solve(self.problem)

        if not self.result.solved:
            print("Khong tim duoc loi giai")
            return

        # Tao danh sach state theo tung action
        self.path = [self.state]
        current = self.state
        for action in self.result.actions:
            current = self.problem.result(current, action)
            self.path.append(current)

        print(f"Algo: {self.algo.upper()}")
        print(f"Cost: {self.result.total_cost}")
        print(f"Nodes: {self.result.nodes_expanded}")
        print(f"Time: {self.result.time:.4f}s")
        print(f"Steps: {len(self.result.actions)}")

    def draw_cell(self, x, y, color):
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, color, rect)

    def draw_map(self, state):
        # Floor + wall
        for y in range(state.height):
            for x in range(state.width):
                if (x, y) in state.walls:
                    self.draw_cell(x, y, COLOR_WALL)
                else:
                    self.draw_cell(x, y, COLOR_FLOOR)

        # Goals
        for gx, gy in state.goals:
            cx = gx * CELL_SIZE + CELL_SIZE // 2
            cy = gy * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(self.screen, COLOR_GOAL, (cx, cy), CELL_SIZE // 6)

        # Boxes
        for bx, by in state.boxes:
            color = COLOR_BOX_GOAL if (bx, by) in state.goals else COLOR_BOX
            rect = pygame.Rect(bx * CELL_SIZE + 4, by * CELL_SIZE + 4,
                               CELL_SIZE - 8, CELL_SIZE - 8)
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)

        # Agent
        ax, ay = state.agent
        rect = pygame.Rect(ax * CELL_SIZE + 6, ay * CELL_SIZE + 6,
                           CELL_SIZE - 12, CELL_SIZE - 12)
        pygame.draw.rect(self.screen, COLOR_AGENT, rect)

    def draw_info(self):
        # Panel duoi cung
        panel_y = self.state.height * CELL_SIZE
        panel = pygame.Rect(0, panel_y, self.width, 80)
        pygame.draw.rect(self.screen, (220, 220, 215), panel)

        lines = [
            f"Algo: {self.algo.upper()}   Step: {self.step}/{len(self.path) - 1}",
            f"Actions: {len(self.result.actions)}   Cost: {self.result.total_cost}   Nodes: {self.result.nodes_expanded}",
            "Space: Pause/Resume   ->: Next   <-: Back   R: Reset   ESC: Quit",
        ]
        for i, line in enumerate(lines):
            text = self.font.render(line, True, COLOR_TEXT)
            self.screen.blit(text, (10, panel_y + 8 + i * 22))

    def handle_key(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        elif key == pygame.K_SPACE:
            self.paused = not self.paused
        elif key == pygame.K_RIGHT:
            if self.step < len(self.path) - 1:
                self.step += 1
        elif key == pygame.K_LEFT:
            if self.step > 0:
                self.step -= 1
        elif key == pygame.K_r:
            self.step = 0
            self.paused = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

            if not self.paused and self.step < len(self.path) - 1:
                self.step += 1

            self.screen.fill((0, 0, 0))
            current_state = self.path[self.step]
            self.draw_map(current_state)
            self.draw_info()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--map', default='maps/example_map.txt')
    parser.add_argument('--algo', default='ucs', choices=['ucs', 'astar'])
    args = parser.parse_args()

    app = SokobanApp(args.map, args.algo)
    app.run()


if __name__ == "__main__":
    main()