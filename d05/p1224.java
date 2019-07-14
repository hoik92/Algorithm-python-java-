package d05;

import java.util.*;
import java.io.*;

public class p1224 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11; tc++) {
			int len = Integer.parseInt(br.readLine());
			String input = br.readLine();
			ArrayList<String> stack = new ArrayList<>();
			String post = "";
			
			for(int i = 0; i < len; i++) {
				char ch = input.charAt(i);
				if(ch == '(') {
					stack.add(ch + "");
				} else if(ch == ')') {
					while(stack.get(stack.size() - 1).charAt(0) != '(') {
						post += stack.remove(stack.size() - 1);
					}
					stack.remove(stack.size() - 1);
				} else if(ch == '+') {
					while(stack.get(stack.size() - 1).charAt(0) == '+' || stack.get(stack.size() - 1).charAt(0) == '*') {
						post += stack.remove(stack.size() - 1);
					}
					stack.add(ch + "");
				} else if(ch == '*') {
					while(stack.get(stack.size() - 1).charAt(0) == '*') {
						post += stack.remove(stack.size() - 1);
					}
					stack.add(ch + "");
				} else {
					post += ch;
				}
			}
			while(stack.size() != 0) {
				post += stack.remove(stack.size() - 1);
			}
			for(int i = 0; i < post.length(); i++) {
				char ch = post.charAt(i);
				if(ch != '+' && ch != '*') {
					stack.add(ch + "");
				} else {
					int tmp2 = Integer.parseInt(stack.remove(stack.size() - 1));
					int tmp1 = Integer.parseInt(stack.remove(stack.size() - 1));
					if(ch == '+') {
						stack.add(Integer.toString(tmp1 + tmp2));
					} else {
						stack.add(Integer.toString(tmp1 * tmp2));
					}
				}
			}
			int result = Integer.parseInt(stack.get(0));
			System.out.println("#" + tc + " " + result);
		}
	}

}
