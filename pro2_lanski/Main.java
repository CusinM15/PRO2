public class Main 
{
	// nisem glih naredu toèno koker je naloga bla zahtevana (koker je sploh podan)
	// sam pomojem kar se kode tièe bo pomojem neki tazga
	// + nisem uporablju abstraknih razredov
	
	public static void main(String[] args)
	{
		// za testiranje
		System.out.println(new Pijace());
		System.out.println(new Pijace("voda", (float) 0.25));
		System.out.println(new AlkoholnePijace("vino", (float) 0.20, (float) 0.11));
	}
	
}

class Pijace {
	
	private String ime;
	private float volumen;
	  
	public Pijace() {
		this.ime = "null";
		this.volumen = 0;
	}
	
	public Pijace(String ime, float volumen)
	{
		super();
	    
	    this.ime = ime;
	    this.volumen = volumen;
	}
	 
	public String getIme() 
	{
		return ime;
	}
	public float getVolumen() 
	{
		return volumen;
	}
	
	@Override
	public String toString() {
		return "ime = " + getIme() + ", volumen = " + getVolumen();
	}
}

class AlkoholnePijace extends Pijace
{
	private float alkohol;
	
	public AlkoholnePijace(String ime, float volumen, float alkohol) {
		super(ime, volumen);
		
		this.alkohol = alkohol;

	}
	
	public float getAlkohol() {
		return alkohol;
	}

	@Override
	public String toString() {
		return super.toString() + ", Alkohol = " + getAlkohol();
	}
}

