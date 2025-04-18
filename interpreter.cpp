#include <iostream>
#include "parser.hpp"
extern int yyparse();

int main() {
    std::cout << "Nocline Drift Protocol Executor — v1.8 Alpha\n";
    yyparse();
    return 0;
}

// interpreter.hpp
class Interpreter {
public:
    void execute(ASTNode* node);
};

// interpreter.cpp
void Interpreter::execute(ASTNode* node) {

::contentReference[oaicite:27]{index=27}
 
