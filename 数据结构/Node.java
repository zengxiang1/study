package com.zx;
public class Node {
	private int value;
	private Node left;
	private Node right;
	public Node(int value, Node left, Node right) {
		this.value = value;
		this.left = left;
		this.right = right;
	}
	public int getValue() {
		return value;
	}
	public void setValue(int value) {
		this.value = value;
	}
	public Node getLeft() {
		return left;
	}
	public void setLeft(Node left) {
		this.left = left;
	}
	public Node getRight() {
		return right;
	}
	public void setRight(Node right) {
		this.right = right;
	}
	public void iterate(Node root){
		if(root.getLeft() != null){
			iterate(root.getLeft());
		}
		System.out.println(root.getValue());
		if(root.getRight() != null){
			iterate(root.getRight());
		}
	}
	public void addNode(int n){
		if(n<value){
			if(left != null){
				left.addNode(n);
			}
			else{
				left = new Node(n,null,null);
			}
		}
		else{
			if(right != null){
				right.addNode(n);
			}
			else{
				right = new Node(n,null,null);
			}
		}
	}
	public static void main(String [] args){
		 int[] arr = new int[]{23,54,1,65,9,3,100};
		 Node  root = new Node(arr[0], null,null);
		 for(int i:arr){
			 root.addNode(i);
		 }
		 root.iterate(root);
	}
}
