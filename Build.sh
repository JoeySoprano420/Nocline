flex nocline.l
bison -d nocline.y
g++ -o nocline nocline.tab.c lex.yy.c ast.cpp interpreter.cpp main.cpp -std=c++17
