import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=0

# Rectangle setup
rect_x, rect_y = 600, 340
rect_width, rect_height = 50,50
rect_speed = 300  # 10 pixels per second

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        rect_x -= rect_speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rect_x += rect_speed * dt
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        rect_y -= rect_speed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        rect_y += rect_speed * dt

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, (255,0,0), (int(rect_x), int(rect_y), rect_width, rect_height))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()