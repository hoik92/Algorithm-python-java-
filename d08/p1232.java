package d08;

import java.util.*;
import java.io.*;

public class p1232 {
	static int[][] m;
	static String[] equ;
	
	static void postorder(int n) {
		if(n != 0) {
			postorder(m[n][0]);
			postorder(m[n][1]);
			char cal = equ[n].charAt(0);
			int tmp = 0;
			if(cal == '+' || cal == '-' || cal == '*' || cal == '/') {
				int a = Integer.parseInt(equ[m[n][0]]);
				int b = Integer.parseInt(equ[m[n][1]]);
				if(cal == '+') {
					tmp = a + b;
				} else if(cal == '-') {
					tmp = a - b;
				} else if(cal == '*') {
					tmp = a * b;
				} else if(cal == '/') {
					tmp = a / b;
				}
				equ[n] = Integer.toString(tmp);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11; tc++) {
			int N = Integer.parseInt(br.readLine());
			m = new int[N + 1][2];
			equ = new String[N + 1];
			for(int i = 0; i < N; i++) {
				String[] node = br.readLine().split("\\s");
				int idx = Integer.parseInt(node[0]);
				equ[idx] = node[1];
				if(node.length == 4) {
					int child1 = Integer.parseInt(node[2]);
					int child2 = Integer.parseInt(node[3]);
					m[idx][0] = child1;
					m[idx][1] = child2;
				}
			}
			
			postorder(1);
			String result = equ[1];
			System.out.println("#" + tc + " " + result);
		}
	}

}
