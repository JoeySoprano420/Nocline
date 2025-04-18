#pragma once
#include <string>
#include <memory>
#include <vector>

class ASTNode {
public:
    virtual ~ASTNode() = default;
    virtual void execute() = 0;
};

class DefineNode : public ASTNode {
    std::string name, type;
public:
    DefineNode(std::string n, std::string t) : name(n), type(t) {}
    void execute() override;
};

class AssignNode : public ASTNode {
    std::string name;
    std::shared_ptr<ASTNode> value;
public:
    AssignNode(std::string n, ASTNode* v) : name(n), value(v) {}
    void execute() override;
};

class ActionNode : public ASTNode {
    std::string name;
public:
    ActionNode(std::string n) : name(n) {}
    void execute() override;
};

class IfNode : public ASTNode {
    std::shared_ptr<ASTNode> condition, body;
public:
    IfNode(ASTNode* cond, ASTNode* b) : condition(cond), body(b) {}
    void execute() override;
};

// Add more node types: IfElseNode, LoopNode, ReturnNode, etc.

class IntLiteral : public ASTNode {
    int value;
public:
    IntLiteral(int v) : value(v) {}
    void execute() override;
};

// Same for FloatLiteral, StringLiteral, VarRef, etc.
