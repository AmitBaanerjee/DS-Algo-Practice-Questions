package Inheritance;

public class Pug extends Dog{
	
	private double weight;
	
	public Pug() {
		System.out.println("A new Pug has been created to test the bark method!");
		
	}
	public void bark() {
		System.out.print("The pug is barking as part of an abstract method!");
	}
	
	public void getWeight() {
		System.out.println("The weight of this pug is : "+weight+" pounds");
	}
	
	public void setWeight(double newWeight) {
		this.weight=newWeight;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Pug p=new Pug();
		p.setType("Mammal");
		p.setColor("Black and white mix");
		p.setHands(0);
		p.setLegs(2);
		p.setWeight(190.23);
		p.AnimalDesc();
		p.getWeight();
	}

}
