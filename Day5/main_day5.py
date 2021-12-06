import numpy as np

class Grid:
    def __init__(self, diagonal=False):
        self.N = 1000
        self.grid_system = np.zeros( (self.N, self.N) )
        self.diagonal = diagonal
    
    def grid_point_counter(self, coordinates):
        """Creates horizontal and vertical lines"""
        x1, y1, x2, y2 = coordinates
        step_x, step_y = 1, 1
              
        # Vertical lines
        if x1 == x2:
            if y1 > y2:
                step_y *= -1
            for y in range(y1, y2 + step_y, step_y):
                self.grid_system[x1, y] += 1
            
        # Horizontal lines
        elif y1 == y2:
            if x1 > x2:
                step_x *= -1
            for x in range(x1, x2 + step_x, step_x):
                self.grid_system[x, y1] += 1 

        # Only for part 2, check if slope is 45deg
        elif self.diagonal:
            slope = abs((y2 - y1)/(x2 - x1))
            if np.arctan(slope) == np.pi / 4:  
                if x1 > x2:
                    step_x *= -1
                if y1 > y2:
                    step_y *= -1
                    
                for (a, b) in zip( range(x1, x2 + step_x, step_x), 
                                   range(y1, y2 + step_y, step_y) ):
                    self.grid_system[a, b] += 1
        
        else:
            print("No horizontal, vertical or diagonal lines")

    def total_points_above_threshold(self):
        """Makes a 1d array of the grid, and returns size of index array that satisfy the threshold."""
        array = np.ndarray.flatten(self.grid_system)
        check = np.array(np.where(array >= 2))
        return check.size
 
 
def coordinate_organizer(line):
    """Organizes a single line of the data file and returns a tuple.
    This tuple contains the intial and final coordinates."""
    xy1 = line.split("\n")[0].split(" -> ")[0]
    xy2 = line.split("\n")[0].split(" -> ")[1]
    x1, y1 = int(xy1.split(",")[0]), int(xy1.split(",")[1])
    x2, y2 = int(xy2.split(",")[0]), int(xy2.split(",")[1])
    
    return (x1, y1, x2, y2)

# Open data and put in list 
with open("Day5/data_day5.txt", "r") as file:
    data = [coordinate_organizer(line) for line in file.readlines()] 

# Use Grid() for part 1, use Grid(True) for part 2: to include diagonals             
new_grid = Grid(True)

for coordinate in data:
    new_grid.grid_point_counter(coordinate)

print(new_grid.total_points_above_threshold())
