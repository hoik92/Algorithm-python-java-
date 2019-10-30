//https://programmers.co.kr/learn/courses/30/lessons/42840?language=java

package programmers_java;

import java.util.*;

public class p42840 {
	public static int[] solution(int[] answers) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int len_a = 5;
        int len_b = 8;
        int len_c = 10;
        int[] result = {0, 0, 0};
        for(int i=0; i<answers.length; i++){
            if(answers[i] == a[i % len_a]) {
                result[0]++;
            }
            if(answers[i] == b[i % len_b]) {
                result[1]++;
            }
            if(answers[i] == c[i % len_c]) {
                result[2]++;
            }
        }
        // System.out.println(Arrays.toString(result));
        int max_val = result[0];
        for(int i=1; i<3; i++) {
            if(result[i] > max_val) {
                max_val = result[i];
            }
        }
        ArrayList<Integer> results = new ArrayList<>();
        for(int i=0; i<3; i++) {
            if(result[i] == max_val) {
                results.add(i + 1);
            }
        }
        int[] answer = new int[results.size()];
        for(int i=0; i<results.size(); i++) {
            answer[i] = results.get(i);
        }
        return answer;
    }
	
	public static void main(String[] args) {
		int[] answer = {1, 2, 3, 4, 5};
		int[] result = solution(answer);
		System.out.println(Arrays.toString(result));
	}

}
