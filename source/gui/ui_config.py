import os


BASE_DIR = os.path.dirname(__file__)
ASSET_DIR = os.path.join(BASE_DIR, "assets")

BACKGROUND_IMAGE = os.path.join(ASSET_DIR, "background.png")
FLOOR_IMAGE = os.path.join(ASSET_DIR, "grass.png")
WALL_IMAGE = os.path.join(ASSET_DIR, "wall.png")
GOAL_IMAGE = os.path.join(ASSET_DIR, "goal.png")
BOX_IMAGE = os.path.join(ASSET_DIR, "box.png")
AGENT1_IMAGE = os.path.join(ASSET_DIR, "a1.png")
AGENT2_IMAGE = os.path.join(ASSET_DIR, "a2.png")


TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (0, 0, 0)

GRID_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (240, 240, 240)

SINGLE_BUTTON_COLOR = (40, 100, 180)
COMPETITIVE_BUTTON_COLOR = (200, 50, 70)
BACK_BUTTON_COLOR = (80, 90, 110)
BUTTON_BORDER_COLOR = (20, 40, 70)
BACK_BUTTON_COLOR = (80, 90, 110)

TITLE_FONT_SIZE = 50
BUTTON_FONT_SIZE = 35

TILE_SIZE = 64

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600