package LinkedList;

public class Node {
	int data;
	Node next;
	
	public Node(int newData) {
		data=newData;
		next=null;
	}
	
	public Node(int newData,Node newNext) {
		data=newData;
		this.next=newNext;
	}
	
	public int getData() {
		return data;
	}
	
	public Node getNext() {
		return next;
	}
	
	public void setData(int data) {
		this.data=data;
	}
	
	public void setNext(Node next) {
		this.next=next;
	}
	
}
