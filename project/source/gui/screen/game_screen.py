import pygame
from ..map_renderer import MapRenderer
from .. import ui_config
from ...mode.single.single_game import SingleMain
from ...mode.single.core.problem import SokobanProblem
from ...mode.competitive.competitive_game import CompetitiveMain
from ...mode.competitive.core.competitive_state import CompetitiveState


class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = MapRenderer(screen, ui_config.TILE_SIZE)
        self.font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        self.back_button = pygame.Rect(20, 20, 100, 42)
        self.ucs_button = pygame.Rect(720, 140, 85, 42)
        self.astar_button = pygame.Rect(815, 140, 85, 42)
        self.input_box = pygame.Rect(720, 140, 180, 42)
        self.run_button = pygame.Rect(720, 200, 180, 42)
        self.reset_button = pygame.Rect(720, 250, 180, 42)

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
        self.final_result = ""
        self.playing = False
        self.auto_delay = 700
        self.last_step_time = 0

    def load_game(self, state, mode):
        self.mode = mode
        self.algorithm = None
        self.state = state.copy()
        self.start_state = state.copy()
        self.actions = []
        self.path = [state.copy()]
        self.step = 0
        self.n_text = ""
        self.result = ""
        self.final_result = ""
        self.playing = False

    def run_single(self, algorithm):
        if self.start_state is None:
            return

        start_state = self.start_state

        game = SingleMain()
        self.actions = game.run(start_state.copy(), algorithm)

        problem = SokobanProblem(start_state.copy())
        current = start_state.copy()
        self.path = [current.copy()]

        for action in self.actions:
            current = problem.result(current, action)
            self.path.append(current.copy())

        self.start()

    def run_competitive(self, max_steps):
        if self.start_state is None:
            return

        start_state = self.start_state

        game = CompetitiveMain()
        self.actions = game.run(start_state, max_steps)

        current = CompetitiveState(start_state.agent1, start_state.agent2, start_state.boxes, start_state.goals, start_state.walls, start_state.width, start_state.height)
        self.path = [current.copy()]

        for action1, action2 in self.actions:
            current = game.movement.move_two_agents(current, action1, action2)
            self.path.append(current.copy())

        score1 = current.get_score(1)
        score2 = current.get_score(2)

        if score1 > score2:
            self.final_result = f"Agent 1 wins: {score1} - {score2}"
        elif score2 > score1:
            self.final_result = f"Agent 2 wins: {score2} - {score1}"
        else:
            self.final_result = f"Draw: {score1} - {score2}"

        self.start()

    def start(self):
        self.step = 0
        self.state = self.path[0]
        self.result = ""
        self.playing = len(self.path) > 1
        self.last_step_time = pygame.time.get_ticks()

    def pause(self):
        self.playing = False

    def toggle_pause(self):
        if self.playing:
            self.playing = False
        elif self.step < len(self.path) - 1:
            self.playing = True
            self.last_step_time = pygame.time.get_ticks()

    def prev(self):
        self.playing = False
        if self.step > 0:
            self.step -= 1
            self.state = self.path[self.step]
        self.result = ""

    def next(self):
        self.playing = False
        if self.step < len(self.path) - 1:
            self.step += 1
            self.state = self.path[self.step]
        self.update_result()

    def reset(self):
        self.playing = False
        self.step = 0
        self.state = self.path[0]
        self.result = ""

    def update_result(self):
        if self.mode == "competitive" and self.step == len(self.path) - 1:
            self.result = self.final_result
        elif self.mode == "competitive":
            self.result = ""

    def update_auto(self):
        if not self.playing:
            return

        now = pygame.time.get_ticks()
        if now - self.last_step_time >= self.auto_delay:
            self.step += 1
            self.state = self.path[self.step]
            self.last_step_time = now

            if self.step == len(self.path) - 1:
                self.playing = False
                self.update_result()

    def draw(self):
        self.update_auto()
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if self.state is None:
            return

        map_width = self.state.width * ui_config.TILE_SIZE
        map_height = self.state.height * ui_config.TILE_SIZE
        offset_x = (680 - map_width) // 2
        offset_y = (ui_config.WINDOW_HEIGHT - map_height) // 2
        self.renderer.draw(self.state, offset_x, offset_y)

        if self.mode == "single":
            ui_config.draw_button(self.screen, self.ucs_button, self.font, "UCS", ui_config.ACTION_BUTTON_COLOR)
            ui_config.draw_button(self.screen, self.astar_button, self.font, "A*", ui_config.ACTION_BUTTON_COLOR)
            if self.algorithm:
                text = self.font.render(f"Selected: {self.algorithm}", True, ui_config.TEXT_COLOR)
                self.screen.blit(text, (720, 360))
        else:
            pygame.draw.rect(self.screen, ui_config.WHITE, self.input_box)
            pygame.draw.rect(self.screen, ui_config.TEXT_COLOR, self.input_box, 2)
            text = self.font.render(self.n_text, True, ui_config.TEXT_COLOR)
            self.screen.blit(text, (self.input_box.x + 10, self.input_box.y + 8))
            text = self.font.render(self.result, True, ui_config.TEXT_COLOR)
            self.screen.blit(text, (720, 500))

        if not self.actions:
            status = "Ready"
        elif self.playing:
            status = "Running"
        elif self.step == len(self.actions):
            status = "Finished"
        else:
            status = "Paused"

        step_text = self.font.render(f"Step: {self.step}/{len(self.actions)}", True, ui_config.TEXT_COLOR)
        cost_text = self.font.render(f"Cost: {self.step}", True, ui_config.TEXT_COLOR)
        status_text = self.font.render(f"Status: {status}", True, ui_config.TEXT_COLOR)
        self.screen.blit(step_text, (720, 400))
        self.screen.blit(cost_text, (720, 435))
        self.screen.blit(status_text, (720, 470))

        ui_config.draw_button(self.screen, self.back_button, self.font, "Back", ui_config.BACK_BUTTON_COLOR)
        ui_config.draw_button(self.screen, self.run_button, self.font, "Run", ui_config.ACTION_BUTTON_COLOR)
        ui_config.draw_button(self.screen, self.reset_button, self.font, "Reset", ui_config.ACTION_BUTTON_COLOR)