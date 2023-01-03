// 1 - A - X - for Rock
// 2 - B - Y - for Paper
// 3 - C - Z - for Scissors

// 0 - if you lost
// 3 - if the round was a draw
// 6 - if you won

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import java.util.HashMap;

public class Part1 {
	public Integer total_score = 0;
	private Character opp, me;

	HashMap<Character, String> rpc_name = new HashMap<>();

	private void assign_rpc_name() {
		rpc_name.put('A', "Rock");
		rpc_name.put('B', "Paper");
		rpc_name.put('C', "Scissors");

		rpc_name.put('X', "Rock");
		rpc_name.put('Y', "Paper");
		rpc_name.put('Z', "Scissors");
	}

	private Boolean is_tie() {
		if (this.opp == 'A' && this.me == 'X') // Rock
			return true;

		if (this.opp == 'B' && this.me == 'Y') // Paper
			return true;

		if (this.opp == 'C' && this.me == 'Z') // Scissors
			return true;

		return false;
	}

	private Boolean is_winning() {
		if (this.opp == 'A' && this.me == 'Y') // Rock - Paper
			return true;

		if (this.opp == 'B' && this.me == 'Z') // Paper - Scissors
			return true;

		if (this.opp == 'C' && this.me == 'X') // Scissors - Rock
			return true;

		return false;
	}

	// rps: Rock, Paper, Scissors values
	private Integer rps_value() {
		switch (this.me) {
			case 'X':
				return 1;
			case 'Y':
				return 2;
			case 'Z':
				return 3;
		}

		return null;
	}

	private Integer current_score() {
		Integer rps_value = this.rps_value(), score;
		System.out.print(String.format("(%c-%c):(%-8s Vs %-8s): ", opp, me, rpc_name.get(opp), rpc_name.get(me)));

		// draw
		if (this.is_tie()) {
			System.out.print("Draw :(3+");
			score = 3 + rps_value;
		}

		// won
		else if (this.is_winning()) {
			System.out.print("Won  :(6+");
			score = 6 + rps_value;
		}

		// lost
		else {
			System.out.print("Lost :(0+");
			score = 0 + rps_value;
		}

		System.out.println(rps_value + "=" + score + ")");
		return score;

	}

	public Part1() throws FileNotFoundException {
		File file = new File("./example_input.txt");
		// File file = new File("./input.txt");
		Scanner scan = new Scanner(file);
		this.assign_rpc_name();

		// looping file
		while (scan.hasNextLine()) {
			String line = scan.nextLine();

			this.opp = line.charAt(0); // opponent
			this.me = line.charAt(2); // yourself

			this.total_score += this.current_score();
		}

		scan.close();
	}

	public static void main(String[] args) throws FileNotFoundException {
		Part1 obj = new Part1();

		// Part-1
		System.out.println("\nTotal score: " + obj.total_score);
	}
}
