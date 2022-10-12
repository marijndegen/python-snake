import arcade
import os
from matplotlib.style import available
import pyglet
import time
import datetime
from snake import Snake

# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake game Marijn"

# row
COLUMN_SPACING = 21
ROW_SPACING = 21
ROWS = 25
COLS = 25
SQUARE_SIZE = 20


class PlayBoard(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
        self.snake = Snake()
        self.started = False
        self.gameTime = 0

    def on_draw(self):
        # Render the screen.
        arcade.start_render()
        self.clear()
        self.gameTime += 1

        if self.snake.alive:
            self.snake.moving(self.gameTime)

        left, screen_width, bottom, screen_height = self.get_viewport()

        # Draw the background
        for row in range(ROWS):
            for column in range(COLS):
                # Calculate our location
                x = column * COLUMN_SPACING + \
                    screen_width // 2 - (ROW_SPACING * ROWS / 2)
                y = row * ROW_SPACING + screen_height // 2 - \
                    (COLUMN_SPACING * COLS / 2)
                arcade.draw_xywh_rectangle_filled(
                    x, y, SQUARE_SIZE, SQUARE_SIZE, arcade.color.AO)

        # Draw the snake
        for el in self.snake.list:
            x = el.col * COLUMN_SPACING + \
                screen_width // 2 - (ROW_SPACING * ROWS / 2)
            y = el.row * ROW_SPACING + screen_height // 2 - \
                (COLUMN_SPACING * COLS / 2)
            arcade.draw_xywh_rectangle_filled(
                x, y, SQUARE_SIZE, SQUARE_SIZE, el.color)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        availableKeys = {arcade.key.W: 'up', arcade.key.A: 'left',
                         arcade.key.S: 'down', arcade.key.D: 'right'}

        if key in availableKeys.keys() and self.started:
            self.snake.addKeyToQueue(availableKeys[key])

        if(not self.started):
            self.started = True

        # if key is arcade.key.ENTER and self.started is False:
        #     self.started = True


def main():
    """ Main function """
    PlayBoard()
    arcade.run()


if __name__ == "__main__":
    main()
