import arcade
import os
from matplotlib.style import available
import pyglet
import time
import datetime
import random

from snake import Snake
from tile import Tile

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
        self.foodTile = None

    def on_draw(self):
        # Render the screen.
        arcade.start_render()
        self.clear()
        self.gameTime += 1

        if self.snake.alive:
            self.snake.moving(self.gameTime)

        if self.snake.alive and self.snake.isSnakeTile(self.foodTile):
            self.snake.addTile = True
            self.foodTile = self.generateFoodTile()

        # Draw the background
        for row in range(ROWS):
            for column in range(COLS):
                x, y = self.calculateRowColPosition(row, column)
                arcade.draw_xywh_rectangle_filled(
                    x, y, SQUARE_SIZE, SQUARE_SIZE, arcade.color.AO)

        # Draw the snake
        for el in self.snake.list:
            x, y = self.calculateRowColPosition(el.row, el.col)
            arcade.draw_xywh_rectangle_filled(
                x, y, SQUARE_SIZE, SQUARE_SIZE, el.color)

        # Draw the foodtile
        if isinstance(self.foodTile, Tile):
            x, y = self.calculateRowColPosition(
                self.foodTile.row, self.foodTile.col)
            arcade.draw_xywh_rectangle_filled(
                x, y, SQUARE_SIZE, SQUARE_SIZE, self.foodTile.color)

    def calculateRowColPosition(self, row, col):
        # Calculate our location
        left, screen_width, bottom, screen_height = self.get_viewport()
        x = col * COLUMN_SPACING + \
            screen_width // 2 - (ROW_SPACING * ROWS / 2)
        y = row * ROW_SPACING + screen_height // 2 - \
            (COLUMN_SPACING * COLS / 2)
        return (x, y)

    def on_key_press(self, key, modifiers):
        availableKeys = {arcade.key.W: 'up', arcade.key.A: 'left',
                         arcade.key.S: 'down', arcade.key.D: 'right'}

        if(not self.started and key in availableKeys.keys()):
            self.started = True
            self.foodTile = self.generateFoodTile()

        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if self.started and key in availableKeys.keys():
            self.snake.addKeyToQueue(availableKeys[key])
            print('addkey')

    def generateFoodTile(self):
        tile = Tile(random.randint(0, ROWS - 1), random.randint(
            0, COLS - 1), arcade.color.BARBIE_PINK)

        if(self.snake.isSnakeTile(tile)):
            return self.generateFoodTile()

        return tile

        # if key is arcade.key.ENTER and self.started is False:
        #     self.started = True


def main():
    """ Main function """
    PlayBoard()
    arcade.run()


if __name__ == "__main__":
    main()
