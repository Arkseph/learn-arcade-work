""" This is my First Drawing in
 Python"""
import arcade

arcade.open_window(1000, 800, "First Drawing")

arcade.set_background_color((20, 228, 255, 0))

arcade.start_render()

# Draw the Sea
arcade.draw_lrtb_rectangle_filled(0, 999, 400, 0, arcade.csscolor.NAVY)

# Draw the Sand
arcade.draw_lrtb_rectangle_filled(0, 999, 200, 0, arcade.csscolor.LIGHT_YELLOW)

# Draw the Sun
arcade.draw_circle_filled(100, 700, 60, arcade.csscolor.YELLOW)

# Draw the Sun's Rays
arcade.draw_line(30, 799, 170, 590, arcade.color.YELLOW, 8)
arcade.draw_line(30, 590, 170, 799, arcade.color.YELLOW, 8)
arcade.draw_line(5, 700, 230, 700, arcade.color.YELLOW, 8)
arcade.draw_line(100, 798, 100, 590, arcade.color.YELLOW, 8)

# Draw Cloud 1
arcade.draw_ellipse_filled(930, 700, 250, 50, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(990, 730, 250, 50, arcade.csscolor.WHITE)

# Draw Could 2
arcade.draw_ellipse_filled(500, 740, 120, 60, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(450, 710, 120, 60, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(550, 710, 120, 60, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(500, 690, 120, 60, arcade.csscolor.WHITE)

# Draw a Boat
arcade.draw_ellipse_filled(270, 320, 150, 30, arcade.csscolor.WHITE)
arcade.draw_triangle_filled(300, 500, 290, 320, 230, 320, arcade.csscolor.LIME_GREEN)

# Draw Tent
arcade.draw_polygon_filled(((800, 320),
                            (700, 160),
                           (730, 120),
                           (920, 120),
                           (940, 160)
                            ), arcade.csscolor.DARK_RED)
arcade.draw_triangle_filled(800, 300, 740, 125, 860, 125, arcade.csscolor.BLACK)

arcade.finish_render()

arcade.run()
