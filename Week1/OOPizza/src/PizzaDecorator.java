
public abstract class PizzaDecorator implements Pizza{
	
	Pizza pizzaDecorada;
	
	PizzaDecorator(Pizza pizza) {
		pizzaDecorada = pizza;
	}

}
