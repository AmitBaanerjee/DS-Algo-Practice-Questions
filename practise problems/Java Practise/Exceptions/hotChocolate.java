package Exceptions;

public class hotChocolate {
	public static final double tooHot=185;
	public static final double tooCold=160;

	public static void drink(double drinkTemp)throws tooCold,tooHot{
		if (drinkTemp<tooCold) {
			throw new tooCold();
		}
		else if(drinkTemp>tooHot){
			throw new tooHot();
		}

	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double currentTemp=200;
		boolean notDrunk=true;
		while(notDrunk) {
			try {
				//drink(currentTemp);
				drink(currentTemp);
				System.out.println("drunk comfortably!");
				notDrunk=false;
			}
			catch(tooCold e1){
				e1.printStackTrace();
				currentTemp+=5;
			}
			catch(tooHot e2) {
				System.out.println("too Hot!");
				currentTemp-=5;
			}
		}
	}

}
