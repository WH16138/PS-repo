import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++)
        {
            long n = input.nextLong();
            long e = 8888888888888888888L;
            long cnt = 0;
            while (e != 0)
            {
                cnt += n / e;
                n -= (n/e)*e;
                e /= 10;
            }
            if (cnt <= 8 && n == 0)
                System.out.println("Yes");
            else
                System.out.println("No");
        }

    }
}