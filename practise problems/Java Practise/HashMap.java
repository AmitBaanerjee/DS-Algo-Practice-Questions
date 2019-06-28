import java.util.HashMap;
import java.util.Map;

public class Test {

	public static void main(String[] args) {

		Map<String,Integer> dictionary=new HashMap<String,Integer>();
		dictionary.put("one",1);
		dictionary.put("two",2);
		if (dictionary.containsKey("three")) {
			System.out.println("three is present in the hashmap");
		}
		else {
			System.out.println("three is not present in the hashmap");
		}
		System.out.println(dictionary.get("one"));
		System.out.println(dictionary.containsValue(1));
	}
}
