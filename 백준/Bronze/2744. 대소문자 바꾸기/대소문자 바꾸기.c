#include <stdio.h>

int main()
{
    char c;
    while ((c=getchar())!=EOF)
    {
        if ('a'<=c && c<='z')
        {
            printf("%c", c-32);
        }
        else if ('A'<=c && c<='Z')
        {
            printf("%c", c+32);
        }
    }
    return 0;
}