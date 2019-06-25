
public class genericTest<E extends Comparable<E>> {

	public void print(E item) {
		System.out.println(item);
	}

	//the comparable part shows that the datatype which is going to be used with the function
	//will require the comparable interface to implement the compareTo method for comparing
	//two elements with each other

	public <E extends Comparable<E>> int comparison(E element1,E element2) {
		int result=(element1.compareTo(element2));
		return result;
	}
	public static void main(String[] args) {
		genericTest<String> g =new genericTest();
		g.print("amit");
		genericTest<Integer> g1 =new genericTest();
		g1.print(45452);
		genericTest<Double> g2 =new genericTest();
		g2.print(34.3424);
		System.out.println(g2.comparison(10,10));
	}

}
