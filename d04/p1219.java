package d04;

import java.util.*;
import java.io.*;

public class p1219 {
	static int[] visited = new int[100];
	static int result;
	
	static void dfs(int start, int end, int cur, int[][] map) {
		if(cur == end) {
			result = 1;
			return;
		}
		
		for(int i = 0; i < 100; i++) {
			if(map[cur][i] == 1 && visited[i] != 1) {
				visited[i] = 1;
				dfs(start, end, i, map);
				visited[i] = 0;
			}
			if(result == 1) {
				return;
			}
		}
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] tcAndLength;
		String[] input;
		int t;
		int leng;
		
		for(int tc = 0; tc < 10; tc++) {
			result = 0;
			int[][] m = new int[100][100];
			tcAndLength = br.readLine().split("\\s");
			t = Integer.parseInt(tcAndLength[0]);
			leng = Integer.parseInt(tcAndLength[1]);
			
			input = br.readLine().split("\\s");
			for(int i = 0; i < leng; i++) {
				int start = Integer.parseInt(input[2 * i]);
				int end = Integer.parseInt(input[2 * i + 1]);
				m[start][end] = 1;
			}
			
			visited[0] = 1;
			dfs(0, 99, 0, m);
			
			System.out.println("#" + t + " " + result);
		}
	}

}
