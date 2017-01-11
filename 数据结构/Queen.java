public class Queen<T>{
	private Node head;
	private Node tail;
	public void add(T data){
		Node node = new Node(data);
		if(tail == null){
			tail = node;
			head = node;
		}
		else{
			tail.setNext(node);
			tail = node;
		}
	}
	public T peek(){
		if(head == null){
			return null;
		}
		else{
			Node node = head;
			head = head.getNext();
			return node.getData();
		}

	}
	class Node{
		private T data;
		private Node next;
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
		public void setNext(Node next){
			this.next = next;
		}
		public Node getNext(){
			return this.next;
		}
	}

	public static void main(String[] args) {
		Queen<String> queen = new Queen<String>();
		queen.add("1");
		queen.add("2");
		queen.add("3");
		System.out.println(queen.peek());
		System.out.println(queen.peek());
		System.out.println(queen.peek());
	}
}