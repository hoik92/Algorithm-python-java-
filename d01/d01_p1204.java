package d01;

import java.util.Scanner;

public class d01_p1204 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		for(int i = 1; i <= T; i++) {
			int tc = s.nextInt();
			int[] scoreCnt = new int[101];
			int maxCnt = 0; // 가장 높은 빈도수
			int maxScore = 0; // 가장 높은 빈도수 중 가장 높은 점수
			for(int j = 0; j < 1000; j++) {
				int score = s.nextInt(); // 점수
				scoreCnt[score] += 1; // 점수에 대한 빈도수 1 증가
				if(scoreCnt[score] >= maxCnt) { // 해당 점수에 대한 빈도수가 가장 높은 빈도수보다 크면
					if(scoreCnt[score] == maxCnt && score > maxScore) {
						maxScore = score;
					}
					else if(scoreCnt[score] > maxCnt) {
						maxScore = score;
					}
					maxCnt = scoreCnt[score]; // 빈도수 최신화
				}
			}
			System.out.println("#" + tc + " " + maxScore); 
		}
	}

}