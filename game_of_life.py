import time
import os
import random
import platform


class golBoard(object):
    """
    NOT COMPLETE!
    An introduction to python using the game of life as a problem to solve in class.
    Not the most pythonic or succinct solution, but it's not meant to be.
    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by over-population.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    def __init__(self,rows=20,cols=20,populate=False,Density=.25):
        random.seed(556897)
        self.width = cols
        self.height = rows

        if populate:
            self.currentGen = self.initRandGen(Density)
        else:
            self.currentGen = self.initGen()

    def __str__(self):
        return "width:%d height:%d" % (self.width,self.height)      

        

    def makeAlive(self,row,col):
        """
        @function: makeAlive
        @description: Adds a life to specified location 
        @param: int x - Column to add life
        @param: int y - Row to add life
        @returns: None
        """ 
        self.currentGen[row-1][col-1] = True

        
       
    def computeNextGen(self):
        """
        @function: computeNextGen
        @description: Computes the next generation our cellular automata 
        @param: None
        @returns: None
        """     
        nextGen = self.initGen()
        for row in range(self.height):
            for col in range(self.width):
                nextGen[row][col] = self.liveOrDie(row,col)
        self.currentGen = nextGen

        

    def liveOrDie(self,r,c):
        """
        @function: liveOrDie
        @description: Calculates whether a cell lives or dies based on Game of Life rules
        @param: int x - Column to check
        @param: int y - Row to check
        @returns: Int : 0 = nothing changes , -1 = dies , 1 = birth
        """    
        neighbors = 0
        alive=self.currentGen[r][c]
        r1=r
        c1=c
        #Nested loop will loop around currentGen[r][c]
        for r in range (-1,2):
            for c in range (-1,2):
                # checkCell = (r1,c1)
                if r1+r>=0 and r1+r<self.height:#check to see if cell is on board
                    if c1+c>=0 and c1+c<self.width:#if so, safe to evaluate
                    
                    #check if current cell as alive
                        if(alive):
                            if(self.currentGen[r1-1][c1-1]==alive): #checks upper left neighbor
                                neighbors+=1
                            if(self.currentGen[r1-1][c1]==alive): #checks upper mid neighbor
                                neighbors+=1
                            if(self.currentGen[r1-1][c1+1]==alive): #checks upper right neighbor
                                neighbors+=1
                            if(self.currentGen[r1][c1-1]==alive): #checks mid left neighbor
                                neighbors+=1
                            if(self.currentGen[r1][c1+1]==alive): #checks right left neighbor
                                neighbors+=1
                            if(self.currentGen[r1+1][c1-1]==alive): #checks lower left neighbor
                                neighbors+=1
                            if(self.currentGen[r1+1][c1]==alive): #checks lower mid neighbor
                                neighbors+=1
                            if(self.currentGen[r1+1][c1+1]==alive): #checks lower right neighbor
                                neighbors+=1
                                
                        if(neighbors==2 or neighbors==3):
                            return 1
                        elif(neighbors<2 or neighbors>3):
                            return -1
                        else:
                            return 0
                else:
                    print("Off the world")
                    
                    
       
        
        
        """
        if(self.currentGen[r1-1][c1-1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#upper left
            neighbors.append(self.currentGen[r1-1][c1-1])
            nbcount+=1
            
        if(self.currentGen[r1-1][c1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#upper mid
            neighbors.append(self.currentGen[r1-1][c1])
            nbcount+=1
            
        if(self.currentGen[r1-1][c1+1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#upper right
            neighbors.append(self.currentGen[r1-1][c1+1])
            nbcount+=1
            
        if(self.currentGen[r1][c1-1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#mid left
            neighbors.append(self.currentGen[r1-1][c1-1])
            nbcount+=1
            
        if(self.currentGen[r1-1][c1+1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#mid right
            neighbors.append(self.currentGen[r1-1][c1-1])
            nbcount+=1
            
        if(self.currentGen[r1+1][c1-1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#lower left
            neighbors.append(self.currentGen[r1+1][c1-1])
            nbcount+=1
            
        if(self.currentGen[r1+1][c1-1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#lower mid
            neighbors.append(self.currentGen[r1+1][c1-1])
            nbcount+=1
            
        if(self.currentGen[r1+1][c1+1]==1 and((r1-1)>=0 and (r1+1)<self.width) and ((c1-1)>=0 and (c1+1)<self.height)):#lower right
            neighbors.append(self.currentGen[r1+1][c1+1])
            nbcount+=1
        """
        
        #alive = self.currentGen[r][c]
        #print(self.getNeighborWindow(r,c))
 
    def getNeighborWindow(self,r,c):
        """
        @function: liveOrDie
        @description: Calculates whether a cell lives or dies based on Game of Life rules
        @param: int x - Column to check
        @param: int y - Row to check
        @returns: Int : 0 = nothing changes , -1 = dies , 1 = birth
        """     
        neighbors = []
        srow = r - 1
        scol = c - 1

        if srow  < 0:
            srow = 0

        if scol < 0:
            scol = 0

        erow = r + 1
        ecol = c + 1

        if erow >= self.height:
            erow = self.height - 1

        if (ecol + 1) >= self.width:
            ecol = self.width

        for i in range(srow,erow+1):
            for j in range(scol,ecol+1):
                if i == r and j == c:
                    continue
                neighbors.append((i,j))

        return neighbors            
                      
                    
        
    def initGen(self):
        """
        @function: initGen
        @description: Initializes a single generation 
        @param: None
        @returns: list - 2D list containing False
        """     
        #return [[False] * self.width for row in range(self.height)]
        
        board = [i for i in range(self.height)]
        for i in range(self.height):
            board[i] = [0 for j in range(self.width)]
        return board      
    
    
       
    def initRandGen(self,density):
        """
        @function: initRandGen
        @description: Initializes a random generation 
        @param: float - density (how many lives to create)
        @returns: list - 2D list containing False and True
        """     
        gen = self.initGen()
        
        numberOfLives = int(self.width * self.height * density)
        
        for i in range(numberOfLives):
                row = random.randint(0, self.height-1)
                col = random.randint(0, self.width-1)
                gen[row][col] = self.randomLife()       # ??
        return gen
        

    def randomLife(self):
        """
        @function: randomLife
        @description: Generates a random life (zero or one)
        @param: none
        @returns: bool - zero or one (alive or dead)
        """    
        if random.random() > .5:
            x = True
        else:
            x = False
        return x


    def stringifyWorld(self):
        """
        @function: stringifyWorld
        @description: Creates a string version of the 2D list representing our world
        @param: none
        @returns: string - a string version 
        """    
        count = 0
        format = ';'.join([str(0), str(32), str(40)])
        string = "\n\n"
        string += '  '
        for i in range(self.width):
            string += ' '+str(i%10)
        string += "\n"
        for row in self.currentGen:
            string += str(count % 10)+' '
            count += 1
            for cell in row:
                if cell == False:
                    string += '\x1b[%sm%s\x1b[0m' % (format,' .')
                else:
                    string += ' x'
            string += "\n"
        return string
        

    def printColoredSection(self,x,y):
        """
        @function: printColoredSection
        @description: Prints a colored portion of the world
        @param: none
        @returns: none
        """
        
        clearScreen()
        format = ';'.join([str(0), str(32), str(40)])
        count = 0
        string = "\n\n"
        string += '  '
        for i in range(self.width):
            string += ' '+str(i%10)
        string += "\n"
        for row in self.currentGen:
            string += str(count % 10)+' '
            count += 1
            for cell in row:
                if cell == False:
                    string += '\x1b[%sm%s\x1b[0m' % (format,' .')
                else:
                    string += ' x'
            string += "\n"
        print(string)      
        
        
    def printDebug(self):
        for row in self.currentGen:  
            print(row)
              

def clearScreen():
    """
    @function: clearScreen
    @description: Clears the terminal screen
    @param: None
    @returns: None 
    """
    if platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def printList(mylist):
    string = ""
    for rows in range(len(mylist)):
        for cols in range(len(mylist)):
            string += "%d " % (mylist[rows][cols])
        string+= "\n"
    print (string)
    
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in xrange(8):
        for fg in xrange(30,38):
            s1 = ''
            for bg in xrange(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print (s1)
        print ('\n')
    
    def genericprint():
        for i in range(self.height):
            for j in range(self.width):
                print (self.currentGen[i][j])


rows = 10
cols = 10
generations = 30
density = .25
sleep = .05


b = golBoard(rows,cols,True,density)
print(b.stringifyWorld())
b.liveOrDie(8,6)
