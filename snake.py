import arcade
from tile import Tile


class Snake:
    def __init__(self):
        self.keyQueue = []
        self.list = [Tile(5, 5, arcade.color.AERO_BLUE)]
        self.direction = None
        self.alive = False
        self.time = None
        self.addTile = False

    def addKeyToQueue(self, key):
        if not self.alive:
            self.alive = True

        # overwrite direction here
        direction = self.direction

        if direction == None:
            self.keyQueue.append(key)
            return

        print(self.keyQueue)

        if self.keyQueue[-1:]:  # -1 causes index out of range exception
            direction = self.keyQueue[-1:]

        print('direction,', direction)
        print('key,', key)

        if key == 'left' and direction != 'right' and direction != 'left':
            self.keyQueue.append(key)

        if key == 'right' and direction != 'right' and direction != 'left':
            self.keyQueue.append(key)

        if key == 'up' and direction != 'up' and direction != 'down':
            self.keyQueue.append(key)

        if key == 'down' and direction != 'up' and direction != 'down':
            self.keyQueue.append(key)

        # if (key == 'up' or key == 'down') and (direction == 'right' or direction == 'left'):
        #     self.keyQueue.append(key)
        #     return

        # if (key == 'right' or key == 'left') and (direction == 'up' or direction == 'down'):
        #     self.keyQueue.append(key)
        #     return

        # print(key, direction)

    def moving(self, gameTime):
        if gameTime % 15 == 0:
            self.move()

    def move(self):
        if len(self.keyQueue) > 0:
            self.direction = self.keyQueue.pop(0)

        currentHead = self.list[0]
        currentHead.color = arcade.color.ALMOND
        col = currentHead.col
        row = currentHead.row

        if self.direction == "up":
            row += 1
        elif self.direction == "down":
            row -= 1
        elif self.direction == "left":
            col -= 1
        elif self.direction == "right":
            col += 1
        self.list.insert(0, Tile(row, col, arcade.color.AERO_BLUE))

        if not self.addTile:
            self.list.pop(-1)
        self.addTile = False

    def isSnakeTile(self, tile):
        for t in self.list:
            if t.row == tile.row and t.col == tile.col:
                return True
        return False
