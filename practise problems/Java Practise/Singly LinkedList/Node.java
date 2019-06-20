package LinkedList;
class Node{
	int data;
	Node pointer;

	public Node(int data) {
		this.data=data;
		pointer=null;
	}

	public Node(int data,Node pointer) {
		this.data=data;
		this.pointer=pointer;
	}

	public int getData() {
		return data;
	}

	public Node getPointer() {
		return pointer;
	}

	public void setData(int newData) {
		this.data=newData;
	}

	public void setPointer(Node pointer) {
		this.pointer=pointer;
	}


}
