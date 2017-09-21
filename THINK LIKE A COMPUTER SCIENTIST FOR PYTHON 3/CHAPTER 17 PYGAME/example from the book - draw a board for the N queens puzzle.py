import pygame, time

def main():
    """ Set up the game and run the main game loop """
    pygame.init()       # prepare pygame module for use

    #create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((1000, 700))

    # load image to draw. Substitute your own.
    # pygame accepts gif, jpg, png, etc. image types
    ball = pygame.image.load("ball2.jpg")

    # create a font for rendering text
    my_font = pygame.font.SysFont('Courier', 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:
        ev = pygame.event.poll()    #  look for any event
        if ev.type == pygame.QUIT:  #  WINDOW close button cliked?
            break                   #  leave game loop

        # logic goes here

        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1 - t0)
            t0 = t1


        # completely redraw te surface starting with the background
        main_surface.fill((0, 200, 255))

        # overpaint a red rectangle on the main surface
        main_surface.fill((255, 0, 0), (300, 100, 150, 90))

        # copy our image to the surface, at (x, y )
        main_surface.blit(ball, (100, 120))

        #make a new surface with an image of the text
        the_text = my_font.render('Frame = {0}, rate = {1:.2f} fps'.format(frame_count, frame_rate), True, (0, 0, 0))

        #copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # now the surface is ready, tell pygame module to dislay it!
        pygame.display.flip()

    pygame.quit()   # once we leave the loop, close the window.


main()
