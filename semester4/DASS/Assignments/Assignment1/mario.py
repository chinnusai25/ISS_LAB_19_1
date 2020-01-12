class Mario:
    
    def __init__(self,x,y,d):

        self.x=x
        self.y=y
        self.d=d
        self.__shape = "@"

    def start(self,grid):
        for i in range(25,28,1):    
            for j in range(0,3,1):    
                grid[i][j]=self.__shape

    def safety_check_at_right_move(self,grid):
        if (grid[self.x][self.y+1]=='|' or 
            grid[self.x][self.y+2]=='|' or
            grid[self.x][self.y+3]=='|' ):

            return 1
        else:
            return 0   

    def safety_check_at_left_move(self,grid):
        if (grid[self.x][self.y-1]=='|'):

            return 1
        else:
            return 0                  

    def safety_check_at_up_move(self,grid):
        if (grid[self.x-1][self.y]=='|' or 
            grid[self.x-1][self.y+1]=='|' or
            grid[self.x-1][self.y+2]=='|' ):
            return 1 
        else:
            return 0
    
    def safety_check_at_down_move(self,grid):
        if (grid[self.x+3][self.y]=='|' or 
            grid[self.x+3][self.y+1]=='|' or
            grid[self.x+3][self.y+2]=='|' ):
            return 1 
        else:
            return 0
    
    def need_to_be_updated(self,grid):
        for i in range(self.x,self.x+3,1):
            for j in range(self.y,self.y+3,1):
                grid[i][j]=" "

    def is_updated(self,grid):
        for i in range(self.x,self.x+3,1):    
            for j in range(self.y,self.y+3,1):    
                grid[i][j]=self.__shape
