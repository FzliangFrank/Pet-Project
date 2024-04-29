import collections

ALIVE ="♥"
DEAD = "·"

class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )

        # create dictionary for counting the number of living neighbors
        # this is the same as {} turns out
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1
                # the resulting index is index of neighbors actual sells
                # this creats a directory of {(row, col): 1}
            # interpretate this as:
                # for each live cell, add ther neighbor to 1
                # if (row,col) is new then creates new value in the directory

        # After you complete this iteration each cell should be populated 
        # with numeric int value.
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells # & is set operatior, union
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells # - is set difference
        # infere self alive

        self.pattern.alive_cells = stay_alive | come_alive
        return self

    def as_string(self, bbox):
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n ".join(display)

    def __str__(self):
        '''Check if your code works as expected'''
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
    import collections

    

    
    