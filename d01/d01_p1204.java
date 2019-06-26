package d01;

import java.util.Scanner;

public class d01_p1204 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		for(int i = 1; i <= T; i++) {
			int tc = s.nextInt();
			int[] scoreCnt = new int[101];
			int maxCnt = 0; // ���� ���� �󵵼�
			int maxScore = 0; // ���� ���� �󵵼� �� ���� ���� ����
			for(int j = 0; j < 1000; j++) {
				int score = s.nextInt(); // ����
				scoreCnt[score] += 1; // ������ ���� �󵵼� 1 ����
				if(scoreCnt[score] >= maxCnt) { // �ش� ������ ���� �󵵼��� ���� ���� �󵵼����� ũ��
					if(scoreCnt[score] == maxCnt && score > maxScore) {
						maxScore = score;
					}
					else if(scoreCnt[score] > maxCnt) {
						maxScore = score;
					}
					maxCnt = scoreCnt[score]; // �󵵼� �ֽ�ȭ
				}
			}
			System.out.println("#" + tc + " " + maxScore); 
		}
	}

}