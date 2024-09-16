%{

#include"symbol_info.h"

#define YYSTYPE symbol_info*

int yyparse(void);
int yylex(void);
void yyerror(char *s){}

extern FILE *yyin;


ofstream outlog;

int lines;

// declare any other variables or functions needed here

%}

%token IF ELSE FOR WHILE DO BREAK CONTINUE RETURN INT FLOAT CHAR VOID DOUBLE SWITCH CASE DEFAULT PRINTLN ADDOP MULOP INCOP DECOP RELOP ASSIGNOP LOGICOP NOT LPAREN RPAREN LCURL RCURL LTHIRD RTHIRD SEMICOLON COMMA ID CONST_INT CONST_FLOAT

%%

start : program
	{
		outlog<<"At line no: "<<lines+1<<" start : program "<<endl<<endl;
	}
;

program : program unit
	{
		outlog<<"At line no: "<<lines+1<<" program : program unit "<<endl<<endl;
		outlog<<$1->getname()+"\n"+$2->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"\n"+$2->getname(),"program");
	}
	| unit
	{
		outlog<<"At line no: "<<lines+1<<" program : unit "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"program");
	}
;

unit : var_declaration
	{
		outlog<<"At line no: "<<lines+1<<" unit : var_declaration "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"unit");
	
	}
	| func_definition
	{
		outlog<<"At line no: "<<lines+1<<" unit : func_definition "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"unit");
	
	}
;

func_definition : type_specifier ID LPAREN parameter_list RPAREN compound_statement
	{	
		outlog<<"At line no: "<<lines+1<<" func_definition : type_specifier ID LPAREN parameter_list RPAREN compound_statement "<<endl<<endl;
		outlog<<$1->getname()<<" "<<$2->getname()<<"("<<$4->getname()<<")\n"<<$6->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+" "+$2->getname()+"("+$4->getname()+")\n"+$6->getname(),"func_def");
	}
	| type_specifier ID LPAREN RPAREN compound_statement
	{
		
		outlog<<"At line no: "<<lines+1<<" func_definition : type_specifier ID LPAREN RPAREN compound_statement "<<endl<<endl;
		outlog<<$1->getname()<<" "<<$2->getname()<<"()\n"<<$5->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+" "+$2->getname()+"()\n"+$5->getname(),"func_def");	
	}
;

parameter_list : parameter_list COMMA type_specifier ID
	{
		outlog<<"At line no: "<<lines+1<<" parameter_list : parameter_list COMMA type_specifier ID "<<endl<<endl;
		outlog<<$1->getname()<<","<<$3->getname()<<" "<<$4->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+","+$3->getname()+" "+$4->getname(),"param_list");
	}
	| parameter_list COMMA type_specifier
	{
		outlog<<"At line no: "<<lines+1<<" parameter_list : parameter_list COMMA type_specifier "<<endl<<endl;
		outlog<<$1->getname()<<", "<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+", "+$3->getname(),"param_list");
	
	}
	| type_specifier ID
	{
		outlog<<"At line no: "<<lines+1<<" parameter_list : type_specifier ID "<<endl<<endl;
		outlog<<$1->getname()<<" "<<$2->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+" "+$2->getname(),"param_list");
	}
	| type_specifier
	{
		outlog<<"At line no: "<<lines+1<<" parameter_list : type_specifier "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"param_list");
	}
;

compound_statement : LCURL statements RCURL
	{
		outlog<<"At line no: "<<lines+1<<" compound_statement : LCURL statements RCURL "<<endl<<endl;
		outlog<<"{\n"<<$2->getname()<<"\n}"<<endl<<endl;
		
		$$ = new symbol_info("{\n"+$2->getname()+"\n}","compound_stmnt");
	}
	| LCURL RCURL
	{
		outlog<<"At line no: "<<lines+1<<" compound_statement : LCURL RCURL "<<endl<<endl;
		outlog<<"{\n}"<<endl<<endl;
		
		$$ = new symbol_info("{\n}","compound_stmnt");
	}
;

var_declaration : type_specifier declaration_list SEMICOLON
	{
		outlog<<"At line no: "<<lines+1<<" var_declaration : type_specifier declaration_list SEMICOLON "<<endl<<endl;
		outlog<<$1->getname()<<" "<<$2->getname()<<";"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+" "+$2->getname()+";","var_decl");
	}
;

type_specifier : INT
	{
		outlog<<"At line no: "<<lines+1<<" type_specifier : INT "<<endl<<endl;
		outlog<<"int"<<endl<<endl;
		
		$$ = new symbol_info("int","type_spec");
	}
	| FLOAT
	{
		outlog<<"At line no: "<<lines+1<<" type_specifier : FLOAT "<<endl<<endl;
		outlog<<"float"<<endl<<endl;
		
		$$ = new symbol_info("float","type_spec");
	}
	| VOID
	{
		outlog<<"At line no: "<<lines+1<<" type_specifier : VOID "<<endl<<endl;
		outlog<<"void"<<endl<<endl;
		
		$$ = new symbol_info("void","type_spec");
	}
;

declaration_list : declaration_list COMMA ID
	{
		outlog<<"At line no: "<<lines+1<<" declaration_list : declaration_list COMMA ID "<<endl<<endl;
		outlog<<$1->getname()<<","<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+","+$3->getname(),"decl_list");
	}
	| declaration_list COMMA ID LTHIRD CONST_INT RTHIRD
	{
		outlog<<"At line no: "<<lines+1<<" declaration_list : declaration_list COMMA ID LTHIRD CONST_INT RTHIRD "<<endl<<endl;
		outlog<<$1->getname()<<","<<$3->getname()<<"["<<$5->getname()<<"]"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+","+$3->getname()+"["+$5->getname()+"]","decl_list");
	}
	| ID
	{
		outlog<<"At line no: "<<lines+1<<" declaration_list : ID "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"decl_list");
	}
	| ID LTHIRD CONST_INT RTHIRD
	{
		outlog<<"At line no: "<<lines+1<<" declaration_list : ID LTHIRD CONST_INT RTHIRD "<<endl<<endl;
		outlog<<$1->getname()<<"["<<$3->getname()<<"]"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"["+$3->getname()+"]","decl_list");
	}
;

statements : statement
	{
		outlog<<"At line no: "<<lines+1<<" statements : statement "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"stmnts");
	}
	| statements statement
	{
		outlog<<"At line no: "<<lines+1<<" statements : statements statement "<<endl<<endl;
		outlog<<$1->getname()<<"\n"<<$2->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"\n"+$2->getname(),"stmnts");
	}
;

statement : var_declaration
	{
		outlog<<"At line no: "<<lines+1<<" statement : var_declaration "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"stmnt");
	}
	| expression_statement
	{
		outlog<<"At line no: "<<lines+1<<" statement : expression_statement "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"stmnt");
	}
	| compound_statement
	{
		outlog<<"At line no: "<<lines+1<<" statement : compound_statement "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"stmnt");
	}
	| FOR LPAREN expression_statement expression_statement expression RPAREN statement
	{
		outlog<<"At line no: "<<lines+1<<" statement : FOR LPAREN expression_statement expression_statement expression RPAREN statement "<<endl<<endl;
		outlog<<"for("<<$3->getname()<<$4->getname()<<$5->getname()<<")\n"<<$7->getname()<<endl<<endl;
		
		$$ = new symbol_info("for("+$3->getname()+$4->getname()+$5->getname()+")\n"+$7->getname(),"stmnt");
	}
	| IF LPAREN expression RPAREN statement ELSE statement
	{
		outlog<<"At line no: "<<lines+1<<" statement : IF LPAREN expression RPAREN statement ELSE statement "<<endl<<endl;
		outlog<<"if("<<$3->getname()<<")\n"<<$5->getname()<<"\n"<<"else\n"<<$7->getname()<<endl<<endl;
		
		$$ = new symbol_info("if("+$3->getname()+")\n"+$5->getname()+"\nelse\n"+$7->getname(),"stmnt");
	}
	| IF LPAREN expression RPAREN statement
	{
		outlog<<"At line no: "<<lines+1<<" statement : IF LPAREN expression RPAREN statement "<<endl<<endl;
		outlog<<"if("<<$3->getname()<<")\n"<<$5->getname()<<endl<<endl;
		
		$$ = new symbol_info("if("+$3->getname()+")\n"+$5->getname(),"stmnt");
	}
	| WHILE LPAREN expression RPAREN statement
	{
		outlog<<"At line no: "<<lines+1<<" statement : WHILE LPAREN expression RPAREN statement "<<endl<<endl;
		outlog<<"while("<<$3->getname()<<")\n"<<$5->getname()<<endl<<endl;
		
		$$ = new symbol_info("while("+$3->getname()+")\n"+$5->getname(),"stmnt");
	}
	| PRINTLN LPAREN ID RPAREN SEMICOLON
	{
		outlog<<"At line no: "<<lines+1<<" statement : PRINTLN LPAREN ID RPAREN SEMICOLON "<<endl<<endl;
		outlog<<"printf("<<$3->getname()<<");"<<endl<<endl;
		
		$$ = new symbol_info("printf("+$3->getname()+");","stmnt");
	}
	| RETURN expression SEMICOLON
	{
		outlog<<"At line no: "<<lines+1<<" statement : RETURN expression SEMICOLON "<<endl<<endl;
		outlog<<"return "<<$2->getname()<<";"<<endl<<endl;
		
		$$ = new symbol_info("return "+$2->getname()+";","stmnt");
	}
;

expression_statement : SEMICOLON
	{
		outlog<<"At line no: "<<lines+1<<" expression_statement : SEMICOLON "<<endl<<endl;
		outlog<<";"<<endl<<endl;
		
		$$ = new symbol_info(";","expr_stmnt");
	}
	| expression SEMICOLON
	{
		outlog<<"At line no: "<<lines+1<<" expression_statement : expression SEMICOLON "<<endl<<endl;
		outlog<<$1->getname()<<";"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+";","expr_stmnt");
	}
;

variable : ID
	{
		outlog<<"At line no: "<<lines+1<<" variable : ID "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"var");
	}
	| ID LTHIRD expression RTHIRD
	{
		outlog<<"At line no: "<<lines+1<<" variable : ID LTHIRD expression RTHIRD "<<endl<<endl;
		outlog<<$1->getname()<<"["<<$3->getname()<<"]"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"["+$3->getname()+"]","var");
	}
;

expression : logic_expression
	{
		outlog<<"At line no: "<<lines+1<<" expression : logic_expression "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"expr");
	}
	| variable ASSIGNOP logic_expression
	{
		outlog<<"At line no: "<<lines+1<<" expression : variable ASSIGNOP logic_expression "<<endl<<endl;
		outlog<<$1->getname()<<"="<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"="+$3->getname(),"expr");
	}
;

logic_expression : rel_expression
	{
		outlog<<"At line no: "<<lines+1<<" logic_expression : rel_expression "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"logic_expr");
	}
	| rel_expression LOGICOP rel_expression
	{
		outlog<<"At line no: "<<lines+1<<" logic_expression : rel_expression LOGICOP rel_expression "<<endl<<endl;
		outlog<<$1->getname()<<$2->getname()<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+$2->getname()+$3->getname(),"logic_expr");
	}
;

rel_expression : simple_expression
	{
		outlog<<"At line no: "<<lines+1<<" rel_expression : simple_expression "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"rel_expr");
	}
	| simple_expression RELOP simple_expression
	{
		outlog<<"At line no: "<<lines+1<<" rel_expression : simple_expression RELOP simple_expression "<<endl<<endl;
		outlog<<$1->getname()<<$2->getname()<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+$2->getname()+$3->getname(),"rel_expr");
	}
;

simple_expression : term
	{
		outlog<<"At line no: "<<lines+1<<" simple_expression : term "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"simple_expr");
	}
	| simple_expression ADDOP term
	{
		outlog<<"At line no: "<<lines+1<<" simple_expression : simple_expression ADDOP term "<<endl<<endl;
		outlog<<$1->getname()<<$2->getname()<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+$2->getname()+$3->getname(),"simple_expr");
	}
;

term : unary_expression
	{
		outlog<<"At line no: "<<lines+1<<" term : unary_expression "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"term");
	}
	| term MULOP unary_expression
	{
		outlog<<"At line no: "<<lines+1<<" term : term MULOP unary_expression "<<endl<<endl;
		outlog<<$1->getname()<<$2->getname()<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+$2->getname()+$3->getname(),"term");
	}
;

unary_expression : ADDOP unary_expression
	{
		outlog<<"At line no: "<<lines+1<<" unary_expression : ADDOP unary_expression "<<endl<<endl;
		outlog<<$1->getname()<<$2->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+$2->getname(),"unary_expr");
	}
	| NOT unary_expression
	{
		outlog<<"At line no: "<<lines+1<<" unary_expression : NOT unary_expression "<<endl<<endl;
		outlog<<"!"<<$2->getname()<<endl<<endl;
		
		$$ = new symbol_info("!"+$2->getname(),"unary_expr");
	}
	| factor
	{
		outlog<<"At line no: "<<lines+1<<" unary_expression : factor "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"unary_expr");
	}
;

factor : variable
	{
		outlog<<"At line no: "<<lines+1<<" factor : variable "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"factor");
	}
	| ID LPAREN argument_list RPAREN
	{
		outlog<<"At line no: "<<lines+1<<" factor : ID LPAREN argument_list RPAREN "<<endl<<endl;
		outlog<<$1->getname()<<"("<<$3->getname()<<")"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"("+$3->getname()+")","factor");
	}
	| LPAREN expression RPAREN
	{
		outlog<<"At line no: "<<lines+1<<" factor : LPAREN expression RPAREN "<<endl<<endl;
		outlog<<"("<<$2->getname()<<")"<<endl<<endl;
		
		$$ = new symbol_info("("+$2->getname()+")","factor");
	}
	| CONST_INT
	{
		outlog<<"At line no: "<<lines+1<<" factor : CONST_INT "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"factor");
	}
	| CONST_FLOAT
	{
		outlog<<"At line no: "<<lines+1<<" factor : CONST_FLOAT "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"factor");
	}
	| variable INCOP
	{
		outlog<<"At line no: "<<lines+1<<" factor : variable INCOP "<<endl<<endl;
		outlog<<$1->getname()<<"++"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"++","factor");
	}
	| variable DECOP
	{
		outlog<<"At line no: "<<lines+1<<" factor : variable DECOP "<<endl<<endl;
		outlog<<$1->getname()<<"--"<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+"--","factor");
	}
;

argument_list : arguments
	{
		outlog<<"At line no: "<<lines+1<<" argument_list : arguments "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"arg_list");
	}
	|
;

arguments : arguments COMMA logic_expression
	{
		outlog<<"At line no: "<<lines+1<<" arguments : arguments COMMA logic_expression "<<endl<<endl;
		outlog<<$1->getname()<<","<<$3->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname()+","+$3->getname(),"args");
	}
	| logic_expression
	{
		outlog<<"At line no: "<<lines+1<<" arguments : logic_expression "<<endl<<endl;
		outlog<<$1->getname()<<endl<<endl;
		
		$$ = new symbol_info($1->getname(),"args");
	}
;


%%

int main(int argc, char *argv[])
{
	if(argc != 2) 
	{
        // check if filename given
		cout<<"Please input file name"<<endl;
		return 0;
	}
	yyin = fopen(argv[1], "r");
	outlog.open("my_log.txt", ios::trunc);
	
	if(yyin == NULL)
	{
		cout<<"Couldn't open file"<<endl;
		return 0;
	}
    
	yyparse();
	
	//print number of lines
	outlog << endl << "Total lines: " << lines+1 << endl;
	
	outlog.close();
	
	fclose(yyin);
	
	return 0;
}