
class Board:
    
    def __init__(self,row,column):
        self.row=row
        self.column=column
        self.matrix=[]

    def createboard(self):
        for i in range (self.row):
            i=i
            self.new=[]
            for j in range(self.column):
                j=j
                self.new.append(" ")
            self.matrix.append(self.new)

    def printit(self,a):
        if a ==0:
            for i in range(self.row):
                for j in range(a,a+110):
                    print(self.matrix[i][j],end='')
                print()                
        # elif(a==444):
        #     for i in range(self.row):
        #         for j in range(self.column):
        #             print(self.matrix[i][j],end='')
        #         print()

        # else:
        #     for i in range(self.row):
        #         for j in range(a-55,a+55):
        #             print(self.matrix[i][j],end='')
        #         print()