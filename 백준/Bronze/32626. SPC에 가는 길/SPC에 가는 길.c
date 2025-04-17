#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

int main()
{
    int sx,sy,ex,ey,px,py;
    scanf("%d %d %d %d %d %d",&sx,&sy,&ex,&ey,&px,&py);
    if (sx==ex)
    {
        if (px==sx && MIN(sy,ey)<py && py<MAX(sy,ey))
        {
            if (sy==ey)
            {
                printf("0");
            } else {
                printf("2");
            }
        } else {
            printf("0");
        }
    } else if (sy==ey) {
        if (py==sy && MIN(sx,ex)<px && px<MAX(sx,ex))
        {
            printf("2");
        } else {
            printf("0");
        }
    } else {
        printf("1");
    }
    return 0;
}