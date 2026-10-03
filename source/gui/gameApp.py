import pygame

from .menu import Menu
from .mapRenderer import MapRenderer


class GameApp:
    def __init__(self, singleData, competitiveData):
        pygame.init()

        # Kích thước cửa sổ
        self.width = 800
        self.height = 600
        self.tileSize = 50

        # Tạo cửa sổ
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sokoban AI")

        # Tạo menu
        self.menu = Menu(self.screen)

        # Tạo phần vẽ map
        self.mapRenderer = MapRenderer(self.screen, self.tileSize)

        # Dữ liệu của 2 mode
        self.singleData = singleData
        self.competitiveData = competitiveData

        # Mode hiện tại
        self.mode = None

        # Điều khiển vòng lặp game
        self.running = True

    # Xử lý event
    def handleEvents(self):
        for event in pygame.event.get():

            # Nhấn nút X
            if event.type == pygame.QUIT:
                self.running = False

            # Click chuột
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = event.pos

                # Chỉ kiểm tra button khi đang ở menu
                if self.mode is None:

                    if self.menu.singleButton.collidepoint(mousePosition):
                        self.mode = "single"

                    elif self.menu.competitiveButton.collidepoint(mousePosition):
                        self.mode = "competitive"

            # Nhấn bàn phím
            if event.type == pygame.KEYDOWN:

                # ESC
                if event.key == pygame.K_ESCAPE:

                    # Nếu đang chơi -> quay lại menu
                    if self.mode is not None:
                        self.mode = None

                    # Nếu đang ở menu -> thoát chương trình
                    else:
                        self.running = False

    # Vẽ giao diện
    def draw(self):

        # Chưa chọn mode -> hiện menu
        if self.mode is None:
            self.menu.draw()
            return

        # Chọn dữ liệu theo mode
        if self.mode == "single":
            data = self.singleData

        elif self.mode == "competitive":
            data = self.competitiveData

        # Xóa màn hình cũ
        self.screen.fill((230, 230, 230))

        # Vẽ map
        self.mapRenderer.draw(
            data["walls"],
            data["state"],
            data["rows"],
            data["columns"]
        )

    # Chạy chương trình
    def run(self):
        while self.running:

            self.handleEvents()

            self.draw()

            pygame.display.flip()

        pygame.quit()