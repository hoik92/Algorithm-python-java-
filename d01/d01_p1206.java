package d01;

import java.util.*;
import java.io.*;

public class d01_p1206 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = 10;
		for(int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			String[] inputString = br.readLine().split("\\s");
			int[] m = new int[N];
			for(int i = 0; i < N; i++) {
				m[i] = Integer.parseInt(inputString[i]);
			}
			
			int result = 0;
			for(int i = 2; i < N - 2; i++) {
				if(m[i] > m[i-1] && m[i] > m[i-2] && m[i] > m[i+1] && m[i] > m[i+2]) {
					int tmp = m[i] - m[i - 2];
					for(int j = -2; j < 3; j++) {
						if(j != 0 && m[i] - m[i + j] < tmp) {
							tmp = m[i] - m[i + j];
						}
					}
					result += tmp;
				}
			}
			System.out.println("#" + tc + " " + result);
		}
	}

}
