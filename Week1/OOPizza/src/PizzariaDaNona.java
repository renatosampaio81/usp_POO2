import java.util.HashMap;

public class PizzariaDaNona {
	
	public static void main(String[] args) {
		
		HashMap<String,Integer> ingredientes = new HashMap<>();
		ingredientes.put("Massa", 10);
		ingredientes.put("Muzzarela", 20);
		ingredientes.put("Tomate", 5);
		ingredientes.put("Mangericao", 5);
		
		Pizza margerita = new PizzaDaNona(ingredientes);
		
		Pizza minhaSuperMarguerita = new ExtraGrande (new BordaRecheada (new MassaIntegral (margerita) ));
		
		System.out.println("Minha pizza custará R$ " + minhaSuperMarguerita.preco());
	}

}
