#include "SymbolTable.hpp"

    SymbolTable::SymbolTable(){
        table = map<string, Entry>();
    }

void SymbolTable::tableInsertion(string type, string name){
    Entry node = {type, name};
    bool overwrite = Table.insert({name, node}).second;
    if (overwrite){
        Table[name] = node;
    }
}