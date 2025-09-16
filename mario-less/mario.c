#include<cs50.h>
#include<stdio.h>

void brick(int n);
void print_row(int spaces,int bricks);
int main(void)
{
    int height;
    do
    {
        height = get_int("Enter Height:");
    }
    while (height < 1 || height > 8);
    brick(height);
}
void brick(int n)
{
    for(int i = 0;i < n;i++)
    print_row(i+1,n);
}
void print_row(int spaces,int bricks)
{
    for (int i = 0;i< bricks-spaces;i++)
    printf(" ");
    for (int i = 0;i<spaces;i++)
    printf("#");
    printf("  ");
    for(int i = 0;i<spaces;i++)
    printf("#");
printf("\n");
}

