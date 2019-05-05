%{
#include <stdio.h>
%}
%start program
%token inum fnum id printdcl intdcl floatdcl end

%token assign addition minus multiplication division

%token newline
%%

program: asignacion newline {printf("asignacion %s",$$);}
    | declaration {printf($$);}
    | print {printf("print");}
    | end {printf("end\n");return 0;}
    ;

num: inum {$$ = "inum";}
    | fnum {$$ = "fnum";}
    ;

type: intdcl {$$ = "intdlc";}
    | floatdcl {$$ = "floatdcl";}
    ;

declaration: type id {printf("%s id", $1);}
    ;

asignacion: id assign id operators num {$$ = '';}
    | id assign num
    ;

print: printdcl id {printf("printdcl %s", $1);} 
    |  printdcl num {printf("printdcl %s", $1);}
    ;

operators: multiplication { printf("multiplication %s", $1);}
    | division   	   { printf("division %s", $1);}
    | addition num { printf("addition %s", $1);}
    | minus num    { printf("minus %s", $1);}
    ;

%%

int main(int argc, char **argv) {
    FILE    *fd;
    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyset_in(fd);
        yylex();
        fclose(fd);
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}