class Part_2:

    def change_current_crt_row(self, line_no, line):
        self.cycle += 1

        index = self.cycle % 40 - 1

        # for cycle = 40, 80, ...
        if index == -1:
            index = 39

        if self.sprite_position[index] == "#":
            self.current_crt[index] = "#"
        else:
            self.current_crt[index] = "."

        # print(
        #     f"No:{line_no}, i:{index:2}, cyc:{self.cycle:3}, '{line:8}', x:{self.x:2}, current_crt: '{''.join(self.current_crt)}', sprite_position: '{''.join(self.sprite_position)}'"
        # )

        if index == 39:
            self.list_of_current_crt.append(self.current_crt)
            self.current_crt = list("||||||||||||||||||||||||||||||||||||||||")

    def change_sprite_position(self, before, after, line_no):
        try:
            self.sprite_position[before] = '.'
            self.sprite_position[before - 1] = '.'
            self.sprite_position[before + 1] = '.'

            self.sprite_position[after - 1] = '#'
            self.sprite_position[after] = '#'
            self.sprite_position[after + 1] = '#'
        except:
            # many be here error can come because of index getting out side of arr
            # not in question not told what to do ...
            #
            # so we ignore it
            # because we can understand which CAPITAL LETTERS
            # are print ... excepting this some condition
            # print(before, after, line_no)
            pass

    def __init__(self, data):
        self.list_of_current_crt = list()

        self.sprite_position = list("###.....................................")
        self.current_crt = list("||||||||||||||||||||||||||||||||||||||||")

        self.data = data
        self.total = 0

        self.x = 1
        self.cycle = 0

        for line_no, line in enumerate(self.data, start=1):
            # calculate values for cycle and x
            if line == "noop":
                self.change_current_crt_row(line_no, line)
            else:
                value = int(line.split(" ")[1])

                # phase 1, for addx statement
                self.change_current_crt_row(line_no, line)

                # phase 2, for addx statement
                self.change_current_crt_row(line_no, line)
                self.change_sprite_position(self.x, self.x + value, line_no)
                self.x = self.x + value

        print(f"\n--- Part 2 ---\n")
        for line in self.list_of_current_crt:
            print("".join(line))

        print()
