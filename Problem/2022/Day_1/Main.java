import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import java.util.ArrayList;
import java.util.Collections;

public class Main {
	private ArrayList<Long> elf_calories = new ArrayList<>();

	public long top_one() {
		return elf_calories.get(0);
	}

	public long top_three() {
		return elf_calories.get(0) + elf_calories.get(1) + elf_calories.get(2);
	}

	private void add_elf_calories(int i, long sum) {
		elf_calories.add(sum);
		System.out.println(String.format("Elf: %d, sum: %d", i, sum));
	}

	public Main() throws FileNotFoundException {
		// File file = new File("./example_input.txt");
		File file = new File("./input.txt");
		Scanner scan = new Scanner(file);

		long sum = 0;
		int i = 0, cal;

		// looping file
		while (scan.hasNextLine()) {
			String line = scan.nextLine();

			if (line.isEmpty()) {
				add_elf_calories(i++, sum);
				sum = 0;
			} else {
				cal = Integer.parseInt(line);
				sum += cal;
			}
		}
		add_elf_calories(i++, sum);

		// sort list
		Collections.sort(elf_calories, Collections.reverseOrder());

		scan.close();
	}

	public static void main(String[] args) throws FileNotFoundException {
		Main obj = new Main();

		// part-1
		System.out.println();
		System.out.println("Top 1 val : " + obj.top_one());

		// part-2
		System.out.println("Top 3 val : " + obj.top_three());

	}
}
