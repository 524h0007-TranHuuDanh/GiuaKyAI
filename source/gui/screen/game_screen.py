import pygame

from ..map_renderer import MapRenderer
from .. import ui_config
from ..ui_components import draw_button

from ...mode.single.main_single import SingleMain
from ...mode.single.core.problem import SokobanProblem

from ...mode.competitive.main_competitive import CompetitiveMain
from ...mode.competitive.core.competitive_state import CompetitiveState


class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = MapRenderer(screen, ui_config.TILE_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        self.back_button = pygame.Rect(20, 20, 100, 42)

        self.ucs_button = pygame.Rect(720, 140, 85, 42)
        self.astar_button = pygame.Rect(815, 140, 85, 42)
        self.input_box = pygame.Rect(720, 140, 180, 42)

        self.run_button = pygame.Rect(720, 200, 180, 42)
        self.prev_button = pygame.Rect(720, 260, 85, 42)
        self.next_button = pygame.Rect(815, 260, 85, 42)
        self.reset_button = pygame.Rect(720, 320, 180, 42)

        self.mode = None
        self.algorithm = None

        self.state = None
        self.start_state = None

        self.actions = []
        self.path = []
        self.step = 0

        self.n_text = ""
        self.input_active = False
        self.result = ""

    def load_game(self, state, mode):
        self.mode = mode
        self.algorithm = None

        self.state = state.copy()
        self.start_state = state.copy()

        self.actions = []
        self.path = [state.copy()]
        self.step = 0

        self.n_text = ""
        self.input_active = False
        self.result = ""

    def run_single(self, algorithm):
        if self.start_state is None:
            return

        game = SingleMain()
        self.actions = game.run(self.start_state.copy(), algorithm)

        problem = SokobanProblem(self.start_state.copy())
        current = self.start_state.copy()

        self.path = [current.copy()]

        for action in self.actions:
            current = problem.result(current, action)
            self.path.append(current.copy())

        self.step = 0
        self.state = self.path[0]

    def run_competitive(self, max_steps):
        if self.start_state is None:
            return

        game = CompetitiveMain()
        self.actions = game.run(self.start_state, max_steps)

        current = CompetitiveState(self.start_state.agent1, self.start_state.agent2, self.start_state.boxes, self.start_state.goals, self.start_state.walls, self.start_state.width, self.start_state.height)

        self.path = [current.copy()]

        for action1, action2 in self.actions:
            current = game.movement.move_two_agents(current, action1, action2)
            self.path.append(current.copy())

        score1 = current.get_score(1)
        score2 = current.get_score(2)

        if score1 > score2:
            self.result = f"Agent 1 wins: {score1} - {score2}"
        elif score2 > score1:
            self.result = f"Agent 2 wins: {score2} - {score1}"
        else:
            self.result = f"Draw: {score1} - {score2}"

        self.step = 0
        self.state = self.path[0]

    def prev(self):
        if self.step > 0:
            self.step -= 1
            self.state = self.path[self.step]

    def next(self):
        if self.step < len(self.path) - 1:
            self.step += 1
            self.state = self.path[self.step]

    def reset(self):
        self.step = 0
        self.state = self.path[0]

    def draw(self):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if self.state is None:
            return

        map_width = self.state.width * ui_config.TILE_SIZE
        map_height = self.state.height * ui_config.TILE_SIZE

        offset_x = (680 - map_width) // 2
        offset_y = (ui_config.WINDOW_HEIGHT - map_height) // 2

        self.renderer.draw(self.state, offset_x, offset_y)

        if self.mode == "single":
            draw_button(self.screen, self.ucs_button, self.button_font, "UCS", ui_config.ACTION_BUTTON_COLOR)
            draw_button(self.screen, self.astar_button, self.button_font, "A*", ui_config.ACTION_BUTTON_COLOR)

            if self.algorithm is not None:
                text = self.button_font.render(f"Selected: {self.algorithm}", True, ui_config.TEXT_COLOR)
                self.screen.blit(text, (720, 380))

        elif self.mode == "competitive":
            pygame.draw.rect(self.screen, ui_config.WHITE, self.input_box)
            pygame.draw.rect(self.screen, ui_config.TEXT_COLOR, self.input_box, 2)

            text = self.button_font.render(self.n_text, True, ui_config.TEXT_COLOR)
            self.screen.blit(text, (self.input_box.x + 10, self.input_box.y + 8))

            result_text = self.button_font.render(self.result, True, ui_config.TEXT_COLOR)
            self.screen.blit(result_text, (720, 380))

        draw_button(self.screen, self.back_button, self.button_font, "Back", ui_config.BACK_BUTTON_COLOR)
        draw_button(self.screen, self.run_button, self.button_font, "Run", ui_config.ACTION_BUTTON_COLOR)
        draw_button(self.screen, self.prev_button, self.button_font, "Prev", ui_config.ACTION_BUTTON_COLOR)
        draw_button(self.screen, self.next_button, self.button_font, "Next", ui_config.ACTION_BUTTON_COLOR)
        draw_button(self.screen, self.reset_button, self.button_font, "Reset", ui_config.ACTION_BUTTON_COLOR)