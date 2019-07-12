package d05;

import java.util.*;
import java.io.*;

class Stack {
	int top;
	String[] arr;
	String str;
	
	Stack(int len) {
		top = -1;
		arr = new String[len];
		str = "";
	}
	
	void push(String item) {
		top++;
		arr[top] = item;
	}
	
	String pop() {
		String tmp = arr[top];
		top--;
		return tmp;
	}
	
	String get() {
		return arr[top];
	}
	
	boolean isEmpty() {
		if(top == -1) {
			return true;
		}
		return false;
	}
	
	String print() {
		 for(int i = 0; i <= top; i++) {
			 str += arr[i];
		 }
		 return str;
	 }
}

public class p1223 {
	
	public static void main(String[] args) throws IOException {
		System.out.println();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11 ; tc++) {
			int strLen = Integer.parseInt(br.readLine());
			String input = br.readLine();
			Stack s1 = new Stack(strLen);
			Stack s2 = new Stack(strLen);
			
			for(int i = 0; i < strLen; i++) {
				char ch = input.charAt(i);
				if(ch != '+' && ch != '*') {
					s2.push(ch + "");
				}
				else {
					if(ch == '+') {
						while(!s1.isEmpty()) {
							s2.push(s1.pop());
						}
					} else {
						while(!s1.isEmpty() && s1.get() == '*' + "") {
							s2.push(s1.pop());
						}
					}
					s1.push(ch + "");
				}
			}
			while(!s1.isEmpty()) {
				s2.push(s1.pop());
			}
			String post = s2.print();
			int result;
			for(int i = 0; i < strLen; i++) {
				char ch = post.charAt(i);
				if(ch != '+' && ch != '*') {
					s1.push(ch + "");
				} else {
					int tmp2 = Integer.parseInt(s1.pop());
					int tmp1 = Integer.parseInt(s1.pop());
					if(ch == '+') {
						s1.push(Integer.toString(tmp1 + tmp2));
					} else {
						s1.push(Integer.toString(tmp1 * tmp2));
					}
				}
			}
			result = Integer.parseInt(s1.pop());
			System.out.println("#" + tc + " " + result);
		}
	}

}