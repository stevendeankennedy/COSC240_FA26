
public class Ball {

	// type
	private String type;
	
	// CONSTRUCTOR for ball
	public Ball(String type) {
		this.type = type;
	}
	
	// bounce
	public void bounce() {
		System.out.println("bounce!");
	}
	
	/**
	 * Return the String representation of this object.
	 */
	public String toString() {
		return type;
	}
}
