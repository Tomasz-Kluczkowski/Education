import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()       # prepare pygame module for use
    surface_sz = 480    # physical surface size in pixels

    #create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    #set up some data to describe a small rectangle and its colors
    small_rect = (300, 200, 150, 90)
    some_color = (255,0,0) # color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    #  look for any event
        if ev.type == pygame.QUIT:  #  WINDOW close button cliked?
            break                   #  leave game loop

        # update game objects and data structures here
        # draw everything from scratch on each frame
        # so first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # now the surface is ready, tell pygame module to dislay it!
        pygame.display.flip()

    pygame.quit()   # once we leave the loop, close the window.


main()
