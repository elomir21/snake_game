import pygame, random
from pygame.locals import *


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def on_grid_random():
    """This function generate the aleatory position of apple

    """
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


def wall_limit(snake_posit):
    """This function generate the wall limit
    :param snake_posit: position of snake
    :type snake_posit: tuple
    :return: 0 or 1
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


def collision_snake_apple(c1, c2):
    """This function generate the collision of the snake with the apple

    """
    return (c1[0] == c2[0] and c1[1] == c2[1])

def main():
    """This function is responsible for run the game

    """
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('snake game')

    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255, 255, 255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))

    my_direction = LEFT

    clock = pygame.time.Clock()


    while True:
        clock.tick(10)
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
            apple_pos = on_grid_random()
            snake.append((0, 0))

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
            if wall_limit(snake[0]) != 0:
                pygame.quit() 
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)  
        if my_direction == RIGHT:
           snake[0] = (snake[0][0] + 10, snake[0][1]) 
        if my_direction == LEFT:
           snake[0] = (snake[0][0] - 10, snake[0][1])

        for posit in range(len(snake) -1, 0, -1):
                snake[posit] = (snake[posit-1][0], snake[posit-1][1])
                if wall_limit(snake[posit]) != 0:
                    pygame.quit()
        
        screen.fill((0, 0, 0))
        screen.blit(apple, apple_pos)
        for position in snake:
            screen.blit(snake_skin, position)

        pygame.display.update()


if __name__ == '__main__':
    main()
