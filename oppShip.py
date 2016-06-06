from random import randint
class oppShip(object):
#initializes computer ships based on their types
    def __init__(self, shipT, v1):
        if shipT == "oppCarrier":
            self.vertical = randint(0, 1)
            if self.vertical == 0:
                x = 0
                y = randint(0,4)
                v1._opponent[x + 4][y]['bg'] = v1._opponent[x + 3][y]['bg'] = v1._opponent[x + 2][y]['bg'] = v1._opponent[x + 1][y]['bg'] =\
                 v1._opponent[x][y]['bg'] = 'green'
                for i in xrange(5):
                    v1._carrier.append((x + i, y))
                
            if self.vertical == 1:
                x = randint(0,4)
                y = 0
                v1._opponent[x][y + 4]['bg'] = v1._opponent[x][y + 3]['bg'] = v1._opponent[x][y + 2]['bg'] = v1._opponent[x][y + 1]['bg'] =\
                 v1._opponent[x][y]['bg'] = 'green'
                for i in xrange(5):
                    v1._carrier.append((x, y + i))
                
        if shipT == "oppBattleship":#correct
            self.vertical = randint(0, 1)
            if self.vertical == 0:
                x = randint(5,6)
                y = randint(0,4)
                v1._opponent[x + 3][y]['bg'] = v1._opponent[x + 2][y]['bg'] = v1._opponent[x + 1][y]['bg'] = v1._opponent[x][y]['bg'] = 'blue'
                for i in xrange(4):
                    v1._battleship.append((x + i, y))
                    
            if self.vertical == 1:
                x = randint(5,9)
                y = randint(0,1)
                v1._opponent[x][y + 3]['bg'] = v1._opponent[x][y + 2]['bg'] = v1._opponent[x][y + 1]['bg'] = v1._opponent[x][y]['bg'] = 'blue'
                for i in xrange(4):
                    v1._battleship.append((x, y + i))
                     
        if shipT == "oppCruiser": #correct
            self.vertical = randint(0, 1)
            if self.vertical == 0:
                x = randint(0,2)
                y = randint(5,9)
                v1._opponent[x + 2][y]['bg'] = v1._opponent[x + 1][y]['bg'] = v1._opponent[x][y]['bg'] = 'brown'
                for i in xrange(3):
                    v1._cruiser.append((x + i, y))
                
            if self.vertical == 1:
                x = randint(0,4)
                y = randint(5,7)
                v1._opponent[x][y + 2]['bg'] = v1._opponent[x][y + 1]['bg'] = v1._opponent[x][y]['bg'] = 'brown'
                for i in xrange(3):
                    v1._cruiser.append((x, y + i))
          
        if shipT == "oppSubmarine":#correct
            self.vertical = randint(0, 1)
            if self.vertical == 0:
                x = 7
                y = randint(5,9)
                v1._opponent[x + 2][y]['bg'] = v1._opponent[x + 1][y]['bg'] = v1._opponent[x][y]['bg'] = 'orange'
                for i in xrange(3):
                    v1._submarine.append((x + i, y))
             
            if self.vertical == 1:
                x = randint(7,9)
                y = randint(5,6)
                v1._opponent[x][y + 2]['bg'] = v1._opponent[x][y + 1]['bg'] = v1._opponent[x][y]['bg'] = 'orange'
                for i in xrange(3):
                    v1._submarine.append((x, y + i))
                    
        if shipT == "oppDestroyer":#correct
            self.vertical = randint(0, 1)
            if self.vertical == 0:
                x = 5
                y = randint(5,9)
                v1._opponent[x + 1][y]['bg'] = v1._opponent[x][y]['bg'] = 'black'
                for i in xrange(2):
                    v1._destroyer.append((x + i, y))
             
            if self.vertical == 1:
                x = randint(5,6)
                y = randint(5,8)
                v1._opponent[x][y + 1]['bg'] = v1._opponent[x][y]['bg'] = 'black'
                for i in xrange(2):
                    v1._destroyer.append((x, y + i))
    