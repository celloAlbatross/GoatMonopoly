import arcade
from random import randint

GAME_TITLE = "Goat Monopoly"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class BetWindow(arcade.Window) :
    def __init__(self, width, height) :
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_draw(self) :
        arcade.start_render()

if __name__ == '__main__' :
    window = BetWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
