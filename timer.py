import pygame as pg
import sys

# === Constants ===
start_time = 20  # how many seconds to being the timer with
interval = 20  # how many seconds to add

fontsize = 200  # font size

win_w, win_h = 1920, 1080
win_dimen = (win_w, win_h)
win = pg.display.set_mode(win_dimen, pg.FULLSCREEN)
pg.display.set_caption("timer")
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

clock = pg.time.Clock()


def delay(seconds):
    """function to pause/delay"""
    pg.time.delay(int((seconds*1000)))


def text_objects(text, color):
    """text object defining text"""
    msg = pg.font.SysFont("arial", fontsize)
    text_surf = msg.render(text, True, color)
    return text_surf, text_surf.get_rect()


def msg_to_screen(text, textcolor):
    """function to render message to screen centered"""
    text_surface, text_rect = text_objects(text, textcolor)
    text_rect.center = (win_w/2), (win_h/2)
    win.blit(text_surface, text_rect)


def main():
    """Main timer loop"""
    initial_time = start_time
    done = False
    pg.init()
    t0 = pg.time.get_ticks()

    # == Quit loop ==
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                # == Press escape to exit
                if event.key == pg.K_ESCAPE:
                    done = True
                # == Press space to add 20 seconds
                if event.key == pg.K_SPACE:
                    initial_time += interval
        win.fill(WHITE)
        t1 = ((pg.time.get_ticks()-t0)/1000)

        if not t1 >= initial_time:
            msg_to_screen("Time remaining: {:2.1f}".format(initial_time - t1), BLACK)
        else:
            msg_to_screen("Time's up!", BLACK)

        pg.display.update()
        clock.tick(60)

    pg. quit()
    sys.exit()


if __name__ == "__main__":
    main()
