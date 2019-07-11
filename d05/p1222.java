package d05;

import java.util.*;
import java.io.*;

public class p1222 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int strLen;
		String input;
		for(int tc = 1; tc < 11; tc++) {
			strLen = Integer.parseInt(br.readLine());
			input = br.readLine();
			int result = 0;
			
			for(int i = 0; i < strLen; i++) {
				if(input.charAt(i) != '+') {
					result += input.charAt(i) - '0';
				}
			}
			
			System.out.println("#" + tc + " " + result);
		}
	}

}
