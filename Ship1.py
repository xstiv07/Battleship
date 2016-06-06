from tkMessageBox import showerror
class ship(object):
#initializes player ships based on their types
    def __init__(self, shipType, x, y, vertical, v1):
        if shipType == "carrier":
            if vertical == False:
                if v1.trr[x][y]['bg'] == v1.trr[x + 1][y]['bg'] == v1.trr[x + 2][y]['bg'] == v1.trr[x + 3][y]['bg'] == v1.trr[x + 4][y]['bg'] == "white":
                    v1.trr[x + 4][y]['bg'] = v1.trr[x + 3][y]['bg'] = v1.trr[x + 2][y]['bg'] = v1.trr[x + 1][y]['bg'] = v1.trr[x][y]['bg'] = 'green'
                    pp = v1._shipList.index("Carrier")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(5):
                        v1._carrier1.append((x + i, y))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')     
                
            if vertical == True:
                if v1.trr[x][y]['bg'] == v1.trr[x][y + 1]['bg'] == v1.trr[x][y + 2]['bg'] == v1.trr[x][y + 3]['bg'] == v1.trr[x][y + 4]['bg'] == "white":
                    v1.trr[x][y + 4]['bg'] = v1.trr[x][y + 3]['bg'] = v1.trr[x][y + 2]['bg'] = v1.trr[x][y + 1]['bg'] = v1.trr[x][y]['bg'] = 'green'
                    pp = v1._shipList.index("Carrier")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(5):
                        v1._carrier1.append((x, y + i))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                    
        if shipType == "battleship":
            if vertical == False:
                if v1.trr[x][y]['bg'] == v1.trr[x + 1][y]['bg'] == v1.trr[x + 2][y]['bg'] == v1.trr[x + 3][y]['bg'] == "white":
                    v1.trr[x + 3][y]['bg'] = v1.trr[x + 2][y]['bg'] = v1.trr[x + 1][y]['bg'] = v1.trr[x][y]['bg'] = 'yellow'
                    pp = v1._shipList.index("Battleship")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(4):
                        v1._battleship1.append((x + i, y))      
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                
            if vertical == True: 
                if v1.trr[x][y]['bg'] == v1.trr[x][y + 1]['bg'] == v1.trr[x][y + 2]['bg'] == v1.trr[x][y + 3]['bg'] == "white":
                    v1.trr[x][y + 3]['bg'] = v1.trr[x][y + 2]['bg'] = v1.trr[x][y + 1]['bg'] = v1.trr[x][y]['bg'] = 'yellow'
                    pp = v1._shipList.index("Battleship")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(4):
                        v1._battleship1.append((x, y + i))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                    
        if shipType == "cruiser":
            if vertical == False:
                if v1.trr[x][y]['bg'] == v1.trr[x + 1][y]['bg'] == v1.trr[x + 2][y]['bg'] == "white":
                    v1.trr[x + 2][y]['bg'] = v1.trr[x + 1][y]['bg'] = v1.trr[x][y]['bg'] = 'blue'
                    pp = v1._shipList.index("Cruiser")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(3):
                        v1._cruiser1.append((x + i, y))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                
            if vertical == True: 
                if v1.trr[x][y]['bg'] == v1.trr[x][y + 1]['bg'] == v1.trr[x][y + 2]['bg'] == "white":
                    v1.trr[x][y + 2]['bg'] = v1.trr[x][y + 1]['bg'] = v1.trr[x][y]['bg'] = 'blue'
                    pp = v1._shipList.index("Cruiser")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(3):
                        v1._cruiser1.append((x, y + i))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                    
        if shipType == "submarine":
            if vertical == False:
                if v1.trr[x][y]['bg'] == v1.trr[x + 1][y]['bg'] == v1.trr[x + 2][y]['bg'] == "white":
                    v1.trr[x + 2][y]['bg'] = v1.trr[x + 1][y]['bg'] = v1.trr[x][y]['bg'] = 'brown'
                    pp = v1._shipList.index("Submarine")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(3):
                        v1._submarine1.append((x + i, y))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                
            if vertical == True: 
                if v1.trr[x][y]['bg'] == v1.trr[x][y + 1]['bg'] == v1.trr[x][y + 2]['bg'] == "white":
                    v1.trr[x][y + 2]['bg'] = v1.trr[x][y + 1]['bg'] = v1.trr[x][y]['bg'] = 'brown'
                    pp = v1._shipList.index("Submarine")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(3):
                        v1._submarine1.append((x, y + i))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
            
        if shipType == "destroyer":
            if vertical == False:
                if v1.trr[x][y]['bg'] == v1.trr[x + 1][y]['bg'] == "white":
                    v1.trr[x + 1][y]['bg'] = v1.trr[x][y]['bg'] = 'orange'
                    pp = v1._shipList.index("Destroyer")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(2):
                        v1._destroyer1.append((x + i, y))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
                
            if vertical == True:
                if v1.trr[x][y]['bg'] == v1.trr[x][y + 1]['bg'] == "white": 
                    v1.trr[x][y + 1]['bg'] = v1.trr[x][y]['bg'] ='orange'
                    pp = v1._shipList.index("Destroyer")
                    del v1._shipList[pp]
                    v1.updateList()
                    for i in xrange(2):
                        v1._destroyer1.append((x, y + i))
                else:
                    showerror(message = 'Error. Ships cannot be on top of each other. Please specify different parameters')
    