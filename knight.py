import random

moves={
        1:(1,-2),
        2:(2,-1),
        3:(2,1),
        4:(1,2),
        5:(-1,2),
        6:(-2,1),
        7:(-2,-1),
        8:(-1,-2)
        }






class Knight:
    def __init__(self):
        self.position=(0,0)
        self.assignment=[]
        self.path=[self.position]

    def move_forward(self,direction):
        move=moves[direction]
        position=self.position
        self.position= (position[0]+move[0],position[1]+move[1])
        
    

    def move_backward(self):
        if len(self.path) > 1:
            self.path.pop()
            self.position = self.path[-1]

    def addMove(self,direction):
        self.assignment.append(direction)
        self.move_forward(direction)
        self.path.append(self.position)

    
    def removeMove(self):
        self.assignment.pop()
        self.move_backward()

    def consistent(self,m):
        move=moves[m]
        pos= self.position[0]+move[0],self.position[1]+move[1]

        if pos[0]<0 or pos[1]<0 or pos[0]>7 or pos[1]>7:
            return False
        

        elif self.path.count(pos)>0:
            return False
        else:
            return True





