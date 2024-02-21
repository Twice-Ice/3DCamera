import pygame
from pygame import Vector2, Vector3
from globals import FPS, SCREEN_SIZE, X, Y
pygame.init()

clock = pygame.time.Clock()
doExit = False
screen = pygame.display.set_mode((SCREEN_SIZE))

object = [
    [Vector3(0, 0, 0), Vector3(100, 100, 100), Vector3(50, 25, 50)]
]

class Camera:
    def __init__(self, pos, moveSpeed = 10):
        self.pos = pos
        self.moveSpeed = moveSpeed
    
    def update(self, keys):
        if keys[pygame.K_w]:
            self.pos.y += self.moveSpeed
        if keys[pygame.K_s]:
            self.pos.y -= self.moveSpeed
        if keys[pygame.K_a]:
            self.pos.x += self.moveSpeed
        if keys[pygame.K_d]:
            self.pos.x -= self.moveSpeed

camera = Camera(Vector2(0, 0))

while not doExit:
    screen.fill((0, 0, 0))
    dt = clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            doExit = True
    
    for i in range(len(object)):
        p1 = object[i][0]# + camera.pos
        p2 = object[i][1]# + camera.pos
        p3 = object[i][2]# + camera.pos
        print(p1)
        pointSize = 2
        pygame.draw.polygon(screen, (155, 155, 155), (p1, p2, p3))
        pygame.draw.circle(screen, (255, 255, 255), p1, pointSize)
        pygame.draw.circle(screen, (255, 255, 255), p2, pointSize)
        pygame.draw.circle(screen, (255, 255, 255), p3, pointSize)

    keys = pygame.key.get_pressed()
    camera.update(keys)

    pygame.display.flip()
pygame.quit()