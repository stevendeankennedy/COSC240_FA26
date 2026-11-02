/**
 * Represents the field in our game.
 */
public class Field {
	private int score1;
	private int score2;
	
	public Field() {
		score1 = 0;
		score2 = 0;
	}
	
	// setter for adding a point
	// aka a "mutator"
	public void addScore1(int point) {
		score1 += point;
	}
	
	// setter to add a point to score 2
	public void addScore2(int point) {
		score2 += point;
	}
	
	// getter for score team 1
	public int getScore1() {
		return score1;
	}
	
	// getter for score team 2
	public int getScore2() {
		return score2;
	}
	
	public String toString() {
		return "The score is " + score1 + ":" + score2;
	}
}
