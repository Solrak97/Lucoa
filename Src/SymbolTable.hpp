#ifndef SymbolTable
#define SymbolTable

#include <iostream>
#include <map>
#include <string>

using namespace std;

struct Entry
{
    string name;
    string type;
};


class SymbolTable
{
private:
    map<string, Entry> table;

public:
    SymbolTable();
    void tableInsertion();
}

#endif