#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
#include <stdbool.h>
#include<stdlib.h>

bool only_digits(string s);
char rotate(char c,int n);

int main(int argc,string argv[])
{
    if (argc !=2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int key;
    string plaintext = get_string("plainText: ");
    char ciphertext[strlen(plaintext)+1];
    key = atoi(argv[1]);
    for (int i = 0,len = strlen(plaintext);i< len;i++)
    {
        ciphertext[i] = rotate(plaintext[i],key);
    }
    ciphertext[strlen(plaintext)] = '\0';
    printf("ciphertext: %s\n",ciphertext);
    return 0;
}


bool only_digits(string s)
{
    for (int i =0,len = strlen(s);i<len;i++)
    {
        if(!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c,int n)
{
    if (isalpha(c))
    {
        if(isupper(c))
        {
            return ((c - 'A' + n ) % 26) + 'A';
        }
        else if(islower(c))
        {
            return ((c - 'a' + n) % 26) + 'a';
        }
    }
    return c;
}
