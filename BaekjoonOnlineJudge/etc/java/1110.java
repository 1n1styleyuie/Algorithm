
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int num = n;
        int cnt = 0;

        while (true) {
            // 각각 십의 자리 수와 일의 자리 수 저장
            int left = num / 10;
            int right = num % 10;

            // 주어진 수의 가장 오른쪽 자리수 앞과 구한 합의 가장 오른쪽 자리 수를 이어붙이기
            num = right * 10 + (left + right) % 10;

            // cnt + 1
            cnt++;

            // 원래의 숫자로 돌아왔을 경우
            if (num == n) {
                break;
            }
        }
        System.out.println(cnt);
    }
}
