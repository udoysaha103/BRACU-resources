%option noyywrap

%{
    
#include<bits/stdc++.h>
using namespace std;

ofstream yyoutlog; //output filestream for log file

string loglist = ""; //list of tokens along with line numbers

// define necessary C++ variables and functions here (if any)
int lines = 1; //to keep track of line numbers

%}

/* Regular Definitions */

delim [ \t\n]

/* write regular expressions for whitespace and newline */
ws     {delim}+
newline \n

letter [a-zA-Z]
digit [0-9]

/* write regular expressions for id, float, and integers */

id     {letter}({letter}|{digit})*
if     "if"
range  "range"

%%

{ws} { /* ignore whitespace */ }

{newline} {
    lines++;
}

{id} {
    loglist = "Line no " + to_string(lines) + ": Token <ID> Lexeme " + yytext + " found" + "\n" + "\n";
    yyoutlog << loglist;
}

if {
    loglist = "Line no " + to_string(lines) + ": Token <IF> Lexeme " + yytext + " found" + "\n" + "\n";
    yyoutlog << loglist;
}

range {
    loglist = "Line no " + to_string(lines) + ": Token <RANGE> Lexeme " + yytext + " found" + "\n" + "\n";
    yyoutlog << loglist;
}

("+"|"-") { /* to match two same operators use | */
    loglist = "Line no " + to_string(lines) + ": Token <ADDOP> Lexeme " + yytext + " found" + "\n" + "\n";
    yyoutlog << loglist;
}

%%

int main(int argc, char *argv[])
{
    if (argc != 2) //check if the file name is given
    {
        cout << "Please input file name" << endl;
        return 0;
    }

    yyin = fopen(argv[1], "r"); //the file to be read must be assigned to yyin

    yyoutlog.open("my_log.txt", ios::trunc); // remember to rename the log file as mentioned in the spec

    if (yyin == NULL) // file does not exist
    {
        // print an error message and exit
        cout << "Error: File not found." << endl;
        return 1;
    }

    yylex(); // start reading the input file in a loop

    // print the total number of lines found in the input file
    cout << "Total lines: " << lines << endl;

    yyoutlog.close(); // close the log file
    fclose(yyin);     // close the input file
}
