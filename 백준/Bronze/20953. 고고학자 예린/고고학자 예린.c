int dolmen(int a, int b) {
    int sum;
    sum = (int)((a+b-1)*(a+b)/2*(a+b));
    return sum;
}

int main() {
    int T,a,b;
    scanf("%d",&T);
    for (int i = 0; i < T; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", dolmen(a,b));
    }
}