%{
#include "parser.hpp"
%}

%%

"define"        { return DEFINE; }
"assign"        { return ASSIGN; }
"action"        { return ACTION; }
"trigger"       { return TRIGGER; }
"if"            { return IF; }
"else"          { return ELSE; }
"loop"          { return LOOP; }
"return"        { return RETURN; }
"import"        { return IMPORT; }
"export"        { return EXPORT; }
"cast"          { return CAST; }
"enable"        { return ENABLE; }
"disable"       { return DISABLE; }
"register"      { return REGISTER; }
"allocate"      { return ALLOCATE; }
"bypass"        { return BYPASS; }
"invoke"        { return INVOKE; }
"mark"          { return MARK; }
"frame"         { return FRAME; }
"resolve"       { return RESOLVE; }
"sync"          { return SYNC; }
"pause"         { return PAUSE; }
"resume"        { return RESUME; }

[0-9]+          { yylval.intVal = atoi(yytext); return INTEGER; }
\"[^\"]*\"      { yylval.strVal = strdup(yytext); return STRING; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.strVal = strdup(yytext); return IDENTIFIER; }

"=="            { return EQ; }
"!="            { return NEQ; }
"->"            { return ARROW; }
"=>"            { return IMPLIES; }
"::"            { return SCOPE; }
".."            { return RANGE; }
"++"            { return INC; }
"--"            { return DEC; }
"+="            { return PLUS_ASSIGN; }
"-="            { return MINUS_ASSIGN; }
"&&"            { return AND; }
"||"            { return OR; }
"!"             { return NOT; }
"?"             { return QUESTION; }
"~"             { return TILDE; }
"#"             { return HASH; }
"@"             { return AT; }
"$"             { return DOLLAR; }
"%"             { return MOD; }
"*"             { return ASTERISK; }
"/"             { return SLASH; }
"\\"            { return BACKSLASH; }
"^"             { return CARET; }

[ \t\r\n]+      { /* Skip whitespace */ }

.               { /* Handle unexpected characters */ }

%%
