package Kaca;

public class Polje {
	  /**
	   * Board of {@link Cell}-s in the Cartesian coordinate plane.
	   */
	  private Celica[][] polje;
	  /**
	   * Constructs a board of {@link Cell}-s in the Cartesian coordinate plane with the specified size (i.e. width and height).
	   *
	   * The board contains the specified number of randomly positioned {@link Pacman}-s with two prime {@link Pacman}-s. Other {@link Cell}-s are random {@link Coin}-s with probability {@link Pacmans#COINS_PROBABILITY} returned by {@link Coin#random(Position)}, {@link Block} cells with probability {@link Pacmans#BLOCKS_PROBABILITY} and {@link Empty} cells otherwise.
	   *
	   * @param size width and height of the board of {@link Cell}-s
	   * @param pacmans number of {@link Pacman}-s of the board
	   */
	  public Polje(int velikost) {
	    this(velikost, velikost);
	  }
	  /**
	   * Constructs a board of {@link Cell}-s in the Cartesian coordinate plane with the specified width and height.
	   *
	   * The board contains the specified number of randomly positioned {@link Pacman}-s with two prime {@link Pacman}-s. Other {@link Cell}-s are random {@link Coin}-s with probability {@link Pacmans#COINS_PROBABILITY} returned by {@link Coin#random(Position)}, {@link Block} cells with probability {@link Pacmans#BLOCKS_PROBABILITY} and {@link Empty} cells otherwise.
	   *
	   * @param width width of the board of {@link Cell}-s
	   * @param height height of the board of {@link Cell}-s
	   * @param pacmans number of {@link Pacman}-s of the board
	   */
	  public Polje(int sirina, int visina) {
	    if (sirina <= 0 || visina <= 0)
	      throw new IllegalArgumentException();
	    
	    polje = new Celica[sirina][visina];
	    Pozicija pozicija = Pozicija.zacetek(this);
	    
	    setCelica(pozicija, new Kaca(pozicija, 0, '*', false));
	   
	  }
	  
	  /**
	   * Returns the width of the board of {@link Cell}-s in the Cartesian coordinate plane.
	   *
	   * @return width of the board of {@link Cell}-s
	   */
	  public int getSirina() {
	    return polje.length;
	  }
	  
	  /**
	   * Returns the height of the board of {@link Cell}-s in the Cartesian coordinate plane.
	   *
	   * @return height of the board of {@link Cell}-s
	   */
	  public int getVisina() {
	    return polje[0].length;
	  }

	  /**
	   * Returns the {@link Cell} on the board in the Cartesian coordinate plane at the specified {@link Position}.
	   *
	   * @param position {@link Position} on the board in the Cartesian coordinate plane
	   *
	   * @return {@link Cell} on the board at the specified {@link Position}
	   */
	  public Celica getCelica(Pozicija pozicija) {
	    return polje[pozicija.getX()][pozicija.getY()];
	  }
	  
	  /**
	   * Sets the specified {@link Cell} to the specified {@link Position} on the board in the Cartesian coordinate plane.
	   *
	   * @param position {@link Position} on the board in the Cartesian coordinate plane
	   * @param cell new {@link Cell} on the board at the specified {@link Position}
	   */
	  public void setCelica(Pozicija pozicija, Celica celica) {
	    polje[pozicija.getX()][pozicija.getY()] = celica;
	  }

	  /**
	   * Returns {@link String} representation of the board of {@link Cell}-s in the Cartesian coordinate plane.
	   *
	   * @return {@link String} representation of the board of {@link Cell}-s
	   */
//	  @Override
//	  public String toString() {
//	    String string = "   ";
//	    for (int i = 0; i < 2 * getWidth() + 1; i++)
//	      string += "-";
//	    string += "\n";
//	    
//	    for (int j = 0; j < getHeight(); j++) {
//	      string += "   |";
//	      for (int i = 0; i < getWidth(); i++)
//	        string += getCell(new Position(i, j)) + "|";
//	      string += "\n";
//	    }
//	    
//	    string += "   ";
//	    for (int i = 0; i < 2 * getWidth() + 1; i++)
//	      string += "-";
//	    
//	    return string;
//	  }

}
