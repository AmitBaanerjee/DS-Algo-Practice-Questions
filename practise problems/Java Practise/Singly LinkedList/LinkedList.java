package LinkedList;

public class LinkedList {
	Node head;
	int counter;

	public LinkedList(Node head) {
		this.head=head;
		counter=1;
	}
	public void addNode(int data) {
		Node temp=new Node(data);
		Node current=head;
		while (current.getPointer()!=null) {
			current=current.getPointer();
		}
		current.setPointer(temp);
		counter++;
		System.out.println("New node with data "+ data+ " has been added to the linkedlist");
	}

	public void printNodes() {
		Node current=head;
		while(current.getPointer()!=null) {
			System.out.print(current.getData()+"-->");
			current=current.getPointer();
		}
		System.out.print(current.getData());
	}
	public void remove(int index) {
		Node current=head;
		for(int i=1;i<index;i++) {
			current=current.getPointer();
			}
		current.setPointer(null);
		counter=counter-1;

	}
	public void isEmpty() {
		if (head==null) {
			System.out.println("The linkedlist is empty for sure.");
		}
		else {
			System.out.println("The linkedlist is not empty,great!");
		}
	}
	public int getSize() {
		return counter;
	}
	public static void main(String args[]) {
		Node n1=new Node(1);
		LinkedList l1=new LinkedList(n1);
		l1.addNode(2);
		l1.addNode(3);
		l1.printNodes();
		l1.remove(2);
		System.out.println();
		l1.printNodes();
		System.out.println();
		l1.isEmpty();
		System.out.println("Size of the linkedlist is :"+l1.getSize());

	}
}
