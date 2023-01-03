// X - Lost
// Y - Draw
// Z - Win

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import java.util.HashMap;

public class Part2 {
	public Integer total_score = 0;
	private HashMap<Character, Integer> hm = new HashMap<>();

	private Character opp;
	private Character result;

	private Integer rock = 1;
	private Integer paper = 2;
	private Integer scissors = 3;

	private Integer lost = 0;
	private Integer draw = 3;
	private Integer win = 6;

	private void assign_hm() {
		hm.put('A', this.rock);
		hm.put('B', this.paper);
		hm.put('C', this.scissors);

		hm.put('X', this.lost);
		hm.put('Y', this.draw);
		hm.put('Z', this.win);
	}

	public Part2() throws FileNotFoundException {
		// File file = new File("./example_input.txt");
		File file = new File("./input.txt");
		Scanner scan = new Scanner(file);

		Integer score;

		this.assign_hm();

		// looping file
		while (scan.hasNextLine()) {
			String line = scan.nextLine();
			score = 0;

			this.opp = line.charAt(0);
			this.result = line.charAt(2);

			System.out.print(String.format("%c-%c : ", this.opp, this.result));

			if (hm.get(this.result) == this.draw) {
				score += this.draw;
				score += hm.get(this.opp);

				System.out.print(String.format("draw : %d+%d", hm.get(this.opp), this.draw));
			} else if (hm.get(this.result) == this.win) {
				score += this.win;

				if (hm.get(this.opp) == this.rock)
					score += this.paper;
				else if (hm.get(this.opp) == this.paper)
					score += this.scissors;
				else if (hm.get(this.opp) == this.scissors)
					score += this.rock;

				System.out.print(String.format("win  : %d+%d", score - this.win, this.win));

			} else if (hm.get(this.result) == this.lost) {
				score += this.lost;

				if (hm.get(this.opp) == this.rock)
					score += this.scissors;
				else if (hm.get(this.opp) == this.paper)
					score += this.rock;
				else if (hm.get(this.opp) == this.scissors)
					score += this.paper;

				System.out.print(String.format("lost : %d+%d", score - this.lost, this.lost));

			}

			this.total_score += score;
			System.out.println("=" + score);
		}

		scan.close();
	}

	public static void main(String[] args) throws FileNotFoundException {
		Part2 obj = new Part2();

		// Part-2
		System.out.println("\nTotal score: " + obj.total_score);
	}
}
