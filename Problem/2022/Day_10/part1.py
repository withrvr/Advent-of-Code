class Part_1:

    def check_signal_strength(self, i, line):
        self.cycle += 1

        # print(f"i:{i:3}, '{line:8}' ---> x:{self.x:3}, cycle:{self.cycle:3}", end="")

        if self.cycle in (20, 60, 100, 140, 180, 220):
            signal_strength = self.x * self.cycle
            self.total += signal_strength

            # print(f" -----> strength:{signal_strength}")
        else:
            # print()
            pass

    def __init__(self, data):
        self.data = data
        self.total = 0

        self.x = 1
        self.cycle = 0

        # noop --> +1 cycle
        # addx --> +2 cycle, add x val

        for i, line in enumerate(self.data, start=1):
            # calculate values for cycle and x
            if line == "noop":
                self.check_signal_strength(i, line)
            else:
                value = int(line.split(" ")[1])

                # phase 1, for addx statement
                self.check_signal_strength(i, line)

                # phase 2, for addx statement
                self.check_signal_strength(i, line)
                self.x += value

        print(f"\n--- Part 1: ---")
        print(f"{self.total}\n")
