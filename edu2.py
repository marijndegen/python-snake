import time
import arcade
import datetime


class Timer(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, 'Arcade Timer')
        self.time = None

    def on_draw(self):
        arcade.start_render()
        if self.time:
            text = str(datetime.timedelta(seconds=time.time()-self.time))
        else:
            text = 'Click to start timer!'

        arcade.draw_text(text, 300, 200, arcade.color.RED,
                         40, anchor_x='center')

    def on_mouse_release(self, x, y, button, key_modifiers):
        self.time = time.time() if not self.time else None


Timer()
arcade.run()
