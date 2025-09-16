// Implements a dictionary's functionality
#include<cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include<string.h>
#include<strings.h>
#include<stdio.h>
#include<stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100;
unsigned int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int value = hash(word) % N;
    node *cursor = table[value];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor -> word,word) == 0)
        {
        return true;
        }
        cursor = cursor -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    for(int i = 0; word[i] != '\0'; i++)
    {
        hash ^= tolower(word[i]);
        hash = (hash << 5) | (hash >> 27);
    }
    return hash;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if(source == NULL)
    {
        printf("Could not open : %s\n",dictionary);
        return false;
    }
    //Read each word in the file
    char buf[LENGTH + 1];
    while(fscanf(source, "%45s",buf) == 1)
    {
        node *n = malloc(sizeof(node));
        if(!n)
        {
            printf("Out of memory!\n");
            fclose(source);
            return false;
        }
        //Add each word to the hash table
        strcpy(n -> word,buf);
        int index = hash(buf) % N;
        n -> next = table[index];
        table[index] = n;
        word_count ++;

    }

    //close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i = 0;i < N; i++)
    {
        node *cursor = table[i];
        while(cursor!= NULL)
        {
            node *tmp = cursor;
            cursor = cursor -> next;
            free(tmp);
        }
        table[i] = NULL;
    }
    return true;
}
