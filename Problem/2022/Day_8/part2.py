class Part_2:
    # from point x, y to which dir:direction
    def check(self, from_x, from_y, dir_x, dir_y):
        point = self.data[from_x][from_y]
        count = 0

        dir_name = ""
        # which direction
        if (dir_x == 0):
            if (dir_y == 1):
                dir_name = "RIGHT"
            else:
                dir_name = "LEFT"
        else:
            if (dir_x == 1):
                dir_name = "BOTTOM"
            else:
                dir_name = "UP"

        # does it work
        while (
            (from_x > 0 and from_x < self.col_len-1) and
            (from_y > 0 and from_y < self.row_len-1)
        ):
            from_x += dir_x
            from_y += dir_y

            count += 1

            if self.data[from_x][from_y] >= point:
                break

        print(f"{dir_name:6} = {count}")
        return count

    def __init__(self, data, row_len, col_len):
        self.data = data
        self.row_len = row_len
        self.col_len = col_len
        self.max_total = -1

        # out_side element ... no need for edge ... as it will be 0
        # in_side element
        for row_i in range(1, row_len-1):
            for col_j in range(1, col_len-1):
                print(f"\n{row_i}-{col_j}, {self.data[row_i][col_j]}")

                # bottom, up, left, right
                total = self.check(row_i, col_j, 1, 0) * \
                    self.check(row_i, col_j, -1, 0) * \
                    self.check(row_i, col_j, 0, -1) * \
                    self.check(row_i, col_j, 0, 1)

                print(f"        ({total})")

                if total > self.max_total:
                    self.max_total = total

        print(f"\n\n--- Part 2:- {self.max_total} ---")
