package Kaca;

public class Prazen extends Celica {

		  /**
		   * Constructs an empty {@link Cell} on a {@link Board} represented by the Cartesian coordinate plane.
		   *
		   * The {@link Cell} is specified by its {@link Position} in the plane which is occupiable, while its intrinsic value equals {@code 0} and its label equals {@code ' '}.
		   *
		   * @param position {@link Position} of the {@link Cell} on a {@link Board}
		   */
		  public Prazen(Pozicija pozicija) {
		    super(pozicija, 0, ' ', true);
		  }
		  
		
}
