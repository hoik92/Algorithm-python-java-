package d08;

import java.util.*;
import java.io.*;

public class p1233 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11; tc++) {
			int N = Integer.parseInt(br.readLine());
			int result = 1;
			
			for(int i = 0; i < N; i++) {
				String[] node = br.readLine().split("\\s");
				char cal = node[1].charAt(0);
				if(node.length == 2 && (cal == '+' || cal == '-' || cal == '*' || cal == '/')) {
					result = 0;
				} else if(node.length > 2 && (cal != '+' && cal != '-' && cal != '*' && cal != '/')) {
					result = 0;
				}
			}
			System.out.println("#" + tc + " " + result);
		}
	}

}
