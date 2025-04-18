%{
#include "ast.hpp"
%}

%union {
    int intVal;
    char* strVal;
    ASTNode* node;
}

%token <intVal> INTEGER
%token <strVal> STRING IDENTIFIER
%token DEFINE ASSIGN ACTION TRIGGER IF ELSE LOOP RETURN
%token IMPORT EXPORT CAST ENABLE DISABLE REGISTER ALLOCATE
%token BYPASS INVOKE MARK FRAME RESOLVE SYNC PAUSE RESUME
%token EQ NEQ ARROW IMPLIES SCOPE RANGE INC DEC PLUS_ASSIGN
%token MINUS_ASSIGN AND OR NOT QUESTION TILDE HASH AT DOLLAR
%token MOD ASTERISK SLASH BACKSLASH CARET

%type <node> statement expression

%%

program:
    /* Define the structure of the program */
    ;

statement:
    DEFINE IDENTIFIER ':' IDENTIFIER
    {
        /* Handle variable/function/type definition */
    }
    | ASSIGN IDENTIFIER '=' expression
    {
        /* Handle assignment */
    }
    | ACTION IDENTIFIER '(' ')'
    {
        /* Handle action invocation */
    }
    | IF expression ':' statement
    {
        /* Handle if statement */
    }
    | IF expression ':' statement ELSE ':' statement
    {
        /* Handle if-else statement */
    }
    ;

expression:
    INTEGER
    {
        /* Handle integer literal */
    }
    | STRING
    {
        /* Handle string literal */
    }
    | IDENTIFIER
    {
        /* Handle variable reference */
    }
    | expression '+' expression
    {
        /* Handle addition */
    }
    ;

%%
