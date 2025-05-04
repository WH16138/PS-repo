#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* infix_to_postfix(char* exp);

int precedence(char op) 
{
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

int main()
{
    char input[101];

    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0';
    
    char *posfix = infix_to_postfix(input);
    printf("%s",posfix);

    return 0;
}

int is_operator(char c) {return (c=='+'||c=='-'||c=='*'||c=='/');}

char* infix_to_postfix(char* exp) 
{
    char* output = (char*)malloc((strlen(exp) + 1) * sizeof(char));
    char oper[100];
    int top_oper = -1;
    int out_idx = 0;

    for (int i = 0; exp[i] != '\0'; i++) 
    {
        char c = exp[i];

        if (isspace(c)) continue;

        if (isalnum(c)) 
        {
            output[out_idx++] = c;
        }
        else if (c == '(') 
        {
            oper[++top_oper] = c;
        }
        else if (c == ')') 
        {
            while (top_oper >= 0 && oper[top_oper] != '(') 
            {
                output[out_idx++] = oper[top_oper--];
            }
            if (top_oper >= 0 && oper[top_oper] == '(') top_oper--;
        }
        else if (is_operator(c)) 
        {
            while (top_oper >= 0 && precedence(oper[top_oper]) >= precedence(c)) 
            {
                if (oper[top_oper] == '(') break;
                output[out_idx++] = oper[top_oper--];
            }
            oper[++top_oper] = c;
        }
    }

    while (top_oper >= 0) 
    {
        if (oper[top_oper] != '(')
            output[out_idx++] = oper[top_oper];
        top_oper--;
    }

    output[out_idx] = '\0';
    return output;
}