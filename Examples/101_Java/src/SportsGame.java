/**
 * The Game class.  Drives the rest of the program.
 */
public class SportsGame {

	public static void main(String[] args) {
		
		Player p1 = new Player("Snoopy");
		Player p2 = new Player("Woodstock");
		Ball theBall = new Ball("soccer ball");
		Field theField = new Field();
		
		// for (INIT; CONTINUE; UPDATE)
		for (int i = 0; i < 5; i+=1) {
			p1.kick(theBall, theField);
			p2.pass(p1, theBall);
		}
		
		// game is over, what is the score?
		System.out.println(theField);
		System.out.println("The team won!");
		
	}
}
