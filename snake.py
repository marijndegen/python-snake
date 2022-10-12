import arcade


class Snake:
    def __init__(self):
        self.keyQueue = []
        self.list = [Tile(5, 5, arcade.color.AERO_BLUE)]
        self.direction = None
        self.alive = False
        self.time = None

    def addKeyToQueue(self, key):
        self.keyQueue.append(key)
        print('add key to queue')
        print(key)

        if not self.alive:
            self.alive = True

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
        self.list.pop(-1)
        print(self.direction)


class Tile:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
