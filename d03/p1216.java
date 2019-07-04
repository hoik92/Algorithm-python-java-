package d03;

import java.util.*;
import java.io.*;

public class p1216 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] m = new String[100];
		int t;
		int result;
		int n;
		boolean find;
		
		for(int tc = 0; tc < 10; tc++) {
			t = Integer.parseInt(br.readLine());
			for(int i = 0; i < 100; i++) {
				m[i] = br.readLine();
			}
			
			result = 1;
			for(int i = 0; i < 100; i++) { // i는 행
				for(int j = 100; j > 1; j--) { // j는 길이
					if(result > j) {
						break;
					}
					n = j / 2;
					
					for(int k = 0; k < 101 - j; k++) { // k는 열
						find = true;
						for(int l = 0; l < n; l++) {
							if(m[i].charAt(k + l) != m[i].charAt(k + j - 1 - l)) {
								find = false;
								break;
							}
						}
						if(find) {
							if(result < j) {
								result = j;
							}
							break;
						}
						
						find = true;
						for(int l = 0; l < n; l++) {
							if(m[k + l].charAt(i) != m[k + j - 1 - l].charAt(i)) {
								find = false;
								break;
							}
						}
						if(find) {
							if(result < j) {
								result = j;
							}
							break;
						}
					}
				}
			}
			System.out.println("#" + t + " " + result);
		}
	}

}
