package Inheritance;

public class Animal {
	private int hands;
	private int legs;
	private String type;
	private String color;

	public Animal() {
		System.out.println("A new animal is getting created inside Animal constructor!");
	}

	public int getHands() {
		return hands;
	}

	public int getLegs() {
		return legs;
	}

	public String getType() {
		return type;
	}

	public String getColor() {
		return color;
	}

	public void setHands(int newHands) {
		this.hands=newHands;
	}

	public void setLegs(int newLegs) {
		this.legs=newLegs;
	}

	public void setType(String newType) {
		this.type=newType;
	}

	public void setColor(String newColor) {
		this.color=newColor;
	}

	public void AnimalDesc() {
		System.out.println("This animal has "+getHands()+" hands and "+getLegs()+" legs and is of "
				+getType()+" type and has the "+getColor()+" color");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Object a1 =new Animal();
		Animal a2=(Animal)a1;
		a2.setHands(2);
		a2.setLegs(2);
		a2.setType("Mammal");
		a2.setColor("Brown");
		a2.AnimalDesc();

	}

}
