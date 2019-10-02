/*
 * RockPaperScissors.java
 * inputs: rock paper scissors or quit
 * outputs: game outcome
 * description: prompt the two players to play RPS
 * author: Yuntian Yang
 * date: 9/20/19
 */

import java.util.Scanner;

public class RockPaperScissors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		System.out.print("Pick 'R', 'P', or 'S'(Enter 'Q' to quit): \n");
		
		char player1 = ' '; // single quotes for char and double quotes for string
		char player2 = ' ';
		char play = ' ';
		
		do
		{	
			// take input from player 1
			System.out.println("Player 1's turn to play: ");
			player1 = input.next().toUpperCase().charAt(0);
			if (player1 == 'Q')
			{
				System.out.println("Player quit. Re-run the program to play.");
				continue;
			}
			// take input from player 2	
			System.out.println("Player 2's turn to play: ");
			player2 = input.next().toUpperCase().charAt(0);
			if (player2 == 'Q')
			{
				System.out.println("Player quit. Re-run the program to play.");
				continue;
			}
			
			// determine game result 
			if ((player1 == 'R' && player2 == 'S') || (player1 == 'P' && player2 == 'R') || (player1 == 'S' && player2 == 'P'))
			{
				System.out.println("Player 1 wins!");
				System.out.println("Do you want to play again?");
				play = input.next().toUpperCase().charAt(0);
				if (play == 'Y') {
					continue;
				} else if (play == 'N') {
					System.out.println("Game terminated.");
					break;
				} else {
					do {
					System.out.println("Invalid option. Answer with 'Y' or 'N'.");
					System.out.println("Do you want to play again?");
					play = input.next().toUpperCase().charAt(0);
					if (play == 'Y') {
						break;
					} else if (play == 'N') {
						System.out.println("game terminated.");
						System.exit(0);
					}
					} while (play != 'Y' || play != 'N');
				}
			} 
			else if ((player2 == 'R' && player1 == 'S') || (player2 == 'P' && player1 == 'R') || (player2 == 'S' && player1 == 'P'))
			{
				System.out.println("Player 2 wins!");
				System.out.println("Do you want to play again?");
				play = input.next().toUpperCase().charAt(0);
				if (play == 'Y') {
					continue;
				} else if (play == 'N') {
					System.out.println("Game terminated.");
					break;
				} else {
					do {
						System.out.println("Invalid option. Answer with 'Y' or 'N'.");
						System.out.println("Do you want to play again?");
						play = input.next().toUpperCase().charAt(0);
						if (play == 'Y') {
							break;
						} else if (play == 'N') {
							System.out.println("game terminated.");
							System.exit(0);
						}
						} while (play != 'Y' || play != 'N');
				}
				
			}
			else if (player1 == player2)
			{
				System.out.println("Tied");
				System.out.println("Do you want to play again?");
				play = input.next().toUpperCase().charAt(0);
				if (play == 'Y') {
					continue;
				} else if (play == 'N') {
					System.out.println("Game terminated.");
					break;
				} else {
					do {
						System.out.println("Invalid option. Answer with 'Y' or 'N'.");
						System.out.println("Do you want to play again?");
						play = input.next().toUpperCase().charAt(0);
						if (play == 'Y') {
							break;
						} else if (play == 'N') {
							System.out.println("game terminated.");
							System.exit(0);
						}
						} while (play != 'Y' || play != 'N');
				}
			}
			else 
			{
				System.out.println("Invalid entry. Enter R P S or Q in either cases. Game restarted.");
				continue;
			} 
		} while ((player1 != 'Q' && player2 != 'Q') || play == 'Y');

	}
	
}