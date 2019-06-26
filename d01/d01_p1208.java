package d01;

import java.util.*;
import java.io.*;

public class d01_p1208 {
	static int N = 100;
	public static int[] findMinMax(int[] array) {
		int minVal = array[0];
		int maxVal = array[0];
		int minIdx = 0;
		int maxIdx = 0;
		for(int i = 1; i < N; i++) {
			if(array[i] > maxVal) {
				maxVal = array[i];
				maxIdx = i;
			}
			else if(array[i] < minVal) {
				minVal = array[i];
				minIdx = i;
			}
		}
		int[] result = new int[2];
		result[0] = minIdx;
		result[1] = maxIdx;
		return result;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int tc = 1; tc < 11; tc++) {
			int dump = Integer.parseInt(br.readLine());
			int[] box = new int[N];
			String[] boxString = br.readLine().split("\\s");
			for(int i = 0; i < N; i++) {
				box[i] = Integer.parseInt(boxString[i]);
			}
			
			for(int i = 0; i < dump; i++) {
				int[] minmax = findMinMax(box);
				int minIdx = minmax[0];
				int maxIdx = minmax[1];
				box[minIdx] += 1;
				box[maxIdx] -= 1;
			}
			int[] minmax = findMinMax(box);
			System.out.println("#" + tc + " " + (box[minmax[1]] - box[minmax[0]]));
		}
	}

}
