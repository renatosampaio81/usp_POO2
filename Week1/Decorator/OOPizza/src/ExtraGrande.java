
public class ExtraGrande extends PizzaDecorator {
	
	ExtraGrande (Pizza p) {
		super(p);
	}
	
	public int preco () {
		return (int) (pizzaDecorada.preco() * 1.3);
	}

}
