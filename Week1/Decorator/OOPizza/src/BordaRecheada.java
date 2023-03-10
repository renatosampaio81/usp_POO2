
public class BordaRecheada extends PizzaDecorator {

	BordaRecheada (Pizza p) {
		super(p);
	}
	
	public int preco () {
		return pizzaDecorada.preco()+10;
	}
	
}
