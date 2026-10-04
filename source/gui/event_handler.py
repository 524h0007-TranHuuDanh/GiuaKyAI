import pygame


class EventHandler:
    def __init__(self, screen_controller):
        self.screen_controller = screen_controller

    def handle_mode_menu(self, mouse_position):
        if self.screen_controller.main_menu_screen.single_button.collidepoint(mouse_position):
            self.screen_controller.mode = "single"
            self.screen_controller.load_map_names()
            self.screen_controller.screen_state = "map"

        elif self.screen_controller.main_menu_screen.competitive_button.collidepoint(mouse_position):
            self.screen_controller.mode = "competitive"
            self.screen_controller.load_map_names()
            self.screen_controller.screen_state = "map"

    def handle_map_menu(self, mouse_position):
        if self.screen_controller.map_select_menu_screen.back_button.collidepoint(mouse_position):
            self.screen_controller.mode = None
            self.screen_controller.selected_map = None
            self.screen_controller.screen_state = "mode"
            return

        for button, map_name in self.screen_controller.map_select_menu_screen.map_buttons:
            if button.collidepoint(mouse_position):
                self.screen_controller.select_map(map_name)
                return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos

                if self.screen_controller.screen_state == "mode":
                    self.handle_mode_menu(mouse_position)

                elif self.screen_controller.screen_state == "map":
                    self.handle_map_menu(mouse_position)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.screen_controller.screen_state == "map":
                        self.screen_controller.mode = None
                        self.screen_controller.selected_map = None
                        self.screen_controller.screen_state = "mode"
                    else:
                        return False

        return True