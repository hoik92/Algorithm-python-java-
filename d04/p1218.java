package d04;

import java.util.*;
import java.io.*;

public class p1218 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N;
		int result;
		ArrayList<Character> m = new ArrayList<>();
		String str;
		char c;
		
		for(int tc = 1; tc < 11; tc++) {
			result = 1;
			m.clear();
			N = Integer.parseInt(br.readLine());
			str = br.readLine();
			for(int i = 0; i < str.length(); i++) {
				if(result == 0) {
					break;
				}
				c = str.charAt(i);
				if(c == '(' || c == '{' || c == '[' || c == '<') {
					m.add(c);
				} else {
					if(m.size() == 0) {
						result = 0;
						break;
					}
					else if((c == ')' && m.get(m.size() - 1) == '(') || (c == '}' && m.get(m.size() - 1) == '{')
							|| (c == ']' && m.get(m.size() - 1) == '[') || (c == '>' && m.get(m.size() - 1) == '<')) {
						m.remove(m.size() - 1);
					}
					else {
						result = 0;
						break;
					}
				}
			}
			if(m.size() != 0) {
				result = 0;
			}
			System.out.println("#" + tc + " " + result);
		}
	}

}
