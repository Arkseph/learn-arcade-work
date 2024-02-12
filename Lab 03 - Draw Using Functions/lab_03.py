import arcade
arcade.open_window(1000, 800, "Second Drawing")

arcade.set_background_color((20, 228, 255, 0))

def cloud(x, y):
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_ellipse_filled(500+x, 740+y, 120, 60, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(450+x, 710+y, 120, 60, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(550+x, 710+y, 120, 60, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(500+x, 690+y, 120, 60, arcade.csscolor.WHITE)

def tree(x, y):
    # Tree
    arcade.draw_rectangle_filled(200+x, 200+y, 15, 60, arcade.color.BROWN)
    arcade.draw_triangle_filled(200+x, 300+y, 170+x, 220+y, 230+x, 220+y, arcade.csscolor.DARK_GREEN)
    arcade.draw_triangle_filled(200+x, 340+y, 170+x, 260+y, 230+x, 260+y, arcade.csscolor.DARK_GREEN)

def bird(x, y):
    # Draw a bird
    arcade.draw_parabola_outline(500+x, 600+y, 520+x, 30, arcade.color.BLACK, 10, 0)
    arcade.draw_parabola_outline(470+x, 600+y, 500+x, 30, arcade.color.BLACK, 10, 10)

def flower1(x,y):
    # Draw Flower
    arcade.draw_circle_filled(100+x, 100+y, 10, arcade.color.ROSE)
    arcade.draw_circle_filled(100+x, 100+y, 4, arcade.color.YELLOW)

def flower2(x, y):
    arcade.draw_circle_filled(200+x, 100+y, 10, arcade.color.BLUE)
    arcade.draw_circle_filled(200+x, 100+y, 4, arcade.color.YELLOW)

def flower3(x, y):
    arcade.draw_circle_filled(300+x, 100+y, 10, arcade.color.PURPLE)
    arcade.draw_circle_filled(300+x, 100+y, 4, arcade.color.YELLOW)

def main():


arcade.start_render()
# Grass
arcade.draw_lrtb_rectangle_filled(0, 999, 200, 0, arcade.csscolor.GREEN)

# Mountains
arcade.draw_ellipse_filled(200, 200,700,300,arcade.csscolor.GREEN)
arcade.draw_ellipse_filled(900, 200,900,500,arcade.csscolor.GREEN)

# Draw the Sun
arcade.draw_circle_filled(100, 700, 60, arcade.csscolor.YELLOW)

# Draw the Sun's Rays
arcade.draw_line(30, 799, 170, 590, arcade.color.YELLOW, 8)
arcade.draw_line(30, 590, 170, 799, arcade.color.YELLOW, 8)
arcade.draw_line(5, 700, 230, 700, arcade.color.YELLOW, 8)
arcade.draw_line(100, 798, 100, 590, arcade.color.YELLOW, 8)

cloud(0, 0)
cloud(350, -50)
cloud(-360, -30)

tree(0, 0)
tree(200, 20)
tree(-100, 30)
tree(500, 100)
tree(600, 0)
tree(700, 20)
tree(620, 150)

bird(100, 100)
bird(150, 120)
bird(90, 130)

flower1(0, 0)
flower1(120, 30)
flower1(220, 40)
flower1(330, 30)
flower1(440, -50)
flower1(660, 40)
flower1(880, 30)

flower2(0, 0)
flower2(170, 40)
flower2(270, -20)
flower2(370, 10)
flower2(500, -40)
flower2(700, 60)
flower2(110, -50)
flower2(20, -60)

flower3(0, 0)
flower3(-170, -20)
flower3(330, 0)
flower3(550, 0)
flower3(670, 0)

arcade.finish_render()

arcade.run()
