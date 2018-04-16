from gamelib import*

game=Game(800,600,"pokemon go")
bk = Image("forest.jpg",game)
bk.resizeTo(800,600)
game.setBackground(bk)


title = Image("pokemon_go_logo.png",game)
title.y -= 120
title.resizeBy(-40)
gun = Sound("shots.wav",1)
winner = Sound("winner.wav",2)
howtoplay = Image("arrowkey.png",game)
howtoplay.resizeBy(-40)
howtoplay.y += 100
shot = Image("space.jpg",game)
shot.resizeBy(-40)
shot.y +=200

win = Image("youwin.png",game)
windfire =Image("windfire.png",game)
windfire.resizeTo(700,400)

smuggler=Image("smuggler.png",game)
smuggler.resizeTo(250,300)
smuggler.moveTo(200,400)

monster=Image("dragon.png",game)
monster.resizeTo(300,300)
monster.moveTo(600,400)

bullet=Image("bullet.png",game)
bullet.resizeTo(20,15)
#bullet.moveTo(270,305)
monster2=Image("oldest.png",game)
monster2.resizeTo(350,350)
monster2.moveTo(600,400)

fire = []
for index in range(50):
    fire.append( Image("fire.png",game))
for index in range(50):

    fire[index].resizeTo(70,70)
    #fire[index].setSpeed(1, 90)
    fire[index].moveTo(monster.x,monster.y)
waterball = []
for index in range(50):
    waterball.append( Image("waterball.png",game))
for index in range(50):
    waterball[index].resizeTo(70,70)
    #fire[index].setSpeed(1, 90)
    waterball[index].moveTo(monster2.x,monster2.y)



#Title Screen
game.over = False
while not game.over:
    game.processInput()
    bk.draw()
    title.draw()
    howtoplay.draw()
    shot.draw()
    game.drawText("Click [SPACE] to Start",300,550)
    if shot.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)


#Level 1
game.over = False 

while not game.over:
    game.processInput()
    bk.draw()
    smuggler.draw()
    #fire.draw()
    monster.draw()
   
    bullet.move()
    
    item=Image("turtle.png",game)
    item.resizeTo(100,100)
    item.moveTo(700,500)
    item.draw()
    
#smuggler control

    if keys.Pressed[K_UP]:
        smuggler.y -= 4
    if keys.Pressed[K_DOWN]:
        smuggler.y += 4
    if keys.Pressed[K_RIGHT]:
        smuggler.x += 4
    if keys.Pressed[K_LEFT]:
        smuggler.x -= 4

    

    for index in range(1):
        fire[index].moveTowards(smuggler, 3)
        
        if fire[index].collidedWith(smuggler):
            fire[index].moveTo (monster.x, monster.y)
            smuggler.health -= 5
        if bullet.collidedWith(monster):
            bullet.visible = False
            monster.health -= 10
            
        
        if fire[index].collidedWith(bullet):
            fire[index].moveTo (monster.x, monster.y)
    if keys.Pressed[K_SPACE]:
        gun.play()
        bullet.moveTo(smuggler.x + 100,smuggler.y - 96)
        bullet.setSpeed(10,270)
        bullet.visible = True
        

    if smuggler.health < 1:
        game.over = True
    if monster.health < 1:
        game.over = True

    
    game.drawText("Level 1",50,50)


    game.drawText("Health: " + str(smuggler.health),smuggler.x - 35,smuggler.y -150)
    game.drawText("Health: " + str(monster.health),monster.x - 20,monster.y - 100)
    game.update(30)


#level 2
game.over = False
while not game.over and smuggler.health > 1:
    game.processInput()
    bk.draw()
    smuggler.draw()
    monster2.draw()
    bullet.move()
    item=Image("turtle.png",game)
    item.resizeTo(100,100)
    item.moveTo(600,550)
    item.draw()
   
    #smuggler control 

    if keys.Pressed[K_UP]:
        smuggler.y -= 4
    if keys.Pressed[K_DOWN]:
        smuggler.y += 4
    if keys.Pressed[K_RIGHT]:
        smuggler.x += 4
    if keys.Pressed[K_LEFT]:
        smuggler.x -= 4
    for index in range(2):
        y=randint(300,500)
        waterball[index].moveTowards(smuggler, 3)
        if waterball[index].collidedWith(smuggler):
            waterball[index].moveTo (monster2.x,y)
            smuggler.health -= 5
            
        if bullet.collidedWith(monster2):
            bullet.visible = False
            monster2.health -= 5
           
        if waterball[index].collidedWith(bullet):
            waterball[index].moveTo (monster2.x, monster2.y)
    if keys.Pressed[K_SPACE]:
        gun.play()
        bullet.moveTo(smuggler.x + 100,smuggler.y - 96)
        bullet.setSpeed(15,270)
        bullet.visible = True
        
    game.drawText("Level 2",50,50)


    game.drawText("Health: " + str(smuggler.health),smuggler.x - 35,smuggler.y -150)
    game.drawText("Health: " + str(monster2.health),monster2.x -50,monster2.y - 200)

    if smuggler.health < 1:
        game.over = True
    if monster2.health < 1:
        #game.over = True
        game.clearBackground(black)
        winner.play()
        win.draw()
        windfire.draw()
        windfire.moveTo(400,400)
   
    
    game.update(30)

#game over screen

game.quit()



