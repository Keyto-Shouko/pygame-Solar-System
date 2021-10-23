import sys, pygame
import random
import math
pygame.init()

screenW, screenH = 1920,1080

screen = pygame.display.set_mode((screenW, screenH))
# pygame.draw.circle(screen,  (255, 100, 0), (100,100), 20)
# pygame.draw.aaline(screen, (255, 255, 255), (160, 100), p)
# screen.set_at((10, 10), (255,0,0))

#Gravitational const
G = 20
GAME_SPEED = 1 # 1 for Real time speed but its too slow
FPS = 60
MAX_COLOR = 255

#-------------------------------external files/assets---------------------------------#
background = pygame.image.load("spaceBG.jpg")
background = pygame.transform.scale(background,(screenW,screenH))
sunIMG = pygame.image.load("sunBG.png")
sunScaleX = 100 #sun image width
sunScaleY = 100 #sun image lenght
sunIMG = pygame.transform.scale(sunIMG,(sunScaleX,sunScaleY))
music = pygame.mixer.music.load('5012-light-years-astra-lost-in-space.mp3')
pygame.mixer.music.play(-1)
volume = 0.2
pygame.mixer.music.set_volume(volume)
#--------------------------------------------------------------------------------------#

#-------------------------------------Classes------------------------------------------#
class PLANETE:
    def __init__(self,name,radius,distance,angle):
        self.name = name #name of planete
        self.radius = radius #radius of planete
        self.distance = distance #distance of planete : it's actually the x and y distance from the sun
        self.angle=angle #starting angle of the planete in the unit circle
        self.x = sun.posX + self.distance #position of X of the planet
        self.y = sun.posY + self.distance #position of Y of the planet
        # the distance from sun, wich correspond to the math formula of the distance between 2 points
        self.realDistance = distanceSoleil(self.x,self.y) 
        # print(self.name)
        # print("distance",self.distance)
        # print("x",self.x,"y",self.y)
        print("realDistance",self.name, self.realDistance)
        # print("-------------------")
        self.color = dynamicColor(self.realDistance) # color of planet
    
    #Function that make planetes spin arround the unit circle
    def spin(self,centerRotationX,centerRotationY,planeteAngle,planeteDistance):
            planete.x = (round((planeteDistance*math.cos(planeteAngle)) + centerRotationX, 2))
            planete.y = (round((planeteDistance*math.sin(planeteAngle)) + centerRotationY, 2))

    #Function that circle through the list of planetes, calc if your mose is in the "hitbox" of a planete and delete it
    def deletePlanete(self,mouseDistance):
        number = 0
        for onePlanet in planetes:
            number+=1
            # see if your mouse is in the hitbox
            if mouseDistance>=onePlanet.realDistance-onePlanet.radius and mouseDistance<= onePlanet.realDistance+onePlanet.radius: 
                del planetes[number-1]

    #Function that add a planet on click, with a fix name, fix radius, realDistance from the sun 
    #and the position where the planete would be in the "time of the solar system" (aka tick)
    def addPlanet(self,mouse,tick):
        if mouse/math.sqrt(2)<sun.radius:
            mouse =56 
        planetes.append(PLANETE("ajouté",8+random.random()*15,mouse/math.sqrt(2),tick))


class SUN:
    def __init__(self,posX,posY,radius,mass):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.mass = mass  
#--------------------------------------------------------------------------------------#


#------------------------Functions : period, distance from sun etc---------------------#

# Function to calc the period of rotation of the planete
def calcPeriod(radius, central_mass):
    period = (2 * math.pi * math.pow(radius, 3 / 2)) / math.pow(G * central_mass, 1 / 2)
    accelerationPeriod = period / GAME_SPEED
    # print("accelerationPeriod",accelerationPeriod)
    return round(accelerationPeriod, 2)

# Function to calc the angle modification per frame
def angleFrame(period):
    # print("period",period)
    # print("FPS",FPS)
    totalFrame = period * FPS
    # print("totalFrame",totalFrame)
    rpf = -1 * (2 * math.pi) / totalFrame
    return rpf # Radiant per frame

# Function to calculate the distance from a point to the sun
def distanceSoleil(x1,y1):
            d = math.sqrt (math.pow(sun.posX-x1,2) + math.pow(sun.posY-y1,2))
            # print("distance",d)
            return d

# Function to set a dynamic color, each planete has its own color where R decrease the further you are from the Sun
# and blue increases the further you are from the Sun
def dynamicColor(realDistance):
    if realDistance>255:
        realDistance=255
    r=int(255-realDistance)
    g=int(realDistance*0.05)
    b=int((255-r+sun.radius))

    #Check if one of the color composant is out of bound and set it to max
    if r>255 or r<0:
        r=MAX_COLOR
    if g>255 or g<0:
        g=MAX_COLOR
    if b>255 or b<0:
        b=MAX_COLOR
    color=(r,g,b)
    print("color",color)
    return color

def modifyVolume(volume):
        pygame.mixer.music.set_volume(volume)
        print("%.2f"%(pygame.mixer.music.get_volume()))
#--------------------------------------------------------------------------------------#

#-------------------------------------Instanciate objects------------------------------#
sun = SUN(screenW/2,screenH/2,40,20000) # instanciate the sun
             
planetes = [ PLANETE("Elona",8+random.random()*15,80,0), #instanciate planetes
             PLANETE("Earth",8+random.random()*15,40,0),
             PLANETE("Ascalon",8+random.random()*15,200,0)]
#--------------------------------------------------------------------------------------#

#------------------------------Instanciate usefull variables---------------------------#
play = True
clock = pygame.time.Clock()
mouse = None
nb=sys.getrefcount(planetes) # get the number of objects created in "planetes"
tick=0 #tick is the "solar system" time variable, wich will allow to place planetes with a different angle
# print(nb)
#--------------------------------------------------------------------------------------#

#------------------------------Game Loop : events etc----------------------------------#
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            x=event.pos[0] 
            y=event.pos[1]
            mouse = distanceSoleil(x,y)
            #print("distance souris au soleil",mouse)
        if event.type == pygame.KEYUP:
            # print(event.key, event.unicode, event.scancode)
            if event.key == pygame.K_ESCAPE:
                play = False
            if event.key == pygame.K_UP:
                volume+=0.05
                modifyVolume(volume)
            if event.key == pygame.K_DOWN:
                volume-=0.05
                modifyVolume(volume)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                planete.deletePlanete(mouse)
            if event.button==3:
                planete.addPlanet(mouse,tick)    

    screen.blit(background,(0,0))

    #Place the sun image on the screen
    screen.blit(sunIMG,(sun.posX-sunScaleX/2-1,sun.posY-sunScaleY/2))
#---------------------------------------------------------------------------------------#

#------------------------Loop in Objects, drawing, moving-------------------------------#
    for planete in planetes :  
        # Calculate period, angle and every physical things needed to move planetes
        planetePeriod = calcPeriod(planete.realDistance, sun.mass)
        planeteAngleFrame = angleFrame(planetePeriod)
        planete.angle = planete.angle + planeteAngleFrame
        planete.spin(sun.posX,sun.posY,planete.angle,planete.realDistance)

        # draw the orbit line of planetes
        sunOrbitX = sun.posX
        sunOrbitY = sun.posY

        # Draw the orbit line
        pygame.draw.circle(screen, (255,255,255), [sunOrbitX, sunOrbitY], planete.realDistance, width=1)

        #Draw planet
        pygame.draw.circle(screen,planete.color, (planete.x,planete.y), planete.radius )
#--------------------------------------------------------------------------------------#

#------------------------END OF GAME LOOP : refresh etc--------------------------------#
    clock.tick(FPS)
    tick=pygame.time.get_ticks() #get the actual time of the solar system
    pygame.display.flip()
#--------------------------------------------------------------------------------------#