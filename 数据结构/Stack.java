public class Stack<T>{
	private Node head;
	public void push(T data){
		Node node  = new Node(data);
		if(null == head){
			head = node;
		}
		else{
			node.setPre(head);
			head = node;
		}
	}
	public T pop(){
		if(head == null){
			return null;
		}
		else{
			Node node = head;
			head = head.getPre();
			return node.getData();
			
		}
	}



	class Node{
		private T data;
		private Node pre;
		public Node(){

		}
		public Node(T data){
			this.data = data;
		}
		public T getData(){
			return this.data;
		}
		public void setData(T data){
			 this.data = data;
		}
		public void setPre(Node pre){
			this.pre = pre;
		}
		public Node getPre(){
			return this.pre;
		}

	}

	public static void main(String[] args) {
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(1);
		stack.push(2);
		stack.push(3);
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
	}
}