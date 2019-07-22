package d07;

import java.util.*;
import java.io.*;

public class p1230 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11; tc++) {
			ArrayList<Integer> arr = new ArrayList<>();
			int n = Integer.parseInt(br.readLine());
			String[] strInput = br.readLine().split("\\s");
			for(int i = 0; i < n; i++) {
				arr.add(Integer.parseInt(strInput[i]));
			}
			int commCnt = Integer.parseInt(br.readLine());
			String[] command = br.readLine().split("\\s");
			int idx = 0;
			int x, y;
			while(idx < command.length) {
				x = Integer.parseInt(command[idx + 1]);
				y = Integer.parseInt(command[idx + 2]);
				if(command[idx].charAt(0) == 'I') {
					idx += 3;
					for(int i = idx; i < idx + y; i++) {
						arr.add(x, Integer.parseInt(command[i]));
						x++;
					}
					idx += y;
				} else if(command[idx].charAt(0) == 'D') {
					idx += 3;
					for(int i = 0; i < y; i++) {
						arr.remove(x);
					}
				} else {
					idx += 2;
					for(int i = idx; i < idx + x; i++) {
						arr.add(Integer.parseInt(command[i]));
					}
					idx += x;
				}
			}
			int cnt;
			if(arr.size() > 10) {
				cnt = 10;
			} else {
				cnt = arr.size();
			}
			System.out.print("#" + tc + " ");
			for(int i = 0; i < cnt; i++) {
				System.out.print(arr.get(i) + " ");
			}
			System.out.println();
		}
	}

}
