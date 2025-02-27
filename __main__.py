from knight import Knight
from knight import consistent
from display import draw

def Backtracking(k):
    if len(k.path)==64:
        return k
    
    for e in range(1,9):
        
        if k.consistent(e):
            k.addMove(e)
            result=Backtracking(k)
            if result != None:
                return result
            k.removeMove()

def main ( ):
    knight = Knight()
    knight = Backtracking(knight)
    print (knight.assignment)
    print (knight.path)
    knight_position = (0, 0)
    draw(knight_position, knight.path)
    
if __name__ == "__main__":
    main()