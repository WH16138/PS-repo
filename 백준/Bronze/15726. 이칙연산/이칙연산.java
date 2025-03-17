import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();
        
        if (b>c)
        {
            System.out.println((int)(a*b/c));
        } else {
            System.out.println((int)(a/b*c));
        }
    }
}
