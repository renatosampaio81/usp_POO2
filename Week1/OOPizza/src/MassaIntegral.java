
public class MassaIntegral extends PizzaDecorator {
	
	MassaIntegral (Pizza p) {
		super(p);
	}
	
	public int preco () {
		return pizzaDecorada.preco()+5;
	}

}
