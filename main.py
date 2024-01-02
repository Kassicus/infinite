# python module imports
import pygame

# project file imports
import lib
import debug

pygame.init() # initialize the pygame module

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption(lib.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get() # initializing the lib.events list (NONE at start)

        self.debug_interface = debug.DebugInterface()

    def run(self):
        while self.running:
            self.single_events()
            self.multi_events()
            self.draw()
            self.update()

    def single_events(self):
        lib.events = pygame.event.get() # refresh events list

        for event in lib.events:
            # special events
            if event.type == pygame.QUIT:
                self.running = False

            # get all keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def multi_events(self):
        pass

    def draw(self):
        self.screen.fill(lib.color.BLACK)

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self):
        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.framerate) / 1000


# run the game
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit() # clean up pygame background processes
