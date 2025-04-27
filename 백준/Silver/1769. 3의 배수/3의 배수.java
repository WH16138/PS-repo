import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        String n = input.next();
        int cnt = 0;
        int s;
        while (n.length() > 1)
        {
            cnt ++;
            s = 0;
            for (int i = 0; i < n.length(); i++){
                s += Character.getNumericValue(n.charAt(i));
            }
            n = String.valueOf(s);
        }
        System.out.println(cnt);
        System.out.println((Integer.parseInt(n)%3==0) ? "YES":"NO");
    }
}
