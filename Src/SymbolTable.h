#ifndef SymbolTable
#define SymbolTable

#include <stdio.h>

//Table implementation on a linked list coz bruh,
//im not doing a hashtable in C... im rewriting
//everything in rust eventually

struct SymbolEntry
{
    int name;
    int type;
};

struct Node
{
    struct SymbolEntry data;
    struct Node *next;
};

struct Node *table = NULL;

void listInsert(struct Node *node)
{
    if (table == NULL)
    {
        table = node;
    }
    else
    {
        struct Node *t = table;
        while (t->next)
        {
            t = t->next;
        }
        t->next = node;
    }
}

void printTable()
{
    struct Node *t = table;
    while (t)
    {
        printf("Name: %d    Type: %d", t->data.name, t->data.type);
        t = t->next;
    }
}

void tableInsertion(int a, int b)
{
    struct Node * node = new Node()
    {
        /* data */
    };
    
}

#endif