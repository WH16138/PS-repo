import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int A, B, C, T;
        int charge = 0;
        A = input.nextInt();
        B = input.nextInt();
        C = input.nextInt();
        T = input.nextInt();

        T -= 30;
        charge += A;
        if (T>0)
        {
            charge += ((T+B-1)/B)*C;
        }
        System.out.println(charge);
    }
}