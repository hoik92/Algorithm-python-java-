package d04;

import java.util.*;
import java.io.*;

public class p1217 {
	static int squ(int n, int cnt, int end) {
		if(cnt == end) {
			return 1;
		}
		return n * squ(n, cnt + 1, end);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t;
		String[] strNM;
		int N, M;
		int result;
		
		for(int tc = 0; tc < 10; tc++) {
			t = Integer.parseInt(br.readLine());
			strNM = br.readLine().split("\\s");
			N = Integer.parseInt(strNM[0]);
			M = Integer.parseInt(strNM[1]);
			
			result = squ(N, 0, M);
			System.out.println("#" + t + " " + result);
		}
	}

}
