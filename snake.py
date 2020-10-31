import pygame
import random
from pygame.locals import *
from pygame import font as pygame_font


def on_grid_random():
    """This method generate the aleatory position of apple
    :retun apple position on screen
    :rtype tuple
    """
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // 10 * 10, y // 10 * 10


def wall_limit(snake_posit):
    """This method generate the wall limit
    :param snake_posit: position of snake
    :type snake_posit: tuple
    :return: collision or not
    :rtype: int
    """
    if snake_posit > (600, -1):
        return 1
    if snake_posit > (600, 600):
        return 1
    if snake_posit < (-1, -1):
        return 1
    if snake_posit < (-1, 600):
        return 1

    for x_posit in range(0, 600):
        if snake_posit == (x_posit, 600):
            return 1
        if snake_posit == (x_posit, -10):
            return 1
    return 0


def collision_snake_apple(snake, apple):
    """This method generate the collision of the snake with the apple
    :param snake: snake head
    :type snake: tuple
    :param apple: apple position on screen  
    :type apple: tuple
    :return snake collision with apple
    :rtype: tuple
    """
    return snake[0] == apple[0] and snake[1] == apple[1]


def collision_snake_body(snake_head, snake_body):
    """This method generate the collision of the snake with herself
    :param snake_head: head of snake
    :type snake_head: tuple
    :param snake_body: body of snake
    :type snake_body: list
    :return snake collision with herself or not
    :rtype tuple
    """
    if snake_head in snake_body:
        return 1
    return 0

def run(screen, snake, snake_skin, apple, apple_pos, sysfont, score):
    """This method is responsible for run the game
    :param screen: the game screen
    :type screen: tuple
    :param snake: the snake
    :type snake: list
    :param snake_skin: the snake skin
    :type snake_skin: tuple
    :param apple: the apple
    :type apple: tuple
    :param apple_pos: the apple position on screen
    :type apple_pos: tuple
    :param sysfont: the font render of the game
    :type sysfont: tuple
    :param score: the score of the game
    :type score: tuple 
    """
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    my_direction = LEFT
    plus_one = 0
    
    clock = pygame.time.Clock()

    while True:
        clock.tick(20)
 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_RIGHT:
                    my_direction = RIGHT
                if event.key == K_LEFT:
                    my_direction = LEFT
        
        if collision_snake_apple(snake[0], apple_pos):
            plus_one += 1
            apple_pos = on_grid_random()
            snake.append((0, 0))

        points = sysfont.render(str(plus_one), True, (255, 255, 255))


        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
            
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)

        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])

        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        if collision_snake_body(snake[0], snake[1:]) != 0:
            pygame.quit()
        
        if wall_limit(snake[0]) != 0:
                pygame.quit()

        for posit in range(len(snake) - 1, 0, -1):
            snake[posit] = (snake[posit - 1][0], snake[posit - 1][1])

        screen.fill((0, 0, 0))
        screen.blit(score, (1, 1))
        screen.blit(points, (65, 1))
        screen.blit(apple, apple_pos)

        for position in snake:
            screen.blit(snake_skin, position)

        pygame.display.update()


def main():
    """This method is responsible for render the elements of the game

    """
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('snake game')

    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((255, 255, 255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))

    pygame_font.init()
    sysfont = pygame_font.Font(None, 30)
    screen.fill((10, 10, 10))
    score = sysfont.render('score: ', True, (255, 255, 255))

    run(screen, snake, snake_skin, apple, apple_pos, sysfont, score)


if __name__ == '__main__':
    main()
