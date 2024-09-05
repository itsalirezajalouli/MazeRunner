#   Maze runner with recursion by PU$HER
from termcolor import colored

#   Point abstract
class Point():
    def __init__(self, string: str, y: int, x:int) -> None:
        self.string = string
        self.y = y
        self.x = x

#   Maze as strings
MAZE = [
    ['#', '#', '#', '#', 'S', '#', 'E', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]


#   Start, end & directions
START = Point('S', 0, 4)
END = Point('E', 0, 7)
DIR = [
    [1, 0],
    [0, -1],
    [-1, 0],
    [0, 1]
]

def walk(maze: list[list[Point]], wall: str, curr: Point, end: Point, seen: list,
         path: list) -> bool:
    #   Base case 1: off the map
    if curr.x < 0 or curr.x >= len(maze[0]):
        return False
    if curr.y < 0 or curr.y >= len(maze):
        return False

    #   Base case 2: are we on a wall?
    if curr.string == wall:
        return False

    #   Base case 3: are we at the end?
    if curr.string == end.string:
        seen[curr.y][curr.x] = True
        path.append(curr)
        return True

    #   Base case 4: are we at a repetetive place?
    if seen[curr.y][curr.x]:
        return False

    #   Recursive case:
    #   Pre:
    seen[curr.y][curr.x] = True
    path.append(curr)

    #   Recurse in all four(len(DIR)) directions:
    for i in range(len(DIR)):
        [x, y] = DIR[i] 
        try:
            if walk(maze, wall, curr = maze[curr.y + y][curr.x + x], end = end, seen = seen, path = path):
                #   Stop recursing if found end
                return True
        except IndexError:
            return False

    #   Post
    path.pop()
    return False

def solve(maze: list, wall: str, start: Point, end: Point) -> list:
    seen = []
    path = []
    print(
        'Given Maze: ' + 'starts at (' + str(start.y) + ',' + str(start.x) + ') and ends in ('
        + str(end.y) + ',' + str(end.x - 1) + ').'
          )
    print(60 * '-')
    printer(maze, str = True)

    #   Convert string maze to a map of points 
    mazePoint = []
    for i in range(len(maze)):
        row = []
        for j in range(len(maze[0])):
            point = Point(maze[i][j], i, j)
            row.append(point)
        mazePoint.append(row)
    
    #   Make a full false list
    for i in range(len(maze)):
        fArray = []
        for j in range(len(maze[0])):
            fArray.append(False)
        seen.append(fArray)

    #   When we start our curr is start... Duuh!
    walk(mazePoint, wall, start, end, seen, path)
    
    print(60 * '-')
    print('Solved Mazed:')
    printer(seen, str = False)
    print(60 * '-')

    return path

#   Nerdy maze visualization
def printer(maze: list, str: bool):
    if str:
        for row in maze:
            for item in row:
                if item == ' ':
                    print(' ', end = '   ')
                elif item == 'S':
                    print(colored('S', 'blue'), end = '   ')
                elif item == 'E':
                    print(colored('E', 'blue'), end = '   ')
                else:
                    print(colored('\u2588', 'red'), end = '   ')
            print('\n')

    else:
        for row in maze: 
            for item in row:
                if item:
                    print(colored('\u2588', 'green'), end = '   ')
                else:
                    print(colored('\u2588', 'red'), end = '   ')
            print('\n')

solvedPath = solve(MAZE, '#', START, END)

#   Nerdy path visualization

cords = []
for i in solvedPath:
    x, y = i.y, i.x
    cords.append([x, y])
print('Path:')
for c in cords:
    print(c, end = ' -> ')

