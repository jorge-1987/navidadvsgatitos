import pygame
import time
import random

#Definiciones globales
pygame.init()

#w = ancho
#h = alto

pantallaw = 1600
pantallah = 1000

#Colores
fondo = (50,50,50)
white = (255,255,255)
marco = (100,100,200)
gris = (40,39,39)
verde = (10,150,10)
agua = (100,100,230)

#Resources
#crocki = pygame.image.load('crockicrocki.png')
carta = pygame.image.load('carta.png')
arbolito = pygame.image.load('arbolito.png')
arbolitoroto = pygame.image.load('arbolitoroto.png')
regalo = pygame.image.load('regalo.png')
gato = pygame.image.load('gato.png')
pepino = pygame.image.load('pepino.png')

linea01 = [0,0,0,0,0,0,0,0]
linea02 = [0,0,0,0,0,0,0,0]
linea03 = [0,0,0,0,0,0,0,0]

areajuego = pygame.display.set_mode((pantallaw,pantallah))
pygame.display.set_caption('Arbolitos de navidad vs Gatitos!')

gametimer = pygame.time.Clock()

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largetext = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (x,y)
    areajuego.blit(TextSurf, TextRect)



def game_loop():
#Posiciones Iniciales
    jposx = 0
    jposy = 800

    arbolito01 = True
    arbolito02 = True
    arbolito03 = True


    oleadas = 10
    cartas = 0
    timer = 0
    selected = 0
    spawn = 1
    
    termino = False

    while not termino:
        #EVENTOS DEL TECLADO
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            termino = True
                        if event.key == pygame.K_LEFT:
                            if jposx <= 0:
                                jposx = 0
                            else:
                                jposx = jposx-200
                        elif event.key == pygame.K_RIGHT:
                            if jposx >= pantallaw-200:
                                jposx = pantallaw-200
                            else:
                                jposx = jposx+200
                        elif event.key == pygame.K_UP:
                            if jposy <= 0:
                                jposy = 0
                            else:
                                jposy = jposy-200
                        elif event.key == pygame.K_DOWN:
                            if jposy >= pantallah-200:
                                jposy = pantallah-200
                            else:
                                jposy = jposy+200
                        elif event.key == pygame.K_RETURN:
                            if selected == 0:
                                if jposy == 800:
                                    if jposx == 0:
                                        if cartas >= 100:
                                            cartas = cartas-100
                                            selected = 1
                                    elif jposx == 200:
                                        if cartas >= 200:
                                            cartas = cartas-200
                                            selected = 3
                            else:
                                if jposx >= 200: 
                                    if jposy == 200:
                                        if (jposx == 200) and linea01[0] == 0:
                                            linea01[0] = selected
                                            selected = 0
                                        elif (jposx == 400) and linea01[1] == 0:
                                            linea01[1] = selected
                                            selected = 0
                                        elif (jposx == 600) and linea01[2] == 0:
                                            linea01[2] = selected
                                            selected = 0
                                        elif (jposx == 800) and linea01[3] == 0:
                                            linea01[3] = selected
                                            selected = 0
                                        elif (jposx == 1000) and linea01[4] == 0:
                                            linea01[4] = selected
                                            selected = 0
                                        elif (jposx == 1200) and linea01[5] == 0:
                                            linea01[5] = selected
                                            selected = 0
                                        elif (jposx == 1400) and linea01[6] == 0:
                                            linea01[6] = selected
                                            selected = 0

                                    if jposy == 400:
                                        if (jposx == 200) and linea02[0] == 0:
                                            linea02[0] = selected
                                            selected = 0
                                        elif (jposx == 400) and linea02[1] == 0:
                                            linea02[1] = selected
                                            selected = 0
                                        elif (jposx == 600) and linea02[2] == 0:
                                            linea02[2] = selected
                                            selected = 0
                                        elif (jposx == 800) and linea02[3] == 0:
                                            linea02[3] = selected
                                            selected = 0
                                        elif (jposx == 1000) and linea02[4] == 0:
                                            linea02[4] = selected
                                            selected = 0
                                        elif (jposx == 1200) and linea02[5] == 0:
                                            linea02[5] = selected
                                            selected = 0
                                        elif (jposx == 1400) and linea02[6] == 0:
                                            linea02[6] = selected
                                            selected = 0

                                    if jposy == 600:
                                        if (jposx == 200) and linea03[0] == 0:
                                            linea03[0] = selected
                                            selected = 0
                                        elif (jposx == 400) and linea03[1] == 0:
                                            linea03[1] = selected
                                            selected = 0
                                        elif (jposx == 600) and linea03[2] == 0:
                                            linea03[2] = selected
                                            selected = 0
                                        elif (jposx == 800) and linea03[3] == 0:
                                            linea03[3] = selected
                                            selected = 0
                                        elif (jposx == 1000) and linea03[4] == 0:
                                            linea03[4] = selected
                                            selected = 0
                                        elif (jposx == 1200) and linea03[5] == 0:
                                            linea03[5] = selected
                                            selected = 0
                                        elif (jposx == 1400) and linea03[6] == 0:
                                            linea03[6] = selected
                                            selected = 0

                            

        #Conflictos
        if timer > 100:
            for i in range(8):
                #Linea de tablero 01
                if i == 0:
                    if linea01[i] == 9:
                        arbolito01 = False
                        linea01[i] = 0
                else:
                    if linea01[i] == 9:
                        if linea01[i-1] == 0:
                            linea01[i-1] = 9
                            linea01[i] = 0
                if linea01[i] == 1:
                    if linea01[i+1] == 9:
                        linea01[i] = 2
                else:
                    if linea01[i] == 2:
                        if linea01[i+1] == 9:
                            linea01[i] = 0
                if linea01[i] == 3:
                    if linea01[i+1] == 9:
                        linea01[i] = 4
                elif linea01[i] == 4:
                    if linea01[i+1] == 9:
                        linea01[i] = 0
                        linea01[i+1] = 0
                        oleadas = oleadas-1

                #Linea de tablero 02
                if i == 0:
                    if linea02[i] == 9:
                        arbolito02 = False
                        linea02[i] = 0
                else:
                    if linea02[i] == 9:
                        if linea02[i-1] == 0:
                            linea02[i-1] = 9
                            linea02[i] = 0

                if linea02[i] == 1:
                    if linea02[i+1] == 9:
                        linea02[i] = 2
                else:
                    if linea02[i] == 2:
                        if linea02[i+1] == 9:
                            linea02[i] = 0

                if linea02[i] == 3:
                    if linea02[i+1] == 9:
                        linea02[i] = 4
                elif linea02[i] == 4:
                    if linea02[i+1] == 9:
                        linea02[i] = 0
                        linea02[i+1] = 0
                        oleadas = oleadas-1

                #Linea de tablero 03
                if i == 0:
                    if linea03[i] == 9:
                        arbolito03 = False
                        linea03[i] = 0
                else:
                    if linea03[i] == 9:
                        if linea03[i-1] == 0:
                            linea03[i-1] = 9
                            linea03[i] = 0

                if linea03[i] == 1:
                    if linea03[i+1] == 9:
                        linea03[i] = 2
                else:
                    if linea03[i] == 2:
                        if linea03[i+1] == 9:
                            linea03[i] = 0

                if linea03[i] == 3:
                    if linea03[i+1] == 9:
                        linea03[i] = 4
                elif linea03[i] == 4:
                    if linea03[i+1] == 9:
                        linea03[i] = 0
                        linea03[i+1] = 0
                        oleadas = oleadas-1

            timer = 0
            spawn = spawn-1
        listachoice = [1,2,3]
        if not arbolito01:
            listachoice.remove(1)
        if not arbolito02:
            listachoice.remove(2)
        if not arbolito03:
            listachoice.remove(3)

        if (spawn == 0) and (len(listachoice) > 0):
            lista = random.choice(listachoice)

            if lista == 1:
                if linea01[7] == 0:
                    linea01[7] = 9
            elif lista == 2:
                if linea02[7] == 0:
                    linea02[7] = 9
            elif lista == 3:
                if linea03[7] == 0:
                    linea03[7] = 9

            spawn = random.randrange(1, 6, 1)


        



        #PINTAR FONDO
        areajuego.fill(fondo)
        #PINTAR Marco y cosas fijas
        #Marco
        pygame.draw.rect(areajuego, marco, [0, 0, pantallaw, 200])
        pygame.draw.rect(areajuego, marco, [0, 800, pantallaw, 200])
        #Jugador
        pygame.draw.rect(areajuego, verde, [jposx, jposy, 200, 200])
        #Pintar seleccion
        if selected == 1:
            pygame.draw.rect(areajuego, verde, [0, 800, 200, 200])
        elif selected == 3:
            pygame.draw.rect(areajuego, verde, [200, 800, 200, 200])

        message_display(str(cartas),300,100)


        message_display("Oleada restantes: "+str(oleadas),1300,900)

        for i in range(7):
            xo = 0
            if i == 0:
                xo = 200
            elif i == 1:
                xo = 400
            elif i == 2:
                xo = 600
            elif i == 3:
                xo = 800
            elif i == 4:
                xo = 1000
            elif i == 5:
                xo = 1200
            elif i == 6:
                xo = 1400
            
            if linea01[i] == 9:
                areajuego.blit(gato,(xo,200))
            if linea01[i] == 1:
                areajuego.blit(regalo,(xo,200))
            if linea01[i] == 2:
                areajuego.blit(regalo,(xo,200))
            if linea01[i] == 3:
                areajuego.blit(pepino,(xo,200))
            if linea01[i] == 4:
                areajuego.blit(pepino,(xo,200))

            if linea02[i] == 9:
                areajuego.blit(gato,(xo,400))
            if linea02[i] == 1:
                areajuego.blit(regalo,(xo,400))
            if linea02[i] == 2:
                areajuego.blit(regalo,(xo,400))
            if linea02[i] == 3:
                areajuego.blit(pepino,(xo,400))
            if linea02[i] == 4:
                areajuego.blit(pepino,(xo,400))

            if linea03[i] == 9:
                areajuego.blit(gato,(xo,600))
            if linea03[i] == 1:
                areajuego.blit(regalo,(xo,600))
            if linea03[i] == 2:
                areajuego.blit(regalo,(xo,600))
            if linea03[i] == 3:
                areajuego.blit(pepino,(xo,600))
            if linea03[i] == 4:
                areajuego.blit(pepino,(xo,600))


        areajuego.blit(carta,(0,0))

        if arbolito01:
            areajuego.blit(arbolito,(0,200))
        else:
            areajuego.blit(arbolitoroto,(0,200))
        if arbolito02:
            areajuego.blit(arbolito,(0,400))
        else:
            areajuego.blit(arbolitoroto,(0,400))
        if arbolito03:
            areajuego.blit(arbolito,(0,600))
        else:
            areajuego.blit(arbolitoroto,(0,600))

        areajuego.blit(regalo,(0,800))
        areajuego.blit(pepino,(200,800))
        message_display("100",150,950)
        message_display("200",350,950)



        #Mostrar todo
        pygame.display.update()
        gametimer.tick(10)
        cartas = cartas+1
        timer = timer+2

        haygatos = False

        for o in linea01:
            if o == 9:
                haygatos = True
        for o in linea02:
            if o == 9:
                haygatos = True
        for o in linea03:
            if o == 9:
                haygatos = True

        if oleadas == 0 and not haygatos:
            termino = True

        if arbolito01 == False and arbolito02 == False and arbolito03 == False:
            oleadas = 1000
            termino = True
        #print(timer)
        #print(selected)

    return oleadas


def main():
    #Cuerpo del programa que llama al juego
    areajuego.fill(fondo)
    score = game_loop()

    time.sleep(4)
    areajuego.fill(fondo)
    if score > 0:
        message_display("Gatitos que te ganaron: "+str(score),300,450)
    else:
        message_display("Tu arbol sobrevivio!!!",300,450)
    pygame.display.update()
    time.sleep(4)
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()