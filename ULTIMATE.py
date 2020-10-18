#Ashley
#player:
#direction/ pick up/ drop off/ 
#customer
from cmu_112_graphics import *
from tkinter import *
from PIL import Image
import random
import copy

#MAKERS
class Aliens(object):
    def __init__(self, alienNum, x, y, mode):
        self.mode = mode
        self.alienNum = alienNum
        self.spriteList = []
        for i in range (1,7):
            pngFile = Image.open(f'worker{i}.png')
            self.spriteList.append(pngFile)
        self.sprite = self.spriteList[self.alienNum-1]
        self.sprite = mode.scaleImage(self.sprite,1/2)
        self.x = x
        self.y = y

    def drawAlienWorker(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.sprite))
        



class Player(object):
    def __init__(self, playerNum, xPos,yPos,mode):
        self.mode = mode
        self.playerNum = playerNum
        self.spriteList = []
        for i in range (1,5):
            pngFile = Image.open(f'player{i}.png')
            self.spriteList.append(pngFile)
        sprite = self.spriteList[self.playerNum-1]
        self.sprite = mode.scaleImage(sprite,1/2)
        self.score = 0
        self.orderList = ['wheels', 'fuel tank True', 'engine', 'control panel', 'shell']
        self.holding = []
        self.x = xPos
        self.y = yPos
        self.charW = 8
        self.charH = 10
        #self.items = set([Wheel,Engine,ControlPanel,Shell,FuelTank])
        table = Table()
        self.tables = table.allTables
        self.lastKey = ''
    def drawPlayers(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.sprite))

    def move(self,event):
        if (event.key == 'Right'):
            self.x += 10
            if self.x >= self.mode.width:
                self.x -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x -= 10
            self.lastKey = 'Right'
            
        elif (event.key == 'Left'):
            self.x -= 10
            if self.x <= 0:
                self.x += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x += 10
            self.lastKey = 'Left'
            
        elif (event.key == 'Up'):
            self.y -= 10
            if self.y <= 0:
                self.y += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y += 10
            self.lastKey = 'Up'
                    
        elif (event.key == 'Down'):
            self.y += 10
            if self.y >= self.mode.height:
                self.y -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y -= 10
            self.lastKey = 'Down'

    def movePlayer2(self,event):
        if (event.key == 'd'):
            self.x += 10
            if self.x >= self.mode.width:
                self.x -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x -= 10
            self.lastKey = 'd'
            
        elif (event.key == 'a'):
            self.x -= 10
            if self.x <= 0:
                self.x += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x += 10
            self.lastKey = 'a'
            
        elif (event.key == 'w'):
            self.y -= 10
            if self.y <= 0:
                self.y += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y += 10
            self.lastKey = 'w'
                    
        elif (event.key == 's'):
            self.y += 10
            if self.y >= self.mode.height:
                self.y -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y -= 10
            self.lastKey = 's'

    def movePlayer3(self,event):
        if (event.key == 'n'):
            self.x += 10
            if self.x >= self.mode.width:
                self.x -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x -= 10
            self.lastKey = 'n'
            
        elif (event.key == 'v'):
            self.x -= 10
            if self.x <= 0:
                self.x += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x += 10
            self.lastKey = 'v'
            
        elif (event.key == 'g'):
            self.y -= 10
            if self.y <= 0:
                self.y += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y += 10
            self.lastKey = 'g'
                    
        elif (event.key == 'b'):
            self.y += 10
            if self.y >= self.mode.height:
                self.y -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y -= 10
            self.lastKey = 'b'

    def movePlayer4(self,event):
        if (event.key == 'l'):
            self.x += 10
            if self.x >= self.mode.width:
                self.x -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x -= 10
            self.lastKey = ''
            
        elif (event.key == 'j'):
            self.x -= 10
            if self.x <= 0:
                self.x += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.x += 10
            self.lastKey = ''
            
        elif (event.key == 'i'):
            self.y -= 10
            if self.y <= 0:
                self.y += 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y += 10
            self.lastKey = 'i'
                    
        elif (event.key == 'k'):
            self.y += 10
            if self.y >= self.mode.height:
                self.y -= 10
            for table in self.tables:
                if Player.isColliding(self,table):
                    self.y -= 10
            self.lastKey = 'k'

            
    def isColliding(self, table):
        a = self.x - self.charW
        b = self.x + self.charW
        c = self.y - self.charH
        d = self.y + self.charH
        #collide bottom right
        if (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        #collide top right
        elif (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        #collide bottom left
        elif (b >= (table.x - table.wid) and\
            a <= (table.x - table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        #collide top left
        elif (b >= (table.x - table.wid) and\
            a <= (table.x - table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        #collide top
        elif (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        #collide bottom
        elif (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        #collide left
        elif(a <= (table.x - table.wid) and\
            b >= (table.x - table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        #collide right
        elif (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        else:
            return False
            
    def tableInFront(self,table):
        a = self.x - self.charW
        b = self.x + self.charW
        c = self.y - self.charH
        d = self.y + self.charH
        
        if self.lastKey == 'Right' and\
            (a <= (table.x + table.wid) and\
            b >= (table.x + table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        elif self.lastKey == 'Left' and\
            (a <= (table.x - table.wid) and\
            b >= (table.x - table.wid)) and\
            (c >= (table.y - table.hei) and\
            d <= (table.y + table.hei)):
            return True
        elif self.lastKey == 'Up' and\
            (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y + table.hei) and\
            d >= (table.y + table.hei)):
            return True
        elif self.lastKey == 'Down' and\
            (a >= (table.x - table.wid) and\
            b <= (table.x + table.wid)) and\
            (c <= (table.y - table.hei) and\
            d >= (table.y - table.hei)):
            return True
        return False

def pickDrop(player,event):
    for table in Table().allTables:
        if (event.key == 'd'):
            if Player.tableInFront(player,table) and\
                len(player.holding)>0 and (isinstance(table,ReceiveTable)):
                item = player.holding.pop
                if isinstance(table,MakerTable) and\
                    player.orderList[len(makerTable1.progress)]==str(item):
                    makerTable1.progress.append(item)
                    print("dropped")
                elif isinstance(table,MakerTable):
                    player.holding.append(item)
                    print("Can't drop here!")
                        
        elif (event.key == 'e'):
            if Player.tableInFront(player,table) and\
                (isinstance(table,PickupTable) and len(player.holding)<2):
                player.holding.append(table.item)
                print("picked up")


#Tables
class ReceiveTable(object):
    wid = 100
    hei = 80

class Trash(ReceiveTable):
    def __init__(self,xPos,yPos,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.x = xPos
        self.y = yPos
        image = Image.open('Trashcan.png')
        self.image = mode.scaleImage(image,1/3)
        
        
    def drawTrash(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class MakerTable(ReceiveTable):
    def __init__(self,xPos,yPos,mode):
        self.wid = super().wid
        self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.progress = []
        self.image = Image.open('makerTable.png')
        self.image = mode.scaleImage(self.image,1/3)
        
    def drawMakerTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class PickupTable(object):
    wid = 100
    hei = 50

class WheelTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,mode):
        if rotated:
            self.wid = super().hei
            self.hei = super().wid
        else:
            self.wid = super().wid
            self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.rotated = rotated
        self.item = Wheels(mode)
        image = Image.open('wheelTable.png')
        self.image = mode.scaleImage(image,1/3)
        if self.rotated:
            self.image = self.image.rotate(90)

    def __repr__(self):
        return 'WheelTable'

    def drawWheelTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

        
class FuelTankTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,mode):
        if rotated:
            self.wid = super().hei
            self.hei = super().wid
        else:
            self.wid = super().wid
            self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.rotated = rotated
        self.item = FuelTank(mode)
        image = Image.open('fuelTankTable.png')
        self.image = mode.scaleImage(image,1/3)
        if self.rotated:
            self.image = self.image.rotate(90)

    def __repr__(self):
        return 'FuelTank'

    def drawFuelTankTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

        
class EngineTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,mode):
        if rotated:
            self.wid = super().hei
            self.hei = super().wid
        else:
            self.wid = super().wid
            self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.rotated = rotated
        self.item = Engine(mode)
        image = Image.open('engineTable.png')
        self.image = mode.scaleImage(image,1/3)
        if self.rotated:
            self.image = self.image.rotate(90)

    def __repr__(self):
        return 'Engine'

    def drawEngineTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))
        
    
class ControlPanelTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,mode):
        if rotated:
            self.wid = super().hei
            self.hei = super().wid
        else:
            self.wid = super().wid
            self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.rotated = rotated
        self.item = ControlPanel(mode)
        image = Image.open('controlPanelTable.png')
        self.image = mode.scaleImage(image,1/3)
        if self.rotated:
            self.image = self.image.rotate(90)

    def __repr__(self):
        return 'ControlPanel'

    def drawControlPanelTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class ShellTable(PickupTable):
    def __init__(self,xPos,yPos,rotated,mode):
        if rotated:
            self.wid = super().hei
            self.hei = super().wid
        else:
            self.wid = super().wid
            self.hei = super().hei
        self.x = xPos
        self.y = yPos
        self.rotated = rotated
        self.item = Shell(mode)
        image = Image.open('shellTable.png')
        self.image = mode.scaleImage(image,1/3)
        if self.rotated:
            self.image = self.image.rotate(90)

    def __repr__(self):
        return 'Shell'

    def drawShellTable(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

class FuelStation(object):
    def __init__(self,xPos,yPos,mode):
        self.x = xPos
        self.y = yPos
        self.wid = 100
        self.hei = 80
        self.image = Image.open('fuelStation.png')
        self.image = mode.scaleImage(self.image,1/4)

    def drawFuelStation(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))


class ColorStation(object):
    def __init__(self,xPos,yPos,mode):
        self.x = xPos
        self.y = yPos
        self.wid = 100
        self.hei = 80
        self.image = Image.open('colorStation.png')
        self.image = mode.scaleImage(self.image,1/4)

    def drawColorStation(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

    def visitColorStation(self,player,event):
        if isinstance(player.holding[0],Shell) and player.holding[0].color == None:
            player.holding[0].selectColor('red')


class WireStation(object):
    def __init__(self,xPos,yPos,mode):
        self.x = xPos
        self.y = yPos
        self.wid = 100
        self.hei = 80
        self.image = Image.open('wireStation.png')
        self.image = mode.scaleImage(self.image,1/4)

    def drawWireStation(self,canvas):
        canvas.create_image(self.x,self.y,image=ImageTk.PhotoImage(self.image))

class Table(object):
    allTableTypes = set([WheelTable,FuelTankTable,EngineTable,
                                  ControlPanelTable,ShellTable,Trash,MakerTable])
    allTables = set()

    def addTable(self,table):
        Table.allTables.add(table)

    def __repr__(self):
        return Table.allTables

        

    


#MAKING
class Rocket(object):
    orderedItems = ['wheels', 'fuel tank True', 'engine', 'control panel', 'shell']
    def __init__(self, mode):
        self.mode = mode
        self.items = []

    def addItem(self, part):
        tempList = copy.copy(self.items)
        tempList.append(part)
        index = len(tempList) - 1
        if str(tempList[index]) == Rocket.orderedItems[index]:
            self.items.append(part)
            print('Part added!')
        else:
            if 'False' in  str(tempList[index]):
                print('You need to do something to this item!')
            else:
                print(f'You can not add that, you need {Rocket.orderedItems[index]}')

    def checkAssembly(self):
        tempList = []
        for item in self.items:
            tempList.append(str(item))
        return Rocket.orderedItems ==  tempList     

    def draw(self, canvas):
        assembled = checkAssembly()
        if assembled == True:
            #draw the assembled rocket
            pass
        else:
            #draw the semi-assembled robot
            pass 
        pass

class Wheels(object):
    def __init__(self, mode):
        self.mode = mode
        pass
    def __repr__(self):
        return 'wheels'
    def draw(self, canvas):
        pass

class FuelTank(object):
    def __init__(self,mode):
        self.mode = mode
        self.tankFilled = False
        pass
    def __repr__(self):
        return f'fuel tank {self.tankFilled}'
    def fillTank(self):
        if self.tankFilled == False:
            self.tankFilled = True
        else:
            print('You already filled this tank')
    def draw(self, canvas):
        pass
class Engine(object):
    def __init__(self, mode):
        self.mode = mode
        #self.engineNum = engineNum
        self.shape = None

    def selectShape(self, shape):
        self.shape = shape

    def draw(self, event):
        if self.shape == 'triangle':
            #draw a triangle
            pass
        elif self.shape == 'circle':
            #draw a circle
            pass
        elif self.shape == 'square':
            #draw a square
            pass


class ControlPanel(object):
    def __init__(self, mode):
        self.mode = mode
        self.wired = False
    def wire(self):
        if self.wired == False:
            print('wired!')
            self.wired = True
        else:
            print("I'm already wired")

class Shell(object):
    def __init__(self, mode):
        self.mode = mode
        self.color = None
    def selectColor(self, color):
        self.color = color
    def draw(self, canvas):
        pass

    
#other helper fx:
#from http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#cachingPhotoImages
#CachingPhotoImage for increased speed section   
def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def getCachedPhotoImage(image):
    if ('cachedPhotoImage' not in image.__dict__):
        image.cachedPhotoImage = ImageTk.PhotoImage(image)
    return image.cachedPhotoImage

# from www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
def getCellBounds(mode, row, col):
    gridWidth  = mode.width - 2*mode.margin
    gridHeight = mode.height - 2*mode.margin
    columnWidth = gridWidth / mode.cols
    rowHeight = gridHeight / mode.rows
    x0 = mode.margin + col * columnWidth
    x1 = mode.margin + (col+1) * columnWidth
    y0 = mode.margin + row * rowHeight
    y1 = mode.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)


#ModalApp
class SplashScreenMode(Mode):
    def redrawAll(mode,canvas):
        mode.splashScreen = Image.open('splashScreen.png')
        canvas.create_image(mode.width/2,mode.height/2,image=ImageTk.PhotoImage(mode.splashScreen))
        
    #for now keyPressed, but should change to mouse Press or sth
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class GameMode(Mode):
    def appStarted(mode):
        mode.numbers = []
        for i in range(0,10):
            mode.numbers.append(Image.open(f'{i}.png'))
        mode.counter = 0
        mode.timer = 200
        mode.margin = 5
        PickupTable()
        #floor
        mode.rows,mode.cols = 15,22
        mode.floor = make2dList(mode.rows,mode.cols)
        tile = Image.open('tile.png')
        mode.tile = mode.scaleImage(tile,1/4)

        for row in range(mode.rows):
            for col in range(mode.cols):
                mode.floor[row][col] = mode.tile
        
        #aliens
        mode.alien1 = Aliens(1,90,700,mode)
        mode.alien2 = Aliens(2,400,80,mode)
        mode.alien3 = Aliens(3,800,80,mode)
        mode.alien4 = Aliens(4,1200,300,mode)
        mode.alien5 = Aliens(5,1200,700,mode)
        
        #tables
        mode.wheelTable = WheelTable(400,160,False,mode)
        Table.addTable(Table,mode.wheelTable)
        mode.controlPanelTable = ControlPanelTable(180,710,True,mode)
        Table.addTable(Table,mode.controlPanelTable)
        mode.fuelTankTable = FuelTankTable(1120,700,True,mode)
        Table.addTable(Table,mode.fuelTankTable)
        mode.engineTable = EngineTable(800,160,False,mode)
        Table.addTable(Table,mode.engineTable)
        mode.shellTable = ShellTable(1120,300,True,mode)
        Table.addTable(Table,mode.shellTable)
        

        mode.trash1 = Trash(350,800,mode)
        Table.addTable(Table,mode.trash1)
        mode.trash2 = Trash(980,800,mode)
        Table.addTable(Table,mode.trash2)

        mode.fuelStation = FuelStation(500,800,mode)
        Table.addTable(Table,mode.fuelStation)
            
        mode.colorStation = ColorStation(670,800,mode)
        Table.addTable(Table,mode.colorStation)
        
        mode.wireStation = WireStation(840,800,mode)
        Table.addTable(Table,mode.wireStation)
        
        mode.makerTable1 = MakerTable(560,405,mode)
        Table.addTable(Table,mode.makerTable1)
        mode.makerTable2 = MakerTable(740,405,mode)
        Table.addTable(Table,mode.makerTable2)
        mode.makerTable3 = MakerTable(560,515,mode)
        Table.addTable(Table,mode.makerTable3)
        mode.makerTable4 = MakerTable(740,515,mode)
        Table.addTable(Table,mode.makerTable4)

        #players
        mode.player1 = Player(1,560,300,mode)
        mode.player2 = Player(2,740,300,mode)
        mode.player3 = Player(3,560,600,mode)
        mode.player4 = Player(4,740,600,mode)

        #Order sheet
        mode.order = Image.open('orderSheet.png')

        mode.order1 = mode.scaleImage(Image.open('oneWheel.png'),1/4)
        
        mode.order2 = mode.scaleImage(Image.open('twoFuelTank.png'),1/4)
        mode.order3 = mode.scaleImage(Image.open('threeEngine.png'),1/4)
        mode.order4 = mode.scaleImage(Image.open('fourControlPanel.png'),1/4)
        mode.order5 = mode.scaleImage(Image.open('fiveShell.png'),1/4)
        
        #score sheet
        mode.score = Image.open('scoreSheet.png')
        mode.score = mode.scaleImage(mode.score,1/2)
        
    def timerFired(mode):
        mode.counter += 1
        if mode.counter % 10 == 0:
            mode.timer -= 1
            if mode.timer == 0:
                mode.app.setActiveMode(mode.app.gameOverMode)

    def drawScore(mode,canvas):
        a = mode.player1.score
        canvas.create_image(120,460,\
                    image=ImageTk.PhotoImage(mode.scaleImage(mode.numbers[a],1/3)))
        canvas.create_image(150,460,\
                    image=ImageTk.PhotoImage(mode.scaleImage(mode.numbers[0],1/3)))
        canvas.create_image(180,460,\
                    image=ImageTk.PhotoImage(mode.scaleImage(mode.numbers[0],1/3)))


    def drawTimer(mode,canvas):
        a = mode.timer//100
        if a == 0:
            a = 0
        b = mode.timer%100//10
        if b == 0 and a == 0:
            b = 0
        c = mode.timer%10
        canvas.create_image(mode.width-120,70,\
                            image=ImageTk.PhotoImage(mode.numbers[a]))
        canvas.create_image(mode.width-80,70,\
                            image=ImageTk.PhotoImage(mode.numbers[b]))
        canvas.create_image(mode.width-40,70,\
                            image=ImageTk.PhotoImage(mode.numbers[c]))
        
        pass
        
        
    def keyPressed(mode,event):
        Player.move(mode.player1,event)
        pickDrop(mode.player1,event)
        Player.movePlayer2(mode.player2,event)
        Player.movePlayer3(mode.player3,event)
        Player.movePlayer4(mode.player4,event)
        

    def redrawAll(mode,canvas):
        #floor
        for row in range(mode.rows):
            for col in range(mode.cols):
                (x0, y0, x1, y1) = getCellBounds(mode,row, col)
                cx, cy = (x0 + x1)/2, (y0 + y1)/2
                tile = mode.floor[row][col]
                photoImage = getCachedPhotoImage(tile)
                canvas.create_image(cx,cy,image=photoImage)
        
        #workers
        mode.alien1.drawAlienWorker(canvas)
        mode.alien2.drawAlienWorker(canvas)
        mode.alien3.drawAlienWorker(canvas)
        mode.alien4.drawAlienWorker(canvas)
        mode.alien5.drawAlienWorker(canvas)

        #tables
        mode.wheelTable.drawWheelTable(canvas)
        mode.controlPanelTable.drawControlPanelTable(canvas)
        mode.fuelTankTable.drawFuelTankTable(canvas)
        mode.shellTable.drawShellTable(canvas)
        mode.engineTable.drawEngineTable(canvas)

        mode.trash1.drawTrash(canvas)
        mode.trash2.drawTrash(canvas)

        mode.fuelStation.drawFuelStation(canvas)

        mode.colorStation.drawColorStation(canvas)

        mode.wireStation.drawWireStation(canvas)

        mode.makerTable1.drawMakerTable(canvas)
        mode.makerTable2.drawMakerTable(canvas)
        mode.makerTable3.drawMakerTable(canvas)
        mode.makerTable4.drawMakerTable(canvas)
        
        
        
        #players
        mode.player1.drawPlayers(canvas)
        mode.player2.drawPlayers(canvas)
        mode.player3.drawPlayers(canvas)
        mode.player4.drawPlayers(canvas)

        #timer
        mode.drawTimer(canvas)

        #order sheet
        canvas.create_image(160,200,image=ImageTk.PhotoImage(mode.order))
        canvas.create_image(175,140,image=ImageTk.PhotoImage(mode.order1))
        canvas.create_image(165,170,image=ImageTk.PhotoImage(mode.order2))
        canvas.create_image(175,230,image=ImageTk.PhotoImage(mode.order3))
        '''
        canvas.create_image(540,400,image=ImageTk.PhotoImage(mode.order1))
        canvas.create_image(580,405,image=ImageTk.PhotoImage(mode.order2))
        canvas.create_image(620,395,image=ImageTk.PhotoImage(mode.order3))

        canvas.create_image(800,400,image=ImageTk.PhotoImage(mode.order1))
        canvas.create_image(780,405,image=ImageTk.PhotoImage(mode.order2))
        canvas.create_image(830,395,image=ImageTk.PhotoImage(mode.order3))
        canvas.create_image(750,415,image=ImageTk.PhotoImage(mode.order4))

        canvas.create_image(540,500,image=ImageTk.PhotoImage(mode.order1))
        canvas.create_image(580,520,image=ImageTk.PhotoImage(mode.order2))

        canvas.create_image(770,540,image=ImageTk.PhotoImage(mode.order1))
        canvas.create_image(790,520,image=ImageTk.PhotoImage(mode.order2))
    '''    
        canvas.create_image(130,270,image=ImageTk.PhotoImage(mode.order4))
        canvas.create_image(130,330,image=ImageTk.PhotoImage(mode.order5))

        
        #score sheet
        canvas.create_image(130,440,image=ImageTk.PhotoImage(mode.score))
        #score
        mode.drawScore(canvas)

class GameOverMode(Mode):
    def appStarted(mode):
        mode.scores = [mode.player1.score,mode.player2.score,mode.player3.score,mode.player4.score]
        mode.maxScore = max(mode.scores)
        mode.winner = mode.scores.index(mode.maxScore)+1
        
        
    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,image=ImageTk.PhotoImage(f'player{mode.winner}win.png'))
    
class CookingRocket(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.gameOverMode = GameOverMode()
        app.setActiveMode(app.splashScreenMode)
        

CookingRocket(width=1320,height=870)
