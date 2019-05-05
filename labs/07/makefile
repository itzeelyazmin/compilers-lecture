@all:
	yacc -d cfgYacc.y
	lex compiler.l
	gcc lex.yy.c y.tab.c -o output
	./output prueba.txt
clean:
	rm -rf *.c
	rm -rf *.h