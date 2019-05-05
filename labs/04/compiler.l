%{
#include <stdio.h>
#include "y.tab.h"
extern int yylval;
%}

%%
p                               {return printdcl; }
i                               {return intdcl; }
f                               {return floatdcl; }
[a-eghj-oq-z]+                  { return id; }
[0-9]+                          { return inum; }
[0-9]+"."[0-9]+                 { return fnum; }
=                               { yylval = (yytext); return assign; }
\+                              { yylval = (yytext); return addition; }
\-                              { yylval = (yytext); return minus; }
\*                              { yylval = (yytext); return multiplication; }
\/                              { yylval = (yytext); return division; }
\/\/.*[\n]                      { /* Is a comment, ignore it */ }
[ \t]                           { /* Is a whitespace, ignore it */ }
\n                              { return AT; }
<<EOF>>                         { return newline;} 
%%

int yywrap (void)
{return 1;}