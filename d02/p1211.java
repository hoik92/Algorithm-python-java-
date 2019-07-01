package d02;

import java.util.*;
import java.io.*;

public class p1211 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[][] ladder = new String[100][100];
		int[][] m = new int[100][100];
		
		for(int tc = 0; tc < 10; tc++) {
			int[] index = new int[100];
			int idx = -1;
			int curIdx = 0;
			int tmp = 0;
			int t = Integer.parseInt(br.readLine());
			for(int i = 0; i < 100; i++) {
				ladder[i] = br.readLine().split("\\s");
				for(int j = 0; j < 100; j ++) {
					m[i][j] = Integer.parseInt(ladder[i][j]);
					if(i == 99) {
						if(m[i][j] == 1 || m[i][j] == 2) {
							idx++;
							index[idx] = j;
						}
					}
				}
			}
			
			int result = 10000;
			int x = 0;
			for(int j = 0; j <= idx; j++) {
				int min = 0;
				curIdx = j;
				for(int i = 99; i >= 0; i--) {
					tmp = index[curIdx];
					if(tmp < 99 && m[i][tmp + 1] == 1) {
						curIdx++;
						min += index[curIdx] - tmp;
					}
					else if(tmp > 0 && m[i][tmp - 1] == 1) {
						curIdx--;
						min += tmp - index[curIdx];
					}
					if(min > result) {
						break;
					}
				}
				if(min <= result) {
					result = min;
					x = index[curIdx];
				}
			}
			System.out.println("#" + t + " " + x);
		}
	}

}
