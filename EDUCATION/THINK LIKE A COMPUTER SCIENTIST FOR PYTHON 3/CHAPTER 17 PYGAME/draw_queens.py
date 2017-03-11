import pygame

gravity = 0.01
my_clock = pygame.time.Clock()

class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this target position on the board """
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)  # start ball at top of its column
        self.y_velocity = 0 # with zero initial velocity

    def update(self):
        self.y_velocity += gravity # gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity # velocity moves the ball
        (target_x, target_y) = self.target_posn # unpack the position
        dist_to_go = target_y - new_y_pos   # how far to our floor

        if dist_to_go < 0:                              # are we under the floor ?
            self.y_velocity = -0.65 * self.y_velocity   # bounce
            new_y_pos = target_y + dist_to_go           # move back above floor
        self.posn = (x, new_y_pos)


    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -0.3 #kicks the sprite up


class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count +1) % 60
            self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0, 50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()/10
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)


def draw_board(the_board):
    """ Draw a chess board with queens, from the board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]   # set up colors - red, black

    n = len(the_board)
    surface_sz = 480
    sq_sz = surface_sz // n
    surface_sz = n * sq_sz # adjusts main surface size to fit the n smaller squares exactly

    # create the surface pf width, height and its window
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.image.load("ball2.jpg")

    # load the sprite sheet
    duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")

    # instantiate two duke instances, put them on the chess board
    duke1 = DukeSprite(duke_sprite_sheet, (sq_sz*2, 0))
    duke2 = DukeSprite(duke_sprite_sheet, (sq_sz*5, sq_sz))



    #use offset to center the ball in its square
    ball_offset = (sq_sz - ball.get_width()) // 2

    all_sprites = []    # keep a list of all sprites in the game

    # create a sprite object for each queen, populate our list
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball, (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
        all_sprites.append(a_queen)

    all_sprites.append(duke1)
    all_sprites.append(duke2)

    while True:

        #look for events
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:    # on Escape key
                break
            if key == ord("r"):
                colors[0] = (255, 0, 0) # red + black
            if key == ord("g"):
                colors[0] = (0, 255, 0) # green + black
            if key == ord("b"):
                colors[0] = (0, 0, 255) # blue + black
        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict["pos"]
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

        # ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()

        # draw a fresh background - blank chess board
        for row in range(n):    # draw row on a board
            c_indx = row % 2    # alternate starting color
            for col in range(n):
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # ask every sprite to draw itself
        for sprite in all_sprites:
            sprite.draw(surface)


        my_clock.tick(60)   # keep frame rate at 60

##        # now that the squares are drawn, draw the queens.
##        for (col, row) in enumerate(the_board):
##            surface.blit(ball, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])