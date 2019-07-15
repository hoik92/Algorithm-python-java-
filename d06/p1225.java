package d06;

import java.util.*;
import java.io.*;

public class p1225 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc = 1; tc < 11; tc++) {
			int t = Integer.parseInt(br.readLine());
			String[] strInput = br.readLine().split("\\s");
			int[] input = new int[8];
			CirQ q = new CirQ(8);
			for(int i = 0; i < 8; i++) {
				input[i] = Integer.parseInt(strInput[i]);
				q.enQ(input[i]);
			}
			
			int[] result;
			int cycle = 0;
			while(true) {
				int tmp = q.deQ();
				cycle++;
				if(cycle == 6) {
					cycle = 1;
				}
				tmp -= cycle;
				if(tmp < 0) {
					tmp = 0;
				}
				q.enQ(tmp);
				if(tmp == 0) {
					result = q.out();
					break;
				}
			}
			
			System.out.print("#" + t + " ");
			for(int i = 0; i < 8; i++) {
				System.out.print(result[i] + " ");
			}
			System.out.println();
		}
	}

}
class CirQ {
	int[] que;
	int head;
	int rear;
	int len;
	
	CirQ(int n) {
		len = n;
		que = new int[len + 1];
		head = -1;
		rear = -1;
	}
	
	boolean isEmpty() {
		if(head == rear) {
			return true;
		}
		return false;
	}
	
	boolean isFull() {
		if((rear + 2) % (len + 1) == head) {
			return true;
		}
		return false;
	}
	
	void enQ(int item) {
		if(!isFull()) {
			rear = (rear + 1) % (len + 1);
			que[rear] = item;
			if(head == -1) {
				head++;
			}
		}
	}
	
	int deQ() {
		if(!isEmpty()) {
			int item = que[head];
			head = (head + 1) % (len + 1);
			return item;
		}
		return 0;
	}
	
	int[] out() {
		int[] output = new int[len];
		for(int i = 0; i < len; i++) {
			int idx = (head + i) % (len + 1);
			output[i] = que[idx];
		}
		return output;
	}
}
