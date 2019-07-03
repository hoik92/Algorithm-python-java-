package d02;

import java.util.*;
import java.io.*;

public class p1209 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int tc = 1; tc < 11; tc++) {
			int t = Integer.parseInt(br.readLine());
			int[][] array = new int[100][100];
			for(int i = 0; i < 100; i++) {
				String[] strArray = br.readLine().split("\\s");
				for(int j = 0; j < 100; j++) {
					array[i][j] = Integer.parseInt(strArray[j]);
				}
			}
			
			int result = 0;
			int mat1 = 0;
			int mat2 = 0;
			for(int i = 0; i < 100; i++) {
				int sum_x = 0;
				int sum_y = 0;
				int tmp = 0;
				for(int j = 0; j < 100; j++) {
					sum_x += array[i][j];
					sum_y += array[j][i];
				}
				if(sum_x < sum_y) {
					tmp = sum_y;
				} else {
					tmp = sum_x;
				}
				if(tmp > result) {
					result = tmp;
				}
				mat1 += array[i][i];
				mat2 += array[i][99 - i];
			}
			if(mat1 > result) {
				result = mat1;
			}
			if(mat2 > result) {
				result = mat2;
			}
			System.out.println("#" + t + " " + result);
		}
	}

}
