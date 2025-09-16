#include<cs50.h>
#include<ctype.h>
#include<math.h>
#include<stdio.h>
#include<string.h>

int count_letters(string s);
int count_words(string s);
int count_sentences(string s);
float compute_readability(float l,float s);


int main(void)
{
    string text = get_string("Text:");
    int count_l = count_letters(text);
    int count_w = count_words(text);
    int count_s = count_sentences(text);
    float average_l = ((float)count_l / count_w) * 100;
    float average_s = ((float)count_s / count_w) * 100;
    float index = compute_readability(average_l,average_s);
    //printf("Letters: %i\nWords: %i\nSentences: %i\nReadability: %.3f\n",count_l,count_w,count_s,index);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if(index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n",(int)round(index));
    }

}

int count_letters(string s)
{
    int letters_count = 0;
    for (int i = 0,len = strlen(s);i < len; i ++)
    {
        if (isalpha(s[i]))
        {
            letters_count += 1;
        }
    }
    return letters_count;
}
int count_words(string s)
{
    int word_count = 1;
    for (int i = 0,len = strlen(s);i < len; i++)
    {
        if (isblank(s[i]))
        {
            word_count += 1;
        }
    }
    return word_count;
}
int count_sentences(string s)
{
    int sentence_count = 0;
    for(int i = 0,len = strlen(s);i < len; i++)
    {
        if(s[i] == '.')
        {
            sentence_count += 1;
        }
    }
    return sentence_count;
}
float compute_readability(float l,float s)
{
    float index = (0.0588 * l) - (0.296 * s) - 15.8;
    return index;
}

