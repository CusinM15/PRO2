package Kaca;

public class Celica {

		  /**
		   * {@link Position} of the cell in the Cartesian coordinate plane.
		   */
		  private Pozicija pozicija;
		  
		  /**
		   * Intrinsic value of the cell equal to a non-negative integer.
		   */
		  private int vrednost;
		  
		  /**
		   * Predefined label of the cell equal to a single character.
		   */
		  private char oznaka;
		  
		  /**
		   * Boolean representing whether the cell is occupiable (e.g. empty).
		   */
		  private boolean prosto;

		  /**
		   * Constructs a cell on a {@link Board} represented by the Cartesian coordinate plane.
		   *
		   * The cell is specified by its {@link Position} in the plane, its intrinsic non-negative value, a predefined label as a single character and whether the cell is occupiable.
		   *
		   * @param position {@link Position} of the cell on a {@link Board}
		   * @param value intrinsic non-negative value of the cell
		   * @param label predefined label or character of the cell
		   * @param occupiable whether the cell is occupiable
		   */
		  public Celica(Pozicija pozicija, int vrednost, char oznaka, boolean prosto) {
		    if (vrednost < 0)
		      throw new IllegalArgumentException();
		    
		    this.pozicija = pozicija;
		    this.vrednost = vrednost;
		    this.oznaka = oznaka;
		    this.prosto = prosto;
		  }

		  /**
		   * Returns the {@link Position} of the cell on a {@link Board}.
		   *
		   * @return position of the cell on a {@link Board}
		   */
		  public Pozicija getPozicija() {
		    return pozicija;
		  }
		  
		  /**
		   * Sets the {@link Position} of the cell on a {@link Board} to the specified position.
		   *
		   * @param position new position of the cell on a {@link Board}
		   */
		  public void setPozicija(Pozicija pozicija) {
		    this.pozicija = pozicija;
		  }

		  /**
		   * Returns the value of the cell on a {@link Board} equal to a non-negative integer.
		   *
		   * @return value of the cell on a {@link Board}
		   */
		  public int getVrednost() {
		    return vrednost;
		  }

		  /**
		   * Returns the label of the cell on a {@link Board} equal to a single character.
		   *
		   * @return label of the cell on a {@link Board}
		   */
		  public char getOznaka() {
		    return oznaka;
		  }

		  /**
		   * Returns whether the cell on a {@link Board} is occupiable (e.g. empty).
		   *
		   * @return whether the cell on a {@link Board} is occupiable
		   */
		  public boolean isProsto() {
		    return prosto;
		  }

		  /**
		   * Returns {@link String} representation of the cell on a {@link Board} equal to its label.
		   *
		   * @return {@link String} representation of the cell on a {@link Board}
		   */
		  @Override
		  public String toString() {
		    return "" + getOznaka();
		  }

		  /**
		   * Returns randomly selected cell at the specified {@link Position} on a {@link Board}.
		   *
		   * The function returns random {@link Coin} with probability {@link Pacmans#COINS_PROBABILITY}, {@link Block} cell with probability {@link Pacmans#BLOCKS_PROBABILITY} and {@link Empty} cell otherwise.
		   *
		   * @param position {@link Position} of the cell on a {@link Board}
		   *
		   * @return random cell at the specified {@link Position} on a {@link Board}
		   */
//		  public static Celica random(Pozicija pozicija) {
//		    double random = Math.random();
//		    
//		    if (random < Pacmans.COINS_PROBABILITY)
//		      return Coin.random(position);
//		    else if (random < Pacmans.COINS_PROBABILITY + Pacmans.BLOCKS_PROBABILITY)
//		      return new Block(position);
//		    else
//		      return new Empty(position);
//		  }
		  
		

}
