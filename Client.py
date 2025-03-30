import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280 , 720
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Image Click Event")
clock = pygame.time.Clock()
running = True

image = pygame.transform.rotate(pygame.image.load("Dominoes\\0.5x\\0_0@0.5x.png"), 90)
image_rect = image.get_rect()

image_rect.centerx = SCREEN_WIDTH // 2
image_rect.bottom = SCREEN_HEIGHT

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if image_rect.collidepoint(event.pos):
                print("hello world")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screen.blit(image, image_rect)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()