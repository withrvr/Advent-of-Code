class Part_1:
    # from point x, y to which dir:direction
    def check(self, from_x, from_y, dir_x, dir_y):
        point = self.data[from_x][from_y]

        # does it work
        while (
            (from_x > 0 and from_x < self.col_len-1) and
            (from_y > 0 and from_y < self.row_len-1)
        ):
            from_x += dir_x
            from_y += dir_y

            # print(f"{from_x}-{from_y}, {self.data[from_x][from_y]}")
            # print(f"{self.data[from_x][from_y]}", end=",")

            if self.data[from_x][from_y] >= point:
                return False

        # which direction
        if (dir_x == 0):
            print("RIGHT") if (dir_y == 1) else print("LEFT")
        else:
            print("BOTTOM") if (dir_x == 1) else print("UP")

        return True

    def __init__(self, data, row_len, col_len):
        self.data = data
        self.row_len = row_len
        self.col_len = col_len

        self.total = 0
        self.out_side = (2 * row_len) + (2 * col_len) - 4
        self.in_side = 0

        # in_side element
        for row_i in range(1, row_len-1):
            for col_j in range(1, col_len-1):

                if (
                    self.check(row_i, col_j, 1, 0)  # bottom
                    or self.check(row_i, col_j, -1, 0)  # up
                    or self.check(row_i, col_j, 0, -1)  # left
                    or self.check(row_i, col_j, 0, 1)  # right
                ):
                    print(f"{row_i}-{col_j}, {self.data[row_i][col_j]}\n")
                    self.in_side += 1

        self.total = self.out_side + self.in_side
        print(
            f"--- Part 1: {self.out_side} + {self.in_side} = {self.total} ---")
