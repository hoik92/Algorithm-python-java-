package d03;

import java.util.*;
import java.io.*;

public class p1215 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] m = new String[8];
		boolean find;
		int result;
		
		for(int tc = 1; tc < 11; tc++) {
			int n = Integer.parseInt(br.readLine());
			int nn = n / 2;
			for(int i = 0; i < 8; i++) {
				m[i] = br.readLine();
			}
			
			result = 0;
			for(int i = 0; i < 8; i++) {
				for(int j = 0; j < 9 - n; j++) {
					find = true;
					for(int k = 0; k < nn; k++) {
						if(m[i].charAt(j + k) != m[i].charAt(j + n - 1 - k)) {
							find = false;
							break;
						}
					}
					if(find) {
						result++;
					}
				}
				for(int j = 0; j < 9 - n; j++) {
					find = true;
					for(int k = 0; k < nn; k++) {
						if(m[j + k].charAt(i) != m[j + n - 1 - k].charAt(i)) {
							find = false;
							break;
						}
					}
					if(find) {
						result++;
					}
				}
			}
			System.out.println("#" + tc + " " + result);
		}
	}

}
