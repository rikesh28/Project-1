'''
Name(s): Rikesh Sapkota
CSC 201
Project 1

Use the ninja to hit rocks. Move the ninja using the left and right click on mouse.
If the ninja hits enough rocks before they escape, you win.


Document Assistance:
We received assistance from Professor Mueller to brainstorm our project


'''

from graphics2 import*
import time
import random
import math



WINDOW_WIDTH = 666
WINDOW_HEIGHT = 666
ROCK_SPEED = 5
NINJA_SPEED = 25
STAR_SPEED = -12
NUM_WIN = 20
STALL_TIME = 0.05
THRESHOLD = 75

def distance_between_points(point1, point2):
    '''
    Calculates the distance between two points
   
    Params:
    point1 (Point): the first point
    point2 (Point): the second point
   
    Returns:
    the distance between the two points
    '''
    p1x = point1.getX()
    p1y = point1.getY()
    p2x = point2.getX()
    p2y = point2.getY()
   
    return (math.sqrt((p2x - p1x) ** 2) + ((p2y - p1y) ** 2))

def outOfRange(rock_img):
    '''
    Compare the distances between Y coordinate of rock and bottom end of window
    
    params:
    bottom_end = end point of window height
    rock_y_coordinate = Y coordinate of image rock
    
    returns:
    True if the Y coordinate is greater than height of the window
    
    '''
    
    bottom_end =  WINDOW_HEIGHT       
    rock_y_coordinate = rock_img.getCenter().getY()
   
    if rock_y_coordinate > bottom_end:   # checks whether the rock is out of the window or not
        return True
    else:
        return False
   
   
def is_close_enough(other_img, rock_img):
    '''
    Determines if the ninja or star is close enough to the rock to say the star
    hit the rock or rock hits the ninja.
   
    Params:
    other_img (Image): the image of object that might be close to the rock_img
    rock_img (Image): the image of the rock
   
    Returns:
    True if the ninja hits the rock
    
    '''
   
    other_center = other_img.getCenter() 
    rock_center = rock_img.getCenter()
   
    distance = distance_between_points(other_center, rock_center)
   
    if distance < THRESHOLD:  
        return True
   
    else:
        return False
    
   
def move_rock(rock_img_list):
    '''
    Moves every rock one Rock_SPEED unit down the window
   
    Params:
    rock_img_list (list): the list of falling rocks
   
    '''
   
    for rock in rock_img_list:
        rock.move(0, ROCK_SPEED)
        
        
def move_star(star_img_list):
    '''
    Moves every star one STAR_SPEED unit up the window
   
    Params:
    star_img_list (list): the list of shooting stars.
   
    '''
   
    for star in star_img_list:
        star.move(0, STAR_SPEED)        
       
def move_ninja(window, ninja_img):
    '''
    Each time the user click on left of the ninja it moves Ninja_SPEED units left and
    each time the user click on right of the ninja it moves Ninja_SPEED units right.
   
    window (GraphWin): the window where game play takes place
    ninja_img (Image): the ninja image
    
    '''
   
    click = window.checkMouse()

# Finding the co-ordinates of the ninja image to determine whether to move the ninja to the left and right or not if the click of the user is not none

    if click != None:
        left_edge = (ninja_img.getCenter()).getX() - (ninja_img.getWidth() / 2)
        right_edge = (ninja_img.getCenter()).getX() + (ninja_img.getWidth() / 2)
        top_edge = (ninja_img.getCenter()).getY() - (ninja_img.getHeight() / 2)
        bottom_edge = (ninja_img.getCenter()).getY() + (ninja_img.getHeight() / 2)

# Conditional Execution to determine whether the click is left or right of the ninja inorder to move it according to the clicks

        if click.getX() > right_edge and  top_edge < click.getY() < bottom_edge:
            ninja_img.move(NINJA_SPEED, 0)
           
        elif click.getX() < left_edge and top_edge < click.getY() < bottom_edge:
            ninja_img.move(- NINJA_SPEED, 0)
           
       
def add_rock_to_window(window):
    '''
    Adds one rock to the top of the window at a random location
   
    Params:
    window (GraphWin): the window where game play takes place
   
    Returns:
    the rock added to the window
    '''
    
    x_location = random.randrange(30, 601)
    rock = Image(Point(x_location, 0), "rock.gif")
    rock.draw(window)
    return rock


def add_star_to_window(window, ninja_img):
    '''
    Adds one star to just above the head of ninja at a specific X and Y location
    
    Params:
    window(GraphWin): the window where game play takes place
    
    Returns:
    the star added to the window
    
    '''
    xStar = ninja_img.getCenter().getX()
    yStar = ninja_img.getCenter().getY() - (ninja_img.getHeight() / 2)
    star = Image(Point(xStar, yStar), "star.gif")
    star.draw(window)
    return star

def end_game(ninja, rock):
    '''
    Ends the game and exit the code when the rock hits the ninja
    Also Pops up new window saying Game Over!
    
    Params:
    ninja (Image): the ninja image
    rock(Image): the rock image
    
    '''
    win = GraphWin('Loser!', WINDOW_WIDTH, WINDOW_HEIGHT)
    loser = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "gameover.gif")
    loser.draw(win)
    
     

def win_game(score):
    '''
    Ends the game and exit the code when the ninja hits enough rocks
    Also pops uo new window saying Winner Winner Chicken Dinner!
    
    Params:
    score = the score of a user visible on the window

    '''
    win = GraphWin('Winner!', WINDOW_WIDTH, WINDOW_HEIGHT)
    winner = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "win.gif")
    winner.draw(win)
    

        
    
    
def game_loop(window, ninja,):
    '''
    Loop continues to allow the rocks to fall and the ninja to move
    until enough rocks escape or the ninja hits enough rocks to
    end the game.
   
    Params:
    window (GraphWin): the window where game play takes place
    ninja (Image): the ninja image
    '''
    rock_list = []
    star_list = []
    score = 0
    scoreView = Text(Point(615, 28), f'Score: {score} ')
    scoreView.setSize(16)
    scoreView.draw(window)
    end = True
   
    while end and score < NUM_WIN:
        move_ninja(window, ninja)
       
        if random.randrange(100) < 6:
            rock = add_rock_to_window(window)
            rock_list.append(rock)
           
        move_rock(rock_list)
        
        key = window.checkKey()
        if key == 'space':
            star = add_star_to_window(window, ninja)
            star_list.append(star)

            
        move_star(star_list)

        for rocks in rock_list:
            for stars in star_list:
                if is_close_enough(stars, rocks):
                    rocks.undraw()
                    rock_list.remove(rocks)
                    stars.undraw()
                    star_list.remove(stars)
                    score += 1
                    scoreView.setText(f'Score: {score} ')
                    if score == NUM_WIN:
                        break            # Breaking the code and escaping this For Loop if the score equals wining points
            if score == NUM_WIN:
                break
            
        for rocks in rock_list:                        
            if outOfRange(rocks):
                rocks.undraw()
                rock_list.remove(rocks)
                score -= 1
                scoreView.setText(f'Score: {score} ')
                
            if is_close_enough(ninja, rocks):
                end = False
        

        
        
        time.sleep(STALL_TIME)

    # after while loop
    if score == NUM_WIN:
        window.close()
        win_game(score)
        
    else:
        window.close()
        end_game(ninja, rock)
                
                
               
def instruction_window():
    """
    Gives list of instructions to play this game to the user on the new window called instruction window
    
    """
    win = GraphWin("Instruction Window",600 ,600)
    win.setBackground('white')
    
    instruction1 = Text(Point(300,30), f'Welcome to Ninja star shooting Game!')
    instruction2 = Text(Point(300,90), f'You have to throw ninja stars at rocks to protect the base.')
    instruction3 = Text(Point(300,150), f'Press space key to launch stars from ninja.')
    instruction4 = Text(Point(300,210), f'Click on left and right of Ninja to move the ninja.')
    instruction5 = Text(Point(300,270), f'You will get 1 point every time when your star hits the rocks.')
    instruction6 = Text(Point(300,330), f'You will lose 1 point every time rock escapes the base.')
    instruction7 = Text(Point(300,390), f'You will win game when your score reaches {NUM_WIN}.')
    instruction8 = Text(Point(300,450), f'You will lose game when rock hits the ninja.')
    instruction9 = Text(Point(300, 510), f'Press any Key to Start the game')
    instruction1.setSize(25)
    instruction1.draw(win)
    instruction2.setSize(16)
    instruction2.draw(win)
    instruction3.setSize(16)
    instruction3.draw(win)
    instruction4.setSize(16)
    instruction4.draw(win)
    instruction5.setSize(16)
    instruction5.draw(win)
    instruction6.setSize(16)
    instruction6.draw(win )
    instruction7.setSize(16)
    instruction7.draw(win)
    instruction8.setSize(16)
    instruction8.draw(win)
    instruction9.draw(win)
    instruction9.setSize(16)
    
    key = win.getKey()
    win.close()
    
        
        
        
def main():

    instruction_window()
    
    
    window = GraphWin("Welcome to rock and ninja Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("white")
    
    background = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "background3.gif")
    background.draw(window)
    
    directions = Text(Point(333, 650), 'Click on left and right of Ninja to move the ninja.')
    directions.setTextColor('red')
    directions.setSize(18)
    directions.draw(window)
    
    
    ninja = Image(Point(325,580), "ninja.gif")
    ninja.draw(window)
   
    star = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "star.gif")
   
    game_loop(window, ninja,)
    
   
main()



