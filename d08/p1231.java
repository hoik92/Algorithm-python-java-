package d08;

import java.util.*;
import java.io.*;

public class p1231 {
	static int[][] m;
	static String[] alpha;
	
	static void inorder(int n) {
		if(n != 0) {
			inorder(m[n][0]);
			System.out.print(alpha[n]);
			inorder(m[n][1]);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11; tc++) {
			int N = Integer.parseInt(br.readLine());
			m = new int[N + 1][2];
			alpha = new String[N + 1];
			
			for(int i = 0; i < N; i++) {
				String[] node = br.readLine().split("\\s");
				int idx = Integer.parseInt(node[0]);
				if(node.length == 3) {
					int child = Integer.parseInt(node[2]);
					m[idx][0] = child;
				} else if(node.length == 4) {
					int child1 = Integer.parseInt(node[2]);
					int child2 = Integer.parseInt(node[3]);
					m[idx][0] = child1;
					m[idx][1] = child2;
				}
				alpha[idx] = node[1];
			}
			
			System.out.print("#" + tc + " ");
			inorder(1);
			System.out.println();
		}
	}

}
