import sys, pygame
import random
import math
pygame.init()

screenW, screenH = 1024,768

screen = pygame.display.set_mode((screenW, screenH))
# pygame.draw.circle(screen,  (255, 100, 0), (100,100), 20)
# pygame.draw.aaline(screen, (255, 255, 255), (160, 100), p)
# screen.set_at((10, 10), (255,0,0))

class PLANETE:
    """ type: badguy, shy, random  """
    def __init__(self,posX,posY,planeteType,planeteRadius,distance=0,speed=0):
        self.posX = posX
        self.posY = posY
        self.planeteType = planeteType
        self.planeteRadius=planeteRadius
        self.distance=SUN.distanceSoleil(self,posX,posY)
        self.speed = self.distance/2000
        print("distance de la planete", self.distance)
        print("vitesse de la planete",self.speed)

    def spin(self,centerX,centerY,centerRadius,distanceFromSun,speed):

        planete.posX=centerX+ int(math.cos(speed)*(distanceFromSun))
        planete.posY=centerY+ int(math.sin(speed)*(distanceFromSun))
        print("la speed",self.speed)

    # def isRandom(self):
    #     return self.type == "random"

    # def color(self):
    #     if self.isRandom():
    #         return (0,255,0)
    #     else:
    #         return (100,100,100)




class SUN:
    def __init__(self,posX,posY,radius):
        self.posX=posX
        self.posY=posY
        self.radius=radius


    def distanceSoleil(self,x1,x2):
            d = math.sqrt (math.pow(theSun.posX-x1,2) + math.pow(theSun.posY-x2,2))
            # print("posX du sun",theSun.posX)
            # print("x1 de l'equation donc position X de planete",x1)
            print("distance",d/10)
            return d




speed=0
theSun = SUN(screenW/2,screenH/2,40)
planetes = [ PLANETE(80,80,"one",15,theSun),
             PLANETE(800,400,"one",15),
             PLANETE(200,200,"one",15),
             PLANETE(90,300,"one",15)]
# PLANETE(sun.posX+sun.rayon-50,sun.posY+sun.rayon+50,"one",15),
# PLANETE(sun.posX+sun.rayon-50,sun.posY+sun.rayon+50,"one",15)]


play = True
clock = pygame.time.Clock()
mouse = None
count = 0

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        if event.type == pygame.KEYUP:
            print(event.key, event.unicode, event.scancode)
            if event.key == pygame.K_ESCAPE:
                play = False

    screen.fill((0,0,0))

    #Draw a Sun
    pygame.draw.circle(screen,  (200, 180, 0), (theSun.posX,theSun.posY), theSun.radius)

    for planete in planetes :
        
        pygame.draw.circle(screen,  (0, 0, 255), (planete.posX,planete.posY), planete.planeteRadius )
        planete.spin(theSun.posX,theSun.posY,theSun.radius,planete.distance,speed)
    clock.tick(60)
    count += 1
    speed+=0.1
    # if planete.distance/10<30:
    #     speed += 0.2
    # if planete.distance/10<40:
    #     speed += 0.1
    pygame.display.flip()
