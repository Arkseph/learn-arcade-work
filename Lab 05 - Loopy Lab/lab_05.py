import arcade


def draw_section_outlines():

    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 5 + column * 10
            y = 5 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = 305 + column * 10
            y = 5 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.NAVY_BLUE)


def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = 605 + column * 10
            y = 5 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            if row % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.NAVY_BLUE)


def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = 905 + column * 10
            y = 5 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            if row % 2 == 1 or column % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.NAVY_BLUE)


def draw_section_5():
    for column in range(30):
        for row in range(column):
            x = 5 + column * 10
            y = 305 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(30-row):
            x = 305 + column * 10
            y = 305 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(30):
        for column in range(row):
            x = 605 + column * 10
            y = 305 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for ro in range(30):
        for c in range(30):
            x = 905 + c * 10
            y = 305 + ro * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    for column in range(30):
        for row in range(30-column):
            x = 905 + column * 10
            y = 305 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.AIR_FORCE_BLUE)


def main():

    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    draw_section_outlines()

    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
