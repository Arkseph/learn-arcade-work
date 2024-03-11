""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

birds_sound = arcade.load_sound("birds.wav")
piano_sound = arcade.load_sound("piano.mp3")

class Sun:
    def __init__(self, position_x, position_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # mouse disappear when it is over the window.
        self.set_mouse_visible(False)

        # background
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

        # Create the Sun
        self.ball = Sun(500,50,50, arcade.color.ORANGE)
        self.ball = Sun(500, 50, 70, arcade.color.GOLD)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

        # Draw the ground
        arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, arcade.csscolor.DARK_GREEN)
        # Draw the Mountains
        arcade.draw_ellipse_filled(200, 200, 600, 200, arcade.csscolor.GREEN)
        arcade.draw_ellipse_filled(700, 200, 700, 400, arcade.csscolor.GREEN)

        # Draw cloud 1
        arcade.draw_ellipse_filled(500, 540, 120, 60, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(450, 510, 120, 60, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(550, 510, 120, 60, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(500, 490, 120, 60, arcade.csscolor.WHITE)
        # Draw cloud 2
        arcade.draw_ellipse_filled(200, 440, 120, 60, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(150, 410, 120, 60, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(250, 410, 120, 60, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(200, 390, 120, 60, arcade.csscolor.WHITE)

    def on_mouse_motion(self, x, y, dx, dy):
         self.ball.position_x = x
         self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        # Sound effects on clicks
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(birds_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(piano_sound)

def main():
    window = MyGame()
    arcade.run()


main()
