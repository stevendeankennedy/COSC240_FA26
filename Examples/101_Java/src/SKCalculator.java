import java.util.Scanner;  // import Scanner code from Java's library

/**
 * This program is a very simple calculator.
 * 
 * @author Steve Kennedy
 * @date 9/21/2026
 */
public class SKCalculator {

	/**
	 * Get 2 numbers and an operator and run the operation asked
	 * 
	 * Special thanks to Michael R, Cole and Bailey!
	 */
	public static void main(String[] args) {
		
		// make a new Scanner for reading the keyboard input
		Scanner userIn = new Scanner(System.in);
		
		// old version
//		int firstNum = 11;
//		int secondNum = 67;
		
		
		// Scanner version
		System.out.print("First num>");
		int firstNum = userIn.nextInt();
		System.out.print("Second num>");
		int secondNum = userIn.nextInt();
		System.out.print("Operation (+,-,/,*)>");
		// get the first character from the input and store it
		char operator = userIn.next().charAt(0);  // charAt(i) gets a character
		
		int result = 0;
		// Do the arithmetic based on the operator
		if (operator == '+') {
			result = firstNum + secondNum;
		} else if (operator == '-') {
			result = firstNum - secondNum;
		}
		
		
		System.out.printf("%d %c %d = %d", firstNum, operator, secondNum, result);  // %d for integer "digits"
	}

}
