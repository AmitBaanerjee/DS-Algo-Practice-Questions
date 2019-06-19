package LinkedList;

//SINGLY LINKED LIST IMPLEMENTATION
public class LinkedList {
	
	Node head;
	int count;
	
	//LinkedList cannot be made with null head. There has to be atleast one element
/*	public LinkedList() {
		head=null;
		count=0;
	}*/
	
	public LinkedList(Node newHead) {
		head=newHead;
		count=1;
	}
	
	public void addNode(int newData) {
		Node temp=new Node(newData);
		Node current=head;
		while (current.getNext()!=null) {
			current=current.getNext();
		}
		current.setNext(temp);
		count++;
	}
	
	public int get(int index) {
		if (index<0) {
			return -1;
		}
		Node current=head;
		for(int i=1;i<index;i++) {
			current=current.getNext();
		}
		return current.getData();
	}
	
	public int getSize() {
		return count; 
	}
	
	public boolean isEmpty() {
		return head==null;
	}
	
	public void removeNode() {
		Node current=head;
		while(current.getNext().getNext()!=null) {
			current=current.getNext();
			}
		current.setNext(null);
		count--;
	}
	
	public static void main(String args[]) {
		Node first=new Node(1);
		LinkedList l=new LinkedList(first);
		l.addNode(2);
		l.addNode(3);
		System.out.println(l.getSize());
		System.out.println(l.isEmpty());
		System.out.println(l.get(2));
	}
}
