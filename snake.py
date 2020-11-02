import pygame
import random
from pygame.locals import *
from pygame import font as pygame_font


def on_grid_random():
    """This method generate the aleatory position of apple
    :retun apple position on screen
    :rtype tuple
    """
    x = random.randint(40, 580)
    y = random.randint(40, 580)

    return x // 10 * 10, y // 10 * 10


def wall_limit(snake_posit):
    """This method generate the wall limit
    :param snake_posit: position of snake
    :type snake_posit: tuple
    :return: wall collision or not
    :rtype: int
    """
    if snake_posit > (590, -1):
        return 1
    if snake_posit > (590, 590):
        return 1
    if snake_posit < (0, -1):
        return 1
    if snake_posit < (0, 590):
        return 1

    for x_posit in range(0, 590):
        if snake_posit == (x_posit, 590):
            return 1
        if snake_posit == (x_posit, 30):
            return 1
    return 0


def collision_snake_apple(snake_head, apple_posit):
    """This method generate the collision of the snake with the apple
    :param snake_head: snake head
    :type snake: tuple
    :param apple_posit: apple position on screen
    :type apple: tuple
    :return snake collision with apple
    :rtype: tuple
    """
    return snake_head[0] == apple_posit[0] and snake_head[1] == apple_posit[1]


def collision_snake_body(snake):
    """This method generate the collision of the snake with herself
    :param snake: the snake body
    :type snake: list
    :return snake collision with herself or not
    :rtype tuple
    """
    if snake[0] in snake[1:]:
        return 1
    return 0


def snake_direction(direction, snake, up, right, down, left):
    """This method is responsible for move the snake on screen
    :param direction: direction of snake
    :type direction: int
    :param snake: snake body
    :type snake: list
    :param up: up direction
    :type up: int
    :param right: right direction
    :type right: int
    :param down: down direction
    :type down: int
    :param left: left direction
    :type left: int
    """
    if direction == up:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if direction == down:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if direction == right:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if direction == left:
        snake[0] = (snake[0][0] - 10, snake[0][1])


def run(
        screen, frame, snake, snake_skin,
        apple, apple_pos, sysfont,
        score, score_posit, points_posit
):
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
    :param score_posit: position of score on screen
    :type score_posit: tuple
    :param points_posit position of points on screen
    :type points_posit tuple
    """
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    my_direction = LEFT
    plus_one = 0

    clock = pygame.time.Clock()

    while True:
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction is not DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction is not UP:
                    my_direction = DOWN
                if event.key == K_RIGHT and my_direction is not LEFT:
                    my_direction = RIGHT
                if event.key == K_LEFT and my_direction is not RIGHT:
                    my_direction = LEFT

        if collision_snake_apple(snake[0], apple_pos):
            plus_one += 1
            apple_pos = on_grid_random()
            snake.append((0, 0))

        points = sysfont.render(str(plus_one), True, (255, 255, 255))


        snake_direction(my_direction, snake, UP, RIGHT, DOWN, LEFT)


        if collision_snake_body(snake) != 0:
            screen.blit(frame, (limit, 600))
            pygame.quit()

        if wall_limit(snake[0]) != 0:
            pygame.quit()


        for posit in range(len(snake) - 1, 0, -1):
            snake[posit] = (snake[posit - 1][0], snake[posit - 1][1])

        screen.fill((0, 0, 0))

        for limit in range(590):
            screen.blit(frame, (limit, 590))
            screen.blit(frame, (limit -9, 30))

        for up in range(30, 590):
            screen.blit(frame, (590, up))
            screen.blit(frame, (0, up))

        for position in snake:
            screen.blit(snake_skin, position)

        screen.blit(score, score_posit)
        screen.blit(points, points_posit)
        screen.blit(apple, apple_pos)

        pygame.display.update()


def main():
    """This method is responsible for render the elements of the game

    """
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('snake game')

    frame = pygame.Surface((10, 10))
    frame.fill((0, 0, 255))

    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((255, 255, 0))

    pygame_font.init()
    sysfont = pygame_font.Font(None, 30)
    screen.fill((10, 10, 10))
    score = sysfont.render('score: ', True, (255, 255, 255))
    score_posit = (1, 1)
    points_posit = (65, 1)

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))


    run(
        screen, frame, snake, snake_skin,
        apple, apple_pos, sysfont,
        score, score_posit, points_posit
    )


if __name__ == '__main__':
    main()
