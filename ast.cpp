// ast.hpp
class ASTNode {
public:
    virtual ~ASTNode() {}
    virtual void execute() = 0;
};

class IntegerLiteral : public ASTNode {
    int value;
public:
    IntegerLiteral(int val) : value(val) {}
    void execute() override {
        // Implementation for executing an integer literal
    }
};

class Assignment : public ASTNode {
    std::string variableName;
    ASTNode* expression;
public:
    Assignment(const std::string& name, ASTNode* expr)
        : variableName(name), expression(expr) {}
    void execute() override {
        // Implementation for executing an assignment
    }
};

// Define other AST node classes as needed
