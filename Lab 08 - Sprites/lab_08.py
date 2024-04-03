import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_METEOR = 0.5
STAR_COUNT = 50
METEOR_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

point_sound = arcade.load_sound("point.ogg")
impact_sound = arcade.load_sound("impact.ogg")


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def on_update(self, delta_time: float = 1 / 60) -> None:

        # Movement
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Meteor(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def reset_pos(self):
        # Reset to the top of the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def on_update(self, delta_time: float = 1 / 60) -> None:
        # Movement
        self.center_y -= 1

        # when out-of-bounds reset
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self):
        """ Initializer """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.meteor_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # hiding the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.COOL_BLACK)

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the UFO (player)
        self.player_sprite = arcade.Sprite("sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Creating the stars
        for i in range(STAR_COUNT):

            # Adding the stars (good sprites)
            coin = Coin("star.png", SPRITE_SCALING_METEOR)
            # stars position
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            self.coin_list.append(coin)

        # Adding the meteors (bad sprites)
        for m in range(METEOR_COUNT):

            meteor = Meteor("meteor.png", SPRITE_SCALING_COIN)

            # meteors position
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)
            meteor.change_x = random.randrange(-3, 4)
            meteor.change_y = random.randrange(-3, 4)

            self.meteor_list.append(meteor)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.meteor_list.draw()
        self.player_list.draw()

        # text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.score <= -3:
            over = f"Game Over"
            arcade.draw_text(over, 300, 300, arcade.color.WHITE, 28)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if self.score > -3:
            # center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self.score > -3:
            # Calling update on all sprites
            self.coin_list.on_update(delta_time)
            self.meteor_list.on_update(delta_time)

            # list sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.coin_list)

            # Loop through each colliding sprite, remove, and add to the score.
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(point_sound)

            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.meteor_list)

            for meteor in hit_list:
                meteor.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(impact_sound)


def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
