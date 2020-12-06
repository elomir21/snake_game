import os
import pygame
import random
from pygame.locals import *
from pygame import font as pygame_font


def initial_screen():
    """This method show initial screen

    """
    scored_points = ''
    if os.stat('../data/best_score.txt').st_size > 0:
            with open('../data/best_score.txt', 'r') as last_score:
                scored_points = last_score.read()

    while True:

        pygame.init
        screen = pygame.display.set_mode((400, 500))
        pygame.display.set_caption('SNAKE GAME')

        pygame_font.init()
        sysfont_title = pygame_font.Font(None, 50)
        sysfont_best_score = pygame_font.Font(None, 30)
        screen.fill((10, 10, 10))

        snake_game = sysfont_title.render('SNAKE GAME', True, (0, 0, 255))
        snake_game_posit = (85, 50)
        best_score = sysfont_best_score.render('BEST SCORE: ', True, (255, 255, 255))
        best_score_posit = (125, 120)

        color_font_button = (0, 0, 0)
        color_light = (170, 170, 170)
        shade_button = (255, 255, 0)
        sysfont_button = pygame_font.Font(None, 30)

        exit_width = screen.get_width() + 170
        exit_height = screen.get_height()
        exit_button = sysfont_button.render('EXIT', True, color_font_button)

        new_game_width = screen.get_width() + 170
        new_game_height = screen.get_height()
        new_game_button = sysfont_button.render('NEW GAME', True, color_font_button)

        points = sysfont_best_score.render(scored_points.strip('\n'), True, (255, 255, 255))
        points_posit = (270, 120)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_width/2-170 <= mouse[0] <= new_game_width/2 and new_game_height/2  <= mouse[1] <= new_game_height/2 + 40:
                    main()

                if exit_width/2 - 170 <= mouse[0] <= exit_width/2 and exit_height/2+50 <= mouse[1] <= exit_height/2 + 90:
                    pygame.quit()

        if new_game_width/2-170 <= mouse[0] <= new_game_width/2 and new_game_height/2  <= mouse[1] <= new_game_height/2 + 40:
            pygame.draw.rect(screen, color_light, [new_game_width/2, new_game_height/2, -170, 40])
        else:
            pygame.draw.rect(screen, shade_button, [new_game_width/2, new_game_height/2, -170, 40])

        if exit_width/2 - 170 <= mouse[0] <= exit_width/2 and exit_height/2+50 <= mouse[1] <= exit_height/2 + 90:
            pygame.draw.rect(screen, color_light, [exit_width/2, exit_height/2+50, -170, 40])
        else:
            pygame.draw.rect(screen, shade_button, [exit_width/2, exit_height/2+50, -170, 40])

        screen.blit(snake_game, snake_game_posit)
        screen.blit(best_score, best_score_posit)
        screen.blit(points, points_posit)
        screen.blit(new_game_button, (new_game_width/2 - 140, new_game_height/2 + 10))
        screen.blit(exit_button, (exit_width/2 - 110, exit_height/2 + 60))


        pygame.display.update()


def on_grid_random():
    """This method generate the aleatory position of apple
    :retun apple position on screen
    :rtype tuple
    """
    x = random.randint(40, 570)
    y = random.randint(40, 570)

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


def store_best_score(points):
    """This method store the best score of the game
    :param points: the best score of the game
    :type points: int
    """
    score_point = 0
    score_point += points

    if os.stat('../data/best_score.txt').st_size > 0:
        with open('../data/best_score.txt', 'r') as last_score:
            score = last_score.read()

            if score_point > int(score):
                with open('../data/best_score.txt', 'w+') as best_score:
                    best_score.write(str(score_point) + '\n')
    else:
        with open('../data/best_score.txt', 'w+') as init_score:
            init_score.write('1\n')


def game_over(points):
    """This method show game over screen
    :param points: hited points
    :type points: int
    """

    while True:

        pygame.init
        screen = pygame.display.set_mode((400, 200))
        pygame.display.set_caption('GAME OVER')

        pygame_font.init()
        sysfont = pygame_font.Font(None, 50)
        sysfont_score = pygame_font.Font(None, 30)
        screen.fill((10, 10, 10))

        game_over = sysfont.render('GAME OVER', True, (255, 0, 0))
        game_over_posit = (85, 20)
        score = sysfont_score.render('SCORE: ', True, (0, 0, 255))
        score_posit = (145, 70)

        color_font_button = (0, 0, 0)
        color_light = (170, 170, 170)
        shade_button = (255, 255, 0)
        sysfont_button = pygame_font.Font(None, 30)

        exit_width = screen.get_width()
        exit_height = screen.get_height()
        exit_button = sysfont_button.render('EXIT', True, color_font_button)

        new_game_width = screen.get_width() - 20
        new_game_height = screen.get_height()
        new_game_button = sysfont_button.render('NEW GAME', True, color_font_button)

        points_posit = (230, 70)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_width/2 <= mouse[0] <= exit_width/2 + 170 and exit_height/2 <= mouse[1] <= exit_height/2 + 40:
                    pygame.quit()
                if new_game_width/2 - 170 <= mouse[0] <= new_game_width/2 and new_game_height/2 <= mouse[1] <= new_game_height/2 + 40:
                    pygame.quit()
                    main()

        if exit_width/2 <= mouse[0] <= exit_width/2 + 170 and exit_height/2 <= mouse[1] <= exit_height/2 + 40:
            pygame.draw.rect(screen, color_light, [exit_width/2, exit_height/2, 170, 40])
        else:
            pygame.draw.rect(screen, shade_button, [exit_width/2, exit_height/2, 170, 40])

        if new_game_width/2-170 <= mouse[0] <= new_game_width/2 and new_game_height/2  <= mouse[1] <= new_game_height/2 + 40:
            pygame.draw.rect(screen, color_light, [new_game_width/2, new_game_height/2, -170, 40])
        else:
            pygame.draw.rect(screen, shade_button, [new_game_width/2, new_game_height/2, -170, 40])

        screen.blit(game_over, game_over_posit)
        screen.blit(score, score_posit)
        screen.blit(points, points_posit)
        screen.blit(exit_button, (exit_width/2 + 60, exit_height/2 + 10))
        screen.blit(new_game_button, (new_game_width/2 - 140, new_game_height/2 + 10))
        pygame.display.update()


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
        store_best_score(plus_one)


        snake_direction(my_direction, snake, UP, RIGHT, DOWN, LEFT)


        if collision_snake_body(snake) != 0:
            screen.blit(frame, (limit, 600))
            pygame.quit()
            game_over(points)

        if wall_limit(snake[0]) != 0:
            pygame.quit()
            game_over(points)


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
    score = sysfont.render('SCORE: ', True, (255, 255, 0))
    score_posit = (1, 5)
    points_posit = (85, 5)

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))


    run(
        screen, frame, snake, snake_skin,
        apple, apple_pos, sysfont,
        score, score_posit, points_posit
    )


if __name__ == '__main__':
    initial_screen()
