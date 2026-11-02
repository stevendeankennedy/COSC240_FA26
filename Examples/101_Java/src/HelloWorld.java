/**
 * The blue comments are called "JavaDocs"
 * @author sdkennedy, Bailey, Cole
 */
public class HelloWorld { // This is an inline comment

	/*
	 * This is a standard block comment.
	 */
	public static void main(String[] args) {
		System.out.println("Hello, COSC240!");
		
		// The syntax is:
		//	TYPE IDENTIFIER = DATA;
		String name = "Tyler";
		System.out.printf("Hello, %s!%n", name);
		
		// Mad Libs sentence!
		// My sentence will be:
		//	"The NOUN VERBed over the ADJ NOUN!"
		String noun1 = "choo choo";
		String verb = "die";
		String adjective = "small";
		String noun2 = "mountain";
		System.out.printf("The %s %sed over the %s %s!%n", noun1, verb, adjective, noun2);
	}
	
}
