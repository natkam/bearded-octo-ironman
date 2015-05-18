''' 
Funkcja solve(tiles, start, end) znajduje najkrotsza droge do wyjscia.

Ta wersja uwzglednia, ze koniec/wyjscie ("end") moze byc na krawedzi labiryntu - jesli tak sie zdarzy, zmieniane sa jego wspolrzedne przekazywane do fcji solve(), tj. koniec jest "odsuwany" od krawedzi. To nie wplywa na to, co rysuje funkcja show().
Jesli w ogole nie da sie dojsc do punktu "end", nie jest on przesuwany.

Uwaga, korekta nie poradzi sobie z przypadkiem, gdy gdzies (poza koncem) nie bedzie sciany zewnetrznej. Zakladam, ze wyjatek "IndexError" pojawia sie tylko w zwiazku z punktem end. Jesli ogrodzenie labiryntu jest nieszczelne w innych miejscach, to czasem w ogole dzieje sie cos dziwnego...

'''
# uwaga, wspolrzedne x i y sa podawane w odwrotnej niz to ogolnie przyjete kolejnosci! (ale dobrze nazwane)

class Tile:
    def __init__(self, passable=False):
        self.passable = passable
        self.steps = float("inf")

    def __bool__(self):
        return self.passable


def create(f):
    start = None
    end = None
    tiles = [ [Tile()]*25 for i in range(25) ]

    for y, row in enumerate(f):
        for x, tile in enumerate(row.strip()):
            if tile in (' ', 'S', 'E'):
                tiles[y][x] = Tile(True)

            if tile == 'S':
                start = (y,x)
                tiles[y][x].steps = 0

            if tile == 'E':
                end = (y,x)
    return tiles, start, end


def show(tiles, start, end, solution):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if (y,x) == start:
                print("S", end='')
            elif (y,x) == end:
                print("E", end='')
            elif (y, x) in solution:
                print("+", end='')
            elif tile:
                print(" ", end='')
            else:
                print("#", end='')
        print()




def solve(tiles, start, end):
    y, x = start
    length = 0
    solution = []
    
    if (y, x) == (end):
        
        length = tiles[y][x].steps
        solution = [end]
        
        while tiles[y][x].steps != 0:
            if tiles[y+1][x].steps == (tiles[y][x].steps - 1):
                y, x = y+1, x
            elif tiles[y][x+1].steps == (tiles[y][x].steps - 1):
                y, x = y, x+1
            elif tiles[y-1][x].steps == (tiles[y][x].steps - 1):
                y, x = y-1, x
            elif tiles[y][x-1].steps == (tiles[y][x].steps - 1):
                y, x = y, x-1
            solution.append((y, x))
            
        return length, solution
        
    else:
        if tiles[y+1][x] and (tiles[y+1][x].steps > tiles[y][x].steps):
            tiles[y+1][x].steps = tiles[y][x].steps + 1
            length_tmp, solution_tmp = solve(tiles, (y+1, x), end)
            if length_tmp != 0:
                length = length_tmp
                solution = solution_tmp
        
        if tiles[y][x+1] and (tiles[y][x+1].steps > tiles[y][x].steps):
            tiles[y][x+1].steps = tiles[y][x].steps + 1
            length_tmp, solution_tmp = solve(tiles, (y, x+1), end)
            if length_tmp != 0:
                length = length_tmp
                solution = solution_tmp
        
        if tiles[y-1][x] and (tiles[y-1][x].steps > tiles[y][x].steps):
            tiles[y-1][x].steps = tiles[y][x].steps + 1
            length_tmp, solution_tmp = solve(tiles, (y-1, x), end)
            if length_tmp != 0:
                length = length_tmp
                solution = solution_tmp
            
        if tiles[y][x-1] and (tiles[y][x-1].steps > tiles[y][x].steps):
            tiles[y][x-1].steps = tiles[y][x].steps + 1
            length_tmp, solution_tmp = solve(tiles, (y, x-1), end)
            if length_tmp != 0:
                length = length_tmp
                solution = solution_tmp
        
        return length, solution


lab1 = open("l1.txt", "r")
tiles, start, end = create(lab1)

try:
    length, solution = solve(tiles, start, end)
except IndexError: # odsuwa end od brzegu - to nie wplywa na rozwiazanie rysowane przez show()
    new_end = [end[0], end[1]]
    
    if end[0]==0:
        new_end[0] = 1
    elif end[0]==24:
        new_end[0] = 23
        
    if end[1]==0:
        new_end[1] = 1
    elif end[1]==24:
        new_end[1] = 23
    
    new_end_tuple = (new_end[0], new_end[1])
    length, solution = solve(tiles, start, new_end_tuple)
    length += 1 # korekta "odsuniecia" punktu end od brzegu
    
if length==0:
    print("didn't manage to find the end, sorry")
else:
    print("the length of the path is %d steps" % length)

show(tiles, start, end, solution)