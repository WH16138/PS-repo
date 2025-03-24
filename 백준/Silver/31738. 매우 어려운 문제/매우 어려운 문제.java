import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        long N = input.nextLong();
        long M = input.nextLong();
        if (N >= M)
        {
            System.out.println(0);
        } else {
            long p = 1;
            for (int i = 1; i <= N; i++)
            {
                p *= i;
                p %= M;
            }
            System.out.println(p);
        }
    }
}