package Kaca;

/**
 * Class representing a position in the Cartesian coordinate plane.
 *
 * The position is represented by its horizontal and vertical coordinates.
 *
 * @author Lovro Šubelj
 */ 
public class Pozicija {

	  /**
	   * Horizontal coordinate or abscissa of the position.
	   */
	  private int x;
	  
	  /**
	   * Vertical coordinate or ordinate of the position.
	   */
	  private int y;

	  /**
	   * Constructs a position in the Cartesian coordinate plane represented by its horizontal and vertical coordinates.
	   *
	   * @param x horizontal coordinate or abscissa
	   * @param y vertical coordinate or ordinate
	   */
	  public Pozicija(int x, int y) {
	    this.x = x;
	    this.y = y;
	  }

	  /**
	   * Returns horizontal coordinate of the position in the Cartesian coordinate plane.
	   *
	   * @return horizontal coordinate or abscissa
	   */
	  public int getX() {
	    return x;
	  }

	  /**
	   * Returns vertical coordinate of the position in the Cartesian coordinate plane.
	   *
	   * @return vertical coordinate or ordinate
	   */
	  public int getY() {
	    return y;
	  }




/**
 * Returns a new position in the Cartesian coordinate plane moved by the specified point.
 *
 * @param x horizontal coordinate or abscissa of the point
 * @param y vertical coordinate or ordinate of the point
 *
 * @return position moved by the horizontal and vertical coordinates of the specified point
 */
public Pozicija premik(int x, int y) {
  return new Pozicija(getX() + x, getY() + y);
}

/**
 * Computes Euclidean distance between the position in the Cartesian coordinate plane and the specified point.
 *
 * @param x horizontal coordinate or abscissa of the point
 * @param y vertical coordinate or ordinate of the point
 *
 * @return Euclidean distance between the position and the specified point
 */
public double razdalja(int x, int y) {
  return Math.sqrt(Math.pow(getX() - x, 2.0) + Math.pow(getY() - y, 2.0));
}

/**
 * Returns random unoccupied position in the Cartesian coordinate plane corresponding to the specified {@link Board}.
 *
 * The function ensures that the returned position is unoccupied or empty tested by whether {@link Board#getCell(Position)} equals {@code null}.
 *
 * @param board {@link Board} representing the Cartesian coordinate plane
 *
 * @return random position in the Cartesian coordinate plane corresponding to the specified {@link Board}
 */
public static Pozicija zacetek(Polje polje) {
	
  Pozicija pozicija = new Pozicija((int)(0.5 * polje.getSirina()), (int)(0.5 * polje.getVisina()));
  
 
  return pozicija;
}

}