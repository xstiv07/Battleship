#! /usr/bin/env python

from Tkinter import *
from tkMessageBox import showerror, showinfo
from Ship1 import ship
from oppShip import oppShip
from random import randint
from ImageTk import *

class gui(Frame):
#Main class which controls everything in the program and manipulates all other classes.
    def __init__(self): 
        Frame.__init__(self, background = 'white') # initializing
        root = self.master #shortcut
        root.title("Battleship")
        self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (self.w, self.h)) #setting up height and width of the window
        menubar = Menu(self.master) # setting up a menuBar
        root.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New Game", command=self.__init__, underline = 0)
        fileMenu.add_command(label="Exit", command=self.quit, underline = 0)
        fileMenu.add_separator()
        menubar.add_cascade(label = "File", menu = fileMenu, underline = 0)
        helpMenu = Menu(menubar)
        helpMenu.add_command(label="About...", command=self.showHelp, underline = 0)
        menubar.add_cascade(label="Help", menu = helpMenu, underline = 0)
        self.grid(sticky = W+E+N+S)
        self.master.rowconfigure(0, weight = 1) #setting up columns rows
        self.master.columnconfigure(0, weight = 1)
        self.configFrame(3, 6)
        
        self._x = StringVar() #the value of rows in a SPINBOX widget
        self._y = StringVar() #the value of columns in a SPINBOX widget
        self._vertical = BooleanVar() #to see whether the CHECKBOX is marked or not
        
        #each list contains the coordinates of the computer's ships. Used to check if the game is over and 
        #to trigger the yellow/red background on the ship pictures.
        self._carrier = []; self._battleship = []; self._cruiser = []; self._submarine = []; self._destroyer = []
        
        #each list contains the coordinates of the player's ships. Used to check if the game is over
        self._carrier1 = []; self._battleship1 = []; self._cruiser1 = []; self._submarine1 = []; self._destroyer1 = []
        
        self._shipList = ["Battleship", "Cruiser", "Submarine", "Carrier", "Destroyer"] #names for navigation menu in LISTBOX
        self._opponentShipList = ("oppCarrier", "oppBattleship", "oppCruiser", "oppSubmarine", "oppDestroyer") #tuple to identify the computer ships

        self._noSimilar = [] # to avoid shooting at the same cell more than once
        self.ships = StringVar(value = tuple(self._shipList)) #controls LISTBOX content
        
        self.trr = [[]for f in xrange(10)] # double matrix for player's field
        self._opponent = [[]for f in xrange(10)] #Invisible double matrix for the opponent's field. 
        self._opponentVis = [[]for f in xrange(10)] #Visible double matrix for the opponnent's field.
        
        self._label = Label(self, text = "Welcome!  It's Battleship Time!",font = ("SketchFlow Print", '22'), background = 'white')
        self._label.grid(row=0, column = 1, sticky = 'N')
        self._textLabel = Label(self, text = 'Carrier - 5 cells\nBattleship - 4 cells\nCruiser - 3 cells\nSubmarine - 3 cells\
        \nDestroyer - 2 cells', bg = 'white', font = ("SketchFlow Print", '12'))
        self._textLabel.grid(row=0, column = 1, sticky = 'S')
        
        self.setPlayer1Field()#setting up the PLAYER'S FIELD
        self.setNavMenu() #setting up the NAVIGATION MENU
        self.setCompInvField() #Setting up an INVISIBLE COMPUTER'S FIELD
        self.setCompVisField() #Setting up a VISIBLE COMPUTER'S FIELD
        
    def setCompVisField(self):
    #Setting up a VISIBLE COMPUTER'S FIELD
        self._field4 = Frame(self, bg = "pink", bd = 5)
        for t in xrange(9, -1, -1):
            for r in xrange(10):
                self.listb2 = Button(self._field4,  bg = 'white', height = 2, width = 5, state = "disabled", relief ='ridge', \
                                             command = lambda i = t, j = r: self.shoot(i, j)) #workaround to pass any arguments from a command
                self._opponentVis[t].append(self.listb2)
                self.listb2.grid(row = r, column = t)
        self._field4.grid(row = 2, column = 2, sticky = "N", rowspan = 2)
        
    def setCompInvField(self):
    #Setting up an INVISIBLE COMPUTER'S FIELD
        self._field3 = Frame(self)
        for t in xrange(9, -1, -1):
            for r in xrange(10):
                self.listb1 = Button(self._field3, bg = 'white', height = 2, width = 5)
                self._opponent[t].append(self.listb1)
                self.listb1.grid(row = r, column = t)
                
    def setPlayer1Field(self):
    #setting up the PLAYER'S FIELD
        self._field1 = Frame(self, bg = "pink", bd = 5,)
        for j in xrange(10):
            for k in xrange(10):
                po = ord(str(k)) + 17 #using ASCII table to show Letters
                self.listb = Button(self._field1, relief ='ridge', height = 2, width = 5, state = 'disabled', bg = 'white')
                self.labelll = Label(self._field1, text = (chr(po), j+1), font = ("Times New Roman", '7'), bg = 'white')
                self.trr[j].append(self.listb)
                self.listb.grid(row = k, column = j)
                self.labelll.grid(row = k, column = j)
        self._field1.grid(row = 2, column = 0, sticky = "N", rowspan = 2)
        
    def setNavMenu(self):
    #setting up the NAVIGATION MENU
        self._field2 = Frame(self, relief = RIDGE, bd = 2, padx = 10, pady = 10)
        self.bb = Label(self._field2, text = "Set Up Your Ships", font = ("SketchFlow Print", '12', 'bold'))
        self.bb.grid(pady = 5, padx = 5)
        self.uu = Label(self._field2, text = "Row", font = ("SketchFlow Print", '10'))
        self.uu.grid(column = 0, row = 1, sticky = "W")
        self.xx = Spinbox(self._field2, values = ('A','B','C','D','E','F','G','H','I','J'), textvariable = self._y, width = 8, state = "readonly", )
        self.xx.grid(column = 0, row = 1, sticky = "E")
        self.bb = Label(self._field2, text = "Column", font = ("SketchFlow Print", '10'))
        self.bb.grid(column = 0, row = 2, sticky = "W")
        self.yy = Spinbox(self._field2, from_ = 1, to = 10, textvariable = self._x, width = 8, state = "readonly")
        self.yy.grid(column = 0, row = 2, sticky = "E")
        self.rr = Checkbutton(self._field2, text = "Vertical", variable = self._vertical, onvalue = True, offvalue = False, font = ("SketchFlow Print", '10'))
        self.rr.grid(sticky = "W", padx = 3, pady = 3)
        self.ll = Listbox(self._field2, height = 5, listvariable = self.ships, font = ("SketchFlow Print", '10'))
        self.ll.selection_set(0)
        self.ll.grid(sticky = "WE", padx = 3, pady = 3)
        for i in range(0,len(self._shipList),2):
            self.ll.itemconfigure(i, background='#f0f0ff')
        tmp = PhotoImage(file = 'add.png')
        self.hh = Button(self._field2, image = tmp, command = self.addToBoard, width = 100)
        self.hh.image = tmp
        self.hh.grid(padx = 3, pady = 3)
        self._field2.grid(row = 2, column = 1, sticky = "N")
    
    def addToBoard(self, *args):
    #Adds ships to the player's board based on the values of variables in the SPINBOXES
        try:
            valuex = int(self._x.get()) #getting a value of rows from the SPINBOX
            valuex -= 1 #to avoid off-by-one error
            valuey = ord(self._y.get()) - 65 #getting a value of columns from the SPINBOX
            
            valueVertical = self._vertical.get()
            aa = ‘,’.join(str(v) for v in self.ll.curselection())
            nowT = self.ll.get(aa) 
            try: #if the name is selected in the LISTBOX, it creates correspondent objects
                if 'Carrier' in nowT :
                    ship("carrier", valuex, valuey, valueVertical, self)
                if 'Battleship' in nowT:
                    ship("battleship", valuex, valuey, valueVertical, self)
                if 'Cruiser' in nowT:
                    ship("cruiser", valuex, valuey, valueVertical, self)
                if 'Submarine' in nowT:
                    ship("submarine", valuex, valuey, valueVertical, self)
                if 'Destroyer' in nowT:
                    ship("destroyer", valuex, valuey, valueVertical, self)
                if len(self._shipList) == 0: #if no more ships left in the LISTBOX
                    self.move() # we are done setting up our ships, we move on
            except IndexError:
                showerror(message = 'Error. You are out of the ocean. Please specify different parameters')
        except ValueError:
                pass
    
    def move(self):
    #Just a shortcut to organize all the other methods in an order.
        self._field2.grid_remove() #removes the navigation menu
        self.setControlPane() #creates a menu with pictures of opponent's ships
        self._label["text"] = "Game on. Shoot!!!"
        self.setOpponentShips() #opponent's ships are now set up
        self.enableButtons() # enabling buttons to SHOOT
    
    def setOpponentShips(self):
    #Initializes oppShip class and sets up the opponent's ships
        for i in xrange(5):
            oppShip(self._opponentShipList[i], self)
            
    def shoot(self, i, j):
    #Callback method. Used to shoot in a ship and automatically shoots player's ships.
        h = self._opponentVis[i][j]
        if self._opponent[i][j]['bg'] == 'white': #if the background of the INVISIBLE opponent FIELD == white
            h.configure(bg="pink", state = 'disabled') #that means a MISS in the VISIBLE field
        else:
            h.configure(state = 'disabled') #we can no longer press this button
            self.controlOverShips(self._carrier, i, j) #if the ship was hit we mark it its own list
            self.controlOverShips(self._battleship, i, j)
            self.controlOverShips(self._cruiser, i, j)
            self.controlOverShips(self._submarine, i, j)
            self.controlOverShips(self._destroyer, i, j)
            self.checkForPlayerHit(i, j, h) #checks whether the player's shot was a HIT or a MISS
        # if the computer HIT player's ship, this ship is DOOMED!    
        if len(self._carrier1) < 5 and len(self._carrier1) > 0:
            self.x = self._carrier1[-1][0] #last element's x 
            self.y = self._carrier1[-1][1] #last element's y
        elif len(self._battleship1) < 4 and len(self._battleship1) > 0:
            self.x = self._battleship1[-1][0]
            self.y = self._battleship1[-1][1] 
        elif len(self._cruiser1) < 3 and len(self._cruiser1) > 0:    
            self.x = self._cruiser1[-1][0]
            self.y = self._cruiser1[-1][1] 
        elif len(self._submarine1) < 3 and len(self._submarine1) > 0:    
            self.x = self._submarine1[-1][0]
            self.y = self._submarine1[-1][1]
        elif len(self._destroyer1) < 2 and len(self._destroyer1) > 0:    
            self.x = self._destroyer1[-1][0]
            self.y = self._destroyer1[-1][1]
        else:
            self.generateRandom() #generates 2 random numbers - x and y
            while (self.x, self.y) in self._noSimilar: #to avoid same x and y
                self.generateRandom()
            self._noSimilar.append((self.x, self.y))
                               
        if self.trr[self.x][self.y]['bg'] != 'white': # if the cell is not white => computer HIT the player's ship
            self.controlOverShips(self._carrier1, self.x, self.y) #if the ship was hit we mark it its own list
            self.controlOverShips(self._battleship1, self.x, self.y)
            self.controlOverShips(self._cruiser1, self.x, self.y)
            self.controlOverShips(self._submarine1, self.x, self.y)
            self.controlOverShips(self._destroyer1, self.x, self.y)
            self.trr[self.x][self.y]['bg'] = ['red']
        else:
            self.trr[self.x][self.y]['bg'] = ['pink'] #it was a MISS then
            
        if self.checkForWinner() == 1: #player got the WIN
            self.winnerGrid()
        elif self.checkForWinner() == 2: #player LOST
            self.looserGrid()

    def controlOverShips(self, thisShip, x, y):
    #If a ship was hit, removes the correspondent x and y from its list.
        if ((x, y)) in thisShip:
                thisShip.remove((x, y))
    
    def checkForWinner(self):
    #Checks for a winner.
        if len(self._carrier)== len(self._battleship) == len(self._cruiser) == len(self._submarine)==\
         len(self._destroyer) == 0:
            return 1
        if len(self._carrier1)== len(self._battleship1) == len(self._cruiser1) == len(self._submarine1)==\
         len(self._destroyer1) == 0:
            return 2
        else:
            return 3
    
    def checkForPlayerHit(self, i, j, h):
    #Checks whether the player hit a computer's ship
        if self._opponent[i][j]['bg'] == 'green': # if invisible field's background is green
            h.configure(bg="green") #we copy the background color to the VISIBLE field
            if len(self._carrier) == 0: #triggers background color of ships pictures
                self._fieldYY.pic['bg'] = 'red'
            if len(self._carrier) >= 2 and len(self._carrier) <= 5:
                self._fieldYY.pic['bg'] = 'yellow'
                    
        if self._opponent[i][j]['bg'] == 'blue':
            h.configure(bg="blue")
            if len(self._battleship) == 0:
                self._fieldYY.pic1['bg'] = 'red'
            if len(self._battleship) >= 2 and len(self._battleship) <= 5:
                self._fieldYY.pic1['bg'] = 'yellow'
                    
        if self._opponent[i][j]['bg'] == 'brown':
            h.configure(bg="brown")
            if len(self._cruiser) == 0:
                self._fieldYY.pic2['bg'] = 'red'
            if len(self._cruiser) >= 2 and len(self._cruiser) <= 5:
                self._fieldYY.pic2['bg'] = 'yellow'
                    
        if self._opponent[i][j]['bg'] == 'orange':
            h.configure(bg="orange")
            if len(self._submarine) == 0:
                self._fieldYY.pic3['bg'] = 'red'
            if len(self._submarine) >= 2 and len(self._submarine) <= 5:
                self._fieldYY.pic3['bg'] = 'yellow'
                    
        if self._opponent[i][j]['bg'] == 'black':
            h.configure(bg="black")
            if len(self._destroyer) == 0:
                self._fieldYY.pic4['bg'] = 'red'
            if len(self._destroyer) >= 2 and len(self._destroyer) <= 5:
                self._fieldYY.pic4['bg'] = 'yellow'
    
    def winnerGrid(self):
    #Draws a window if a PLAYER got a Win
        self.destroy()
        Frame.__init__(self, bg = '#7fc7ff')
        self.grid(sticky = W+E+N+S)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        
        self.configFrame(3, 3)
            
        self._field5 = Frame(self, bd = 5, bg = '#7fc7ff')
        self._lawr = PhotoImage(file = 'lawrence.png')
        self._field5.label55 = Label(self._field5, text = "Congratulations!\n James Lawrence is proud of you!!!", bg = '#7fc7ff', font = ("SketchFlow Print", '16'))
        self._field5.label66 = Label(self._field5, image = self._lawr,bg = '#7fc7ff')
        self._field5.butt55 = Button(self._field5, command = self.quit, text = 'QUIT', bg = '#7fc7ff', padx = 10, pady = 10)
        self._field5.butt66 = Button(self._field5, command = self.__init__, text = 'Play Again', bg = '#7fc7ff', padx = 10, pady = 10)
        self._field5.label55.grid(row = 0, column = 1, columnspan = 2, sticky = 'N')
        self._field5.label66.grid(row = 1, column = 1, columnspan = 2, sticky = 'N')
        self._field5.butt55.grid(row = 2, column = 1, sticky = 'S')
        self._field5.butt66.grid(row = 2, column = 2, sticky = 'S')
        self._field5.grid(row = 0, column = 1)
        
    def looserGrid(self):
    #Draws a window if a COMPUTER got a WIN
        self.destroy()
        Frame.__init__(self, bg = '#abcdef')
        self.grid(sticky = W+E+N+S)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        
        self.configFrame(3, 3)
            
        self._field5 = Frame(self, bd = 5, bg = '#abcdef')
        self._lawr = PhotoImage(file = 'wreckedship.png')
        self._field5.label55 = Label(self._field5, text = "This Battle is Lost....", bg = '#abcdef', font = ("SketchFlow Print", '16'))
        self._field5.label66 = Label(self._field5, image = self._lawr,bg = '#abcdef')
        self._field5.butt55 = Button(self._field5, command = self.quit, text = 'QUIT', bg = '#abcdef', padx = 10, pady = 10)
        self._field5.butt66 = Button(self._field5, command = self.__init__, text = 'Play Again', bg = '#abcdef', padx = 10, pady = 10)
        self._field5.label55.grid(row = 0, column = 1, columnspan = 2, sticky = 'N')
        self._field5.label66.grid(row = 1, column = 1, columnspan = 2, sticky = 'N')
        self._field5.butt55.grid(row = 2, column = 1, sticky = 'S')
        self._field5.butt66.grid(row = 2, column = 2, sticky = 'S')
        self._field5.grid(row = 0, column = 1)
            
    def generateRandom(self):
    #Generates two random numbers
        self.x = randint(0,9)
        self.y = randint(0,9)
        return self.x, self.y
    
    def configFrame(self, x, y):
    #Used to configure rows and columns
        for i in xrange(x):
            self.columnconfigure(i, weight = 1)
        for i in xrange(y):
            self.rowconfigure(i, weight = 1)

    def setControlPane(self):
    #Creates a menu with pictures of opponent's ships
        self._fieldYY = Frame(self, relief = RIDGE, bd = 2, padx = 10, pady = 10, background = 'white')
        self._shipLabel1 = Label(self._fieldYY, text = "Status of opponent's ships", background = 'white', font = ("SketchFlow Print", '12', 'bold'))
        self.setImages(self._fieldYY)
        self._shipLabel1.grid(row = 0, column = 0, sticky = "WE", pady = 5)
        self._fieldYY.grid(row = 2, column = 1, sticky = 'N')
        
    def setImages(self, v1):
    #Setting up pictures of the ships
        self._pic = PhotoImage(file = 'carrier.png')
        self._pic1 = PhotoImage(file = 'battleship.png')
        self._pic2 = PhotoImage(file = 'cruiser.png')
        self._pic3 = PhotoImage(file = 'submarine.png')
        self._pic4 = PhotoImage(file = 'destroyer.png')
        v1.pic = Label(v1, image = self._pic, background = 'white')
        v1.pic1 = Label(v1, image = self._pic1, background = 'white')
        v1.pic2 = Label(v1, image = self._pic2, background = 'white')
        v1.pic3 = Label(v1, image = self._pic3, background = 'white')
        v1.pic4 = Label(v1, image = self._pic4, background = 'white')
        v1.pic.grid(row = 1, column = 0)
        v1.pic1.grid(row = 2, column = 0)
        v1.pic2.grid(row = 3, column = 0)
        v1.pic3.grid(row = 4, column = 0)
        v1.pic4.grid(row = 5, column = 0)
        
    def updateList(self):
    #Updates a navigation menu, when the ship was added to the FIELD.
        self.ll.delete(0, END)
        for i in self._shipList:
            self.ll.insert(END, i)
        for i in range(0,len(self._shipList),2):
            self.ll.itemconfigure(i, background='#f0f0ff')
            
    def enableButtons(self):
    #Enables buttons to shoot.
        for i in xrange(10):
            for k in xrange(10):
                self._opponentVis[i][k]['state'] = 'normal'

    def showHelp(self):
        showinfo("About", "The game of Battleship is a classic board game.\nThe goal of the game is to sink the other player's ships before they sink your ships.\
        \nIt involves two players who have an 'ocean' laid out on a 10 X 10 grid, with columns labeled 1 - 10, and rows labeled A - J.\
        \nEach player takes turns shooting at the other side, trying to find and destroy the other player's five ships.\
        \nShips can only be put on the board vertically or horizontally (no diagonals).\
        \nShips cannot 'float off the board' and the whole ship must be in the 10 X 10 grid.\
        \nShips cannot be 'on top' of each other.\
        \nOnce the game starts, ships cannot be moved. ")
                                
def main():
    gui().mainloop()
    
if __name__ == "__main__":
    main()