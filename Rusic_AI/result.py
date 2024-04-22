import pygame as pg
import sys


class Game:
    def __init__(self):
        pg.font.init()
        font = pg.font.SysFont('Comic Sans MS', 20)

        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60

        self.switch = pg.image.load('./arts/коммутатор.png')
        self.router = pg.image.load('./arts/маршрутизатор.png')
        self.computer = pg.image.load('./arts/ЭВМ.png')

        self.line_colors = ['red', 'yellow', 'green', 'white']

        self.probability_1 = font.render('Соединение 1: 50%', False, pg.Color('white'))
        self.probability_2 = font.render('Соединение 2: 50%', False, pg.Color('white'))
        self.probability_3 = font.render('Соединение 3: 50%', False, pg.Color('white'))
        self.probability_4 = font.render('Соединение 4: 50%', False, pg.Color('white'))
        self.probability_5 = font.render('Соединение 5: 50%', False, pg.Color('white'))
        self.probability_6 = font.render('Соединение 6: 50%', False, pg.Color('white'))
        self.probability_7 = font.render('Соединение 7: 50%', False, pg.Color('white'))
        self.probability_8 = font.render('Соединение 8: 50%', False, pg.Color('white'))
        self.probability_9 = font.render('Соединение 9: 50%', False, pg.Color('white'))
        self.probability_10 = font.render('Соединение 10: 50%', False, pg.Color('white'))

        self.close = font.render('Для выхода из этого окна нажмите - q', False, pg.Color('white'))

    def draw_all(self):
        """
        drawing all objects and connections
        """
        window = pg.display.set_mode((self.WIDTH, self.HIGH))
        clock = pg.time.Clock()

        window.fill(pg.Color('black'))

        # connections: computer - router
        pg.draw.line(window, pg.Color(self.line_colors[-1]), [30 + 55, 360 + 30], [150, 360 + 30], 3)
        pg.draw.line(window, pg.Color(self.line_colors[-1]), [570 + 50, 360 + 30], [700 - 5, 360 + 30], 3)

        # connections: switch - router
        pg.draw.line(window, pg.Color(self.line_colors[2]), [570 - 5, 360 + 30], [370 + 55, 360 + 30], 3)
        pg.draw.line(window, pg.Color(self.line_colors[2]), [570 - 5, 360 + 30], [370 + 55, 160 + 30], 3)
        pg.draw.line(window, pg.Color(self.line_colors[1]), [570 - 5, 360 + 30], [370 + 55, 560 + 30], 3)

        pg.draw.line(window, pg.Color(self.line_colors[1]), [150 + 55, 360 + 30], [370 - 5, 360 + 30], 3)
        pg.draw.line(window, pg.Color(self.line_colors[0]), [150 + 55, 360 + 30], [370 - 5, 160 + 30], 3)
        pg.draw.line(window, pg.Color(self.line_colors[0]), [150 + 55, 360 + 30], [370 - 5, 560 + 30], 3)

        # connections: switch - switch
        pg.draw.line(window, pg.Color(self.line_colors[-1]), [370 + 25, 360 + 15], [370 + 25, 160 + 55], 3)
        pg.draw.line(window, pg.Color(self.line_colors[-1]), [370 + 25, 360 + 55], [370 + 25, 560 + 15], 3)

        # Draw switch
        window.blit(self.switch, [370, 360])
        window.blit(self.switch, [370, 160])
        window.blit(self.switch, [370, 560])

        # Draw router
        window.blit(self.router, [150, 360])
        window.blit(self.router, [570, 360])

        # Draw computer
        window.blit(self.computer, [30, 360])
        window.blit(self.computer, [700, 360])

        # Draw probabilities of the net
        window.blit(self.probability_1, (900, 30))
        window.blit(self.probability_2, (900, 60))
        window.blit(self.probability_3, (900, 90))
        window.blit(self.probability_4, (900, 120))
        window.blit(self.probability_5, (900, 150))
        window.blit(self.probability_6, (900, 180))
        window.blit(self.probability_7, (900, 210))
        window.blit(self.probability_8, (900, 240))
        window.blit(self.probability_9, (900, 270))
        window.blit(self.probability_10, (900, 300))

        window.blit(self.close, (850, 650))

        pg.display.update()
        clock.tick(self.FPS)

    def start_game(self):
        run = True
        while run:
            self.draw_all()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        run = False
                        pg.quit()


# if __name__ == '__main__':
#     game = Game()
#     game.start_game()
