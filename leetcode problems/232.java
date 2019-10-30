232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

class MyQueue {
    Stack<Integer> s=new Stack<Integer>();
    Stack<Integer> main=new Stack<Integer>();
    /** Initialize your data structure here. */
    public MyQueue() {

    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        main.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        s=new Stack<Integer>();
        while(!main.isEmpty()){
            s.push(main.pop());
        }
        int item=s.pop();
        while(!s.isEmpty()){
            main.push(s.pop());
        }
        return item;
    }

    /** Get the front element. */
    public int peek() {
        s=new Stack<Integer>();
        while(!main.isEmpty()){
            s.push(main.pop());
        }
        int val=s.peek();
        while(!s.isEmpty()){
            main.push(s.pop());
        }
        return val;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return main.size()==0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
