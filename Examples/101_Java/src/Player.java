/**
 * This class defines a soccer player for our Sports Game program!
 * 
 * Authors:
 * 	Michael R, Bailey, Cole, Juaquim, Declan, 
 */
public class Player {

	// state
	private String name; // encapsulate name with private
	private int goals;
	private int number;
	private String position;
	
	// CONSTRUCTOR method
	public Player(String name) {
		this.name = name;
	}
	
	// behavior
	public void kick(Ball ball, Field theField) {
//		System.out.println(name + " kicked!");
		System.out.printf("%s kicked the %s and scored a point%n", name, ball);
//		theField.score1 += 1; // <- won't work
		theField.addScore1(1);
		goals += 1;
	}
	
	public void pass(Player p, Ball ball) {
//		System.out.println(name + " passes to " + p.name + "!");
		System.out.printf("%s passes %s to %s%n", name, ball, p.name);
	}
	
	public void run() {
		System.out.println(name + " runs!");
	}
	
	
}
