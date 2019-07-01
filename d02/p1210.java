package d02;

import java.util.*;
import java.io.*;

public class p1210 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] strArray = new String[100];
		int[][] array = new int[100][100];
		int[] index = new int[100];
		for(int tc = 0; tc < 10; tc++) {
			int t = Integer.parseInt(br.readLine());
			int idx = -1;
			int startIdx = 0;
			for(int i = 0; i < 100; i++) {
				strArray = br.readLine().split("\\s");
				for(int j = 0; j < 100; j++) {
					array[i][j] = Integer.parseInt(strArray[j]);
				}
				if(i == 99) {
					for(int j = 0; j < 100; j++) {
						if(array[i][j] == 2 || array[i][j] == 1) {
							idx++;
							index[idx] = j;
							if(array[i][j] == 2) {
								startIdx = idx;
							}
						}
					}
				}
			}
			for(int i = 99; i >= 0; i--) {
				if(index[startIdx] > 0 && array[i][index[startIdx] - 1] == 1) {
					startIdx--;
				}
				else if(index[startIdx] < 99 && array[i][index[startIdx] + 1] == 1) {
					startIdx++;
				}
			}
			System.out.println("#" + t + " " + index[startIdx]);
		}
	}

}
