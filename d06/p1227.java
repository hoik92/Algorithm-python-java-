package d06;

import java.util.*;
import java.io.*;

public class p1227 {
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int[][] m = new int[100][100];
	static int startx, starty;
	static int[][] visited = new int[100][100];
	static int result;
	
	static void dfs(int x, int y) {
		if(m[x][y] == 3) {
			result = 1;
			return;
		}
		
		for(int i = 0; i < 4; i++) {
			int tmpx = x + dx[i];
			int tmpy = y + dy[i];
			if(tmpx >= 0 && tmpx < 100 && tmpy >= 0 && tmpy < 100 && m[tmpx][tmpy] != 1 && visited[tmpx][tmpy] != 1) {
				visited[tmpx][tmpy] = 1;
				dfs(tmpx, tmpy);
				visited[tmpx][tmpy] = 0;
				if(result == 1) {
					return;
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int tc = 0; tc < 10; tc++) {
			int t = Integer.parseInt(br.readLine());
			for(int i = 0; i < 100; i++) {
				String s = br.readLine();
				for(int j = 0; j < 100; j++) {
					m[i][j] = s.charAt(j) - '0';
					if(m[i][j] == 2) {
						startx = i;
						starty = j;
					}
				}
			}
			result = 0;
			visited[startx][starty] = 1;
			dfs(startx, starty);
			
			System.out.println("#" + t + " " + result);
		}
	}

}
