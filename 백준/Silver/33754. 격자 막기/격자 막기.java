import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] a = new int[n];

        int min = 2;

        for (int i = 0; i < n; i++)
        {
            a[i] = input.nextInt();
            if (a[i] == 0)
                min = 1;
        }

        for (int i = 0; i < n; i++)
        {
            if (input.nextInt() == 0)
            {
                if (a[i]==0 || i>0 && a[i-1]==0 || a[i+1]==0 && i<n-1)
                {
                    min = 0;
                }
            }
        }

        System.out.println(min);
    }
}