import os
import random
import pygame
my_clock = pygame.time.Clock()


class Card:

    # directory and list of files containing images of all cards
    my_dir = "C:\\Users\\T Kluczlowski\\Dropbox\PYTHON 3\\CHAPTER 17 PYGAME\\PNG-cards-1.3\\"
    file_list = [file for file in os.listdir(my_dir)]

    # getting a hand of 5 cards drawn
    rng = random.Random()
    rng.shuffle(file_list)
    hand_images = file_list[1:6]


    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn

    def update(self):
        (x, y) = self.posn
        y -= 1
        self.posn = (x, y)

    def draw(self, target_surface):
        patch_rect = (0, 0, self.image.get_width(), self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)

    def resize_sprite(self, x_coef, y_coef):
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(my_width * x_coef), int(my_height * y_coef)))

        return (my_width, my_height)

    def handle_click(self, new_ix):
        self.image = file_list[new_ix]


    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)




pygame.init()
colors = [(255, 0, 0), (0, 0, 0)]   # set up colors - red, black


# create the surface pf width, height and its window
resolution = pygame.display.Info()
surface = pygame.display.set_mode((resolution.current_w, resolution.current_h))





card_image = pygame.image.load


hand_cards = []    # keep a list of all sprites in the game


# create a sprite object for each card, populate our list
for i in range(0, 5):

    card = Card(card_image(Card.my_dir + Card.hand_images[i]), (0, 0))
    card.resize_sprite(0.5, 0.5)
    # calculate gap between cards and sides of the screen in x axis
    gap = (resolution.current_w - 5 * card.image.get_width()) / 6
    card.posn = (gap + i * (gap + card.image.get_width()), 25)
    hand_cards.append(card)

card_swaps = 0
new_ix = 5


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
        for card in hand_cards:
            if card.contains_point(posn_of_click):
                card_swaps += 1
                if card_swaps < 3:
                    while card.posn[1] > -370:
                        card.update()
                        card.draw(surface)
                        pygame.display.flip()
                    new_ix += 1
                    card.image = card_image(Card.my_dir + Card.file_list[new_ix])
                    card.resize_sprite(0.5, 0.5)
                break

    surface.fill(colors[0])

    # ask every card to update itself.
##    for card in hand_cards:
##        card.update()

    # ask every card to draw itself
    for card in hand_cards:
        card.draw(surface)

    my_clock.tick(60)   # keep frame rate at 60


    pygame.display.flip()

pygame.quit()
