from turtle import Screen
from alien import Aliens
from ship import Ship
from alien_bullet import AlienBullets
from bullet import Bullets
from scoreboard import ScoreBoard, SeparateLine
import time
import random

# A random for the alien's bullets out
possibility = [i for i in range(10)]


# Bullet shot out from the ship
def ship_bullet_out():
    # Restrict the bullets are maximum 3 on the screen
    if len(bullets.bullets_list) < 3:
        bullets.create_bullet(ship_x=ship_pos_x)
    # bullets.create_bullet(ship_x=ship_pos_x)


# Bullet shot out from the alien ship
def alien_bullet_out():
    alien_bullets.create_alien_bullet(alien_cor=(btm_row_x, btm_row_y - 30))


# Check if the bullet from ship is out of the screen
def ship_bullet_out_frame():
    for b in bullets.bullets_list:
        if b.ycor() > 450:
            bullets.remove_bullet(bullet=b)


# Check if the bullet from alien ship is out of the screen
def alien_bullet_out_out_frame():
    for b in alien_bullets.alien_bullets_list:
        if b.ycor() < -420:
            alien_bullets.remove_bullet(bullet=b)


# Check if the alien bullets collide with the ship
def collision_ship():
    global is_game_on
    for a_bullet in alien_bullets.alien_bullets_list:
        if a_bullet.ycor() < -375 and a_bullet.distance(ship) < 15:
            # print("Collide with Ship")

            alien_bullets.remove_bullet(bullet=a_bullet)
            alien_bullets.reset_alien_bullet()

            scoreboard.lives -= 1
            scoreboard.update_lives()

            if scoreboard.lives == 0:
                is_game_on = False


# Check if the ship bullets collide with the alien ships
def collision_alien_ship():
    for alien_x in aliens.aliens_list:
        for alien in alien_x:
            for b in bullets.bullets_list:
                if b.ycor() > (alien.ycor() - 32) and b.distance(alien) < 20:
                    # print("Collide with Alien")
                    alien_col = aliens.aliens_list.index(alien_x)
                    aliens.remove_alien(alien=alien, col=alien_col)
                    bullets.remove_bullet(bullet=b)

                    scoreboard.scores += 1
                    scoreboard.update_scores()


# Check if the ship bullets collide with the alien ships' bullets, remove bullets if yes
def collision_bullets():
    for a_bullet in alien_bullets.alien_bullets_list:
        for b in bullets.bullets_list:
            if b.ycor() > (a_bullet.ycor() - 17) and b.distance(a_bullet) < 12:
                # print("Two Bullets Collide")
                alien_bullets.remove_bullet(bullet=a_bullet)
                bullets.remove_bullet(bullet=b)


# Initialize and set the screen
screen = Screen()
screen.setup(width=1200, height=1000)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.tracer(0)

# Add new shapes to turtle
screen.register_shape('./img/ship.gif')
screen.register_shape('./img/alien_ship.gif')

# Initialize and objects
ship = Ship()
aliens = Aliens()
alien_bullets = AlienBullets()
bullets = Bullets()

separate_line = SeparateLine()
scoreboard = ScoreBoard()

# Define the movement by keystrokes
screen.listen()
screen.onkey(fun=ship.move_right, key="Right")
screen.onkey(fun=ship.move_left, key="Left")
screen.onkey(fun=ship_bullet_out, key="space")

# The parameter to know whether it's game over
is_game_on = True


while is_game_on:
    screen.update()

    # Alien ships move right and left between the frame
    aliens.get_last_col()
    aliens.get_first_col()
    aliens.herd_move()

    # Get ship's x coordination
    ship_pos_x = ship.get_x_cor()

    # Ship Bullets move up
    for bullet in bullets.bullets_list:
        bullet.move()

    # Alien Bullet out randomly from the bottom of each column of the alien ships
    if random.choice(possibility) == 1:
        random_col = random.randint(0, len(aliens.quantity_list)-1)
        if aliens.quantity_list[random_col] > 0:
            btm_row_y = aliens.aliens_list[random_col][0].ycor()
            btm_row_x = aliens.aliens_list[random_col][0].xcor()
            # print(f"In col {random_col}'s btm row y: {btm_row_y}")
            alien_bullet_out()

    # Alien Bullets move down
    for alien_bullet in alien_bullets.alien_bullets_list:
        alien_bullet.move()

    # Check whether the bullets are out of the frame and the collision of objects
    ship_bullet_out_frame()
    alien_bullet_out_out_frame()
    collision_ship()
    collision_alien_ship()
    collision_bullets()

    time.sleep(0.05)


# Show game over when the lives run out
if not is_game_on:
    scoreboard.game_over()


screen.exitonclick()

