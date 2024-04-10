
import arcade
import random

SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.8

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "lab 9"

NUMBER_OF_COINS = 30

MOVEMENT_SPEED = 5

# Sounds from freesound.org
point_sound = arcade.load_sound("point.ogg")
music = arcade.load_sound("music.mp3")


class MyGame(arcade.Window):

    arcade.play_sound(music)

    def __init__(self):
        # parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # the player
        self.player_sprite = None

        self.physics_engine = None

    def setup(self):

        # background color
        arcade.set_background_color(arcade.color.JAPANESE_VIOLET)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Player image from kenney.nl
        self.player_sprite = arcade.Sprite("player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # all walls images from kenney.nl
        wall = arcade.Sprite("wall2.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("wall3.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 420
        self.wall_list.append(wall)

        wall = arcade.Sprite("wall1.png", SPRITE_SCALING_BOX)
        wall.center_x = 440
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("wall3.png", SPRITE_SCALING_BOX)
        wall.center_x = 500
        wall.center_y = 420
        self.wall_list.append(wall)

        wall = arcade.Sprite("wall2.png", SPRITE_SCALING_BOX)
        wall.center_x = 400
        wall.center_y = 500
        self.wall_list.append(wall)

        wall = arcade.Sprite("wall3.png", SPRITE_SCALING_BOX)
        wall.center_x = 370
        wall.center_y = 200
        self.wall_list.append(wall)

        # walls inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite("wall2.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for x in range(0, 800, 70):
            wall = arcade.Sprite("wall2.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 15
            self.wall_list.append(wall)

        for x in range(0, 800, 70):
            wall = arcade.Sprite("wall2.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 575
            self.wall_list.append(wall)

        # walls with a list
        coordinate_list = [[785, 295],
                           [785, 85],
                           [785, 155],
                           [785, 225],
                           [785, 365],
                           [785, 445],
                           [785, 515],
                           [15, 295],
                           [15, 85],
                           [15, 155],
                           [15, 225],
                           [15, 365],
                           [15, 445],
                           [15, 515]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall1.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # the coins
        for i in range(NUMBER_OF_COINS):
            # Coin(or bolt) image from kenney.nl
            coin = arcade.Sprite("bolt.png", SPRITE_SCALING_COIN)

            # Boolean variable
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:

                    coin_placed_successfully = True

            # adding the coin to the lists
            self.coin_list.append(coin)

        # physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        # Loop through each colliding sprite and add score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(point_sound)

    def on_key_press(self, key, modifiers):
        # keyboard settings
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
