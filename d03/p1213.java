package d03;

import java.util.*;
import java.io.*;

public class p1213 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		boolean find;
		for(int tc = 1; tc < 11; tc++) {
			int t = Integer.parseInt(br.readLine());
			String word = br.readLine();
			String total = br.readLine();
			int index = word.length() - 1;
			int result = 0;
			while(index < total.length()) {
				find = true;
				if(word.charAt(word.length() - 1) != total.charAt(index)) {
					find = false;
					for(int i = 0; i < word.length(); i++) {
						if(word.charAt(word.length() - 1 - i) == total.charAt(index)) {
							index += i - 1;
							break;
						}
					}
				} else {
					for(int i = 0; i < word.length(); i++) {
						if(word.charAt(word.length() - 1 - i) != total.charAt(index - i)) {
							find = false;
							break;
						}
					}
				}
				if(find) {
					result++;
				}
				index++;
			}
			System.out.println("#" + t + " " + result);
		}
	}

}
