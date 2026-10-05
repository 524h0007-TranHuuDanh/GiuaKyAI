import pygame


class EventHandler:
    def __init__(self, screen_controller):
        self.screen_controller = screen_controller

    def handle_mode_menu(self, mouse_position):
        menu = self.screen_controller.main_menu_screen

        if menu.single_button.collidepoint(mouse_position):
            self.screen_controller.mode = "single"
            self.screen_controller.load_map_names()
            self.screen_controller.screen_state = "map"

        elif menu.competitive_button.collidepoint(mouse_position):
            self.screen_controller.mode = "competitive"
            self.screen_controller.load_map_names()
            self.screen_controller.screen_state = "map"

    def handle_map_menu(self, mouse_position):
        menu = self.screen_controller.map_select_menu_screen

        if menu.back_button.collidepoint(mouse_position):
            self.screen_controller.go_to_mode_menu()
            return

        for button, map_name in menu.map_buttons:
            if button.collidepoint(mouse_position):
                self.screen_controller.select_map(map_name)
                return

    def handle_game(self, mouse_position):
        game = self.screen_controller.game_screen

        if game.back_button.collidepoint(mouse_position):
            game.pause()
            self.screen_controller.screen_state = "map"
            return

        if game.mode == "single":
            if game.ucs_button.collidepoint(mouse_position):
                game.algorithm = "UCS"
                return

            if game.astar_button.collidepoint(mouse_position):
                game.algorithm = "A*"
                return

        if game.mode == "competitive":
            game.input_active = game.input_box.collidepoint(mouse_position)

        if game.run_button.collidepoint(mouse_position):
            if game.mode == "single" and game.algorithm is not None:
                game.run_single(game.algorithm)

            elif game.mode == "competitive" and game.n_text:
                game.run_competitive(int(game.n_text))

            return

        if game.reset_button.collidepoint(mouse_position):
            game.reset()
            return

        if game.pause_button.collidepoint(mouse_position):
            game.toggle_pause()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.screen_controller.screen_state == "mode":
                    self.handle_mode_menu(event.pos)

                elif self.screen_controller.screen_state == "map":
                    self.handle_map_menu(event.pos)

                elif self.screen_controller.screen_state == "game":
                    self.handle_game(event.pos)

            if event.type == pygame.KEYDOWN:
                game = self.screen_controller.game_screen

                if self.screen_controller.screen_state == "game":
                    if event.key == pygame.K_SPACE:
                        game.toggle_pause()

                    elif event.key == pygame.K_LEFT:
                        game.prev()

                    elif event.key == pygame.K_RIGHT:
                        game.next()

                    elif event.key == pygame.K_BACKSPACE:
                        if game.mode == "competitive" and game.input_active:
                            game.n_text = game.n_text[:-1]

                    elif game.mode == "competitive" and game.input_active and event.unicode.isdigit():
                        game.n_text += event.unicode

                if event.key == pygame.K_ESCAPE:
                    if self.screen_controller.screen_state == "game":
                        game.pause()
                        self.screen_controller.screen_state = "map"

                    elif self.screen_controller.screen_state == "map":
                        self.screen_controller.go_to_mode_menu()

                    else:
                        return False

        return True