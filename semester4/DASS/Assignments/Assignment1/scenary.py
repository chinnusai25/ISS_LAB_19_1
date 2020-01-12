import random

class Scenary:
    
    def __init__(self):
        self.__sky = "X"
        self.__ground = "T"
        self.__beams = [('||'),('||'),('||'),('||'),('||')]

    def create_ground(self, grid):
        for i in range(500):
            grid[29][i]=self.__ground
            grid[28][i]="~"

    def create_sky(self, grid):
        for i in range(500):
            grid[0][i]=self.__sky

    def create_beams(self,grid,c,d):
        while(d<300):
            e=d
            f=c
            for i in range(5):
                for j in range(2):
                    grid[c][d]=self.__beams[i][j]
                    d+= len('|')
                d=e
                c+=1
            c=f
            d+=70 

      