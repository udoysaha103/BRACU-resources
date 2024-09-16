%{
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include "symbol_info.h"
#include "TreeNode.h"
#define YYSTYPE symbol_info*

extern int yyparse(void);
extern int yylex(void);

extern FILE *yyin;

extern YYSTYPE yylval;

std::ofstream outlog;

int lines = 1;

TreeNode* rootNode = nullptr;

void yyerror(const char *s)
{
    outlog << "At line " << lines << " " << s << std::endl << std::endl;
}

%}

%token IF ELSE FOR WHILE DO BREAK INT CHAR FLOAT DOUBLE VOID RETURN SWITCH CASE DEFAULT CONTINUE PRINTF ADDOP MULOP INCOP DECOP RELOP ASSIGNOP LOGICOP NOT LPAREN RPAREN LCURL RCURL LTHIRD RTHIRD COMMA SEMICOLON CONST_INT CONST_FLOAT ID

%nonassoc LOWER_THAN_ELSE
%nonassoc ELSE

%%
start : program
	{
		TreeNode* node = TreeNode::createNonTerminalNode("start");
		node->addChild($1->getNode());
		$$ = new symbol_info("start", "non_terminal", node);
	}
;

program : program unit
	{
		TreeNode* node = TreeNode::createNonTerminalNode("program");
		node->addChild($1->getNode());
		node->addChild($2->getNode());
		$$ = new symbol_info("program", "non_terminal", node);
		rootNode = node;
	}
	| unit
	{
		TreeNode* node = TreeNode::createNonTerminalNode("program");
		node->addChild($1->getNode());
		$$ = new symbol_info("program", "non_terminal", node);
		rootNode = node;                                        
	}
;

unit : var_declaration
	{
		TreeNode* node = TreeNode::createNonTerminalNode("unit");
		node->addChild($1->getNode());
		$$ = new symbol_info("unit", "non_terminal", node);
	}
	| func_definition
	{
		TreeNode* node = TreeNode::createNonTerminalNode("unit");
		node->addChild($1->getNode());
		$$ = new symbol_info("unit", "non_terminal", node);
	}
;

func_definition : type_specifier id_name LPAREN parameter_list RPAREN compound_statement
	{	
		TreeNode* node = TreeNode::createNonTerminalNode("func_definition"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild($2->getNode());
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($4->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild($6->getNode());
		$$ = new symbol_info("func_definition", "non_terminal", node); /// WILL THERE 
	}
	| type_specifier id_name LPAREN RPAREN compound_statement 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("func_definition"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild($2->getNode());
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild($5->getNode());
		$$ = new symbol_info("func_definition", "non_terminal", node); /// WILL THERE 
	}
;

parameter_list : parameter_list COMMA type_specifier ID
	{
		TreeNode* node = TreeNode::createNonTerminalNode("parameter_list"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("COMMA", ","));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("ID", $4->getname().c_str()));
		$$ = new symbol_info("parameter_list", "non_terminal", node); /// WILL THERE
	}
	| parameter_list COMMA type_specifier
	{
		TreeNode* node = TreeNode::createNonTerminalNode("parameter_list"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("COMMA", ","));
		node->addChild($3->getNode());
		$$ = new symbol_info("parameter_list", "non_terminal", node); /// WILL THERE
	}
	| type_specifier ID
	{
		TreeNode* node = TreeNode::createNonTerminalNode("parameter_list"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("ID", $2->getname().c_str()));
		$$ = new symbol_info("parameter_list", "non_terminal", node); /// WILL THERE
	}
	| type_specifier
	{
		TreeNode* node = TreeNode::createNonTerminalNode("parameter_list"); /// WILL THERE
		node->addChild($1->getNode());
		$$ = new symbol_info("parameter_list", "non_terminal", node); /// WILL THERE
	}
;

compound_statement : LCURL statements RCURL
	{ 
		TreeNode* node = TreeNode::createNonTerminalNode("compound_statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("LCURL", "{"));
		node->addChild($2->getNode());
		node->addChild(TreeNode::createTerminalNode("RCURL", "}"));
		$$ = new symbol_info("compound_statement", "non_terminal", node); /// WILL THERE 
	}
	| LCURL RCURL
	{ 
		TreeNode* node = TreeNode::createNonTerminalNode("compound_statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("LCURL", "{"));
		node->addChild(TreeNode::createTerminalNode("RCURL", "}"));
		$$ = new symbol_info("compound_statement", "non_terminal", node); /// WILL THERE 
	}
;

var_declaration : type_specifier declaration_list SEMICOLON
	{
		TreeNode* node = TreeNode::createNonTerminalNode("var_declaration"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild($2->getNode());
		node->addChild(TreeNode::createTerminalNode("SEMICOLON", ";"));
		$$ = new symbol_info("var_declaration", "non_terminal", node); /// WILL THERE 
	}
;

type_specifier : INT
	{
		$$ = new symbol_info("type_specifier", "terminal", TreeNode::createTerminalNode("type", "int"));
	}
	| FLOAT
	{
		$$ = new symbol_info("type_specifier", "terminal", TreeNode::createTerminalNode("type", "float"));
	}
	| VOID
	{
		$$ = new symbol_info("type_specifier", "terminal", TreeNode::createTerminalNode("type", "void"));
	}
;

declaration_list : declaration_list COMMA id_name
	{
		TreeNode* node = TreeNode::createNonTerminalNode("declaration_list"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("COMMA", ","));
		node->addChild($3->getNode());
		$$ = new symbol_info("declaration_list", "non_terminal", node); /// WILL THERE 
	}
	| declaration_list COMMA id_name LTHIRD CONST_INT RTHIRD //array after some declaration
	{
		TreeNode* node = TreeNode::createNonTerminalNode("declaration_list"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("COMMA", ","));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("LTHIRD", "["));
		node->addChild(TreeNode::createTerminalNode("const_int", $5->getname().c_str()));
		node->addChild(TreeNode::createTerminalNode("RTHIRD", "]"));
		$$ = new symbol_info("declaration_list", "non_terminal", node); /// WILL THERE 
	}
	| id_name
	{
		
		TreeNode* node = TreeNode::createNonTerminalNode("declaration_list"); /// WILL THERE
		node->addChild($1->getNode());
		$$ = new symbol_info("declaration_list", "non_terminal", node); /// WILL THERE 
	}
	| id_name LTHIRD CONST_INT RTHIRD //array
	{
		TreeNode* node = TreeNode::createNonTerminalNode("declaration_list"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("LTHIRD", "["));
		node->addChild(TreeNode::createTerminalNode("const_int", $3->getname().c_str()));
		node->addChild(TreeNode::createTerminalNode("RTHIRD", "]"));
		$$ = new symbol_info("declaration_list", "non_terminal", node); /// WILL THERE 
	}
;

id_name : ID
	{
		$$ = new symbol_info("id_name", "terminal", TreeNode::createTerminalNode("id", $1->getname().c_str()));
	}
;

statements : statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statements");
		node->addChild($1->getNode());
		$$ = new symbol_info("statements", "non_terminal", node);
	}
	| statements statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statements");
		node->addChild($1->getNode());
		node->addChild($2->getNode());
		$$ = new symbol_info("statements", "non_terminal", node);
	}
;

statement : var_declaration
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement");
		node->addChild($1->getNode());
		$$ = new symbol_info("statement", "non_terminal", node);
	}
	| expression_statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement");
		node->addChild($1->getNode());
		$$ = new symbol_info("statement", "non_terminal", node);
	}
	| compound_statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement");
		node->addChild($1->getNode());
		$$ = new symbol_info("statement", "non_terminal", node);
	}
	| FOR LPAREN expression_statement expression_statement expression RPAREN statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("FOR", $1->getname().c_str()));
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($3->getNode());
		node->addChild($4->getNode());
		node->addChild($5->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild($7->getNode());
		$$ = new symbol_info("statement", "non_terminal", node); /// WILL THERE 
	}
	| IF LPAREN expression RPAREN statement %prec LOWER_THAN_ELSE
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("IF", $1->getname().c_str()));
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild($5->getNode());
		
		$$ = new symbol_info("statement", "non_terminal", node); /// WILL THERE 
	}
	| IF LPAREN expression RPAREN statement ELSE statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("IF", $1->getname().c_str()));
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild($5->getNode());
		node->addChild(TreeNode::createTerminalNode("ELSE", $6->getname().c_str()));
		$$ = new symbol_info("statement", "non_terminal", node); /// WILL THERE 
	}
	| WHILE LPAREN expression RPAREN statement
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("WHILE", $1->getname().c_str()));
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild($5->getNode());
		$$ = new symbol_info("statement", "non_terminal", node); /// WILL THERE 
	}
	| PRINTF LPAREN id_name RPAREN SEMICOLON
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("PRINTF", "print"));
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		node->addChild(TreeNode::createTerminalNode("SEMICOLON", ";"));
		$$ = new symbol_info("statement", "non_terminal", node); /// WILL THERE 
	}
	| RETURN expression SEMICOLON
	{
		TreeNode* node = TreeNode::createNonTerminalNode("statement"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("RETURN", "return"));
		node->addChild($2->getNode());
		node->addChild(TreeNode::createTerminalNode("SEMICOLON", ";"));
		$$ = new symbol_info("statement", "non_terminal", node); /// WILL THERE 
	}
;

expression_statement : SEMICOLON
	{
		TreeNode* node = TreeNode::createNonTerminalNode("expression_statement");
		node->addChild(TreeNode::createTerminalNode("SEMICOLON", ";"));
		$$ = new symbol_info("expression_statement", "non_terminal", node); 
	}			
	| expression SEMICOLON 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("expression_statement");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("SEMICOLON", ";"));
		$$ = new symbol_info("expression_statement", "non_terminal", node); 
	}
;

variable : id_name 	
	{
		TreeNode* node = TreeNode::createNonTerminalNode("variable");
		node->addChild($1->getNode());
		$$ = new symbol_info("variable", "non_terminal", node);
	}	
	| id_name LTHIRD expression RTHIRD 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("variable"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("LTHIRD", "["));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("RTHIRD", "]"));
		$$ = new symbol_info("variable", "non_terminal", node); /// WILL THERE 
	}
;

expression : logic_expression //expr can be void
	{
		TreeNode* node = TreeNode::createNonTerminalNode("expression");
		node->addChild($1->getNode());
		$$ = new symbol_info("expression", "non_terminal", node);
	}
	| variable ASSIGNOP logic_expression 	
	{
		TreeNode* node = TreeNode::createNonTerminalNode("expression");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("ASSIGNOP", "="));
		node->addChild($3->getNode());
		$$ = new symbol_info("expression", "non_terminal", node);
	}
;

logic_expression : rel_expression //lgc_expr can be void
	{
		TreeNode* node = TreeNode::createNonTerminalNode("logic_expression");
		node->addChild($1->getNode());
		$$ = new symbol_info("logic_expression", "non_terminal", node);
	}	
	| rel_expression LOGICOP rel_expression 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("logic_expression");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("LOGICOP", $2->getname().c_str()));
		node->addChild($3->getNode());
		$$ = new symbol_info("logic_expression", "non_terminal", node);
	}	
;

rel_expression	: simple_expression //rel_expr can be void
	{
		TreeNode* node = TreeNode::createNonTerminalNode("rel_expression");
		node->addChild($1->getNode());
		$$ = new symbol_info("rel_expression", "non_terminal", node);
	}
	| simple_expression RELOP simple_expression
	{
		TreeNode* node = TreeNode::createNonTerminalNode("rel_expression");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("RELOP", $2->getname().c_str()));
		node->addChild($3->getNode());
		$$ = new symbol_info("rel_expression", "non_terminal", node);
	}
;

simple_expression : term //simp_expr can be void /// WILL THERE
	{
		TreeNode* node = TreeNode::createNonTerminalNode("simple_expression");
		node->addChild($1->getNode());
		$$ = new symbol_info("simple_expression", "non_terminal", node);
	}
	| simple_expression ADDOP term 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("simple_expression");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("ADDOP", $2->getname().c_str()));
		node->addChild($3->getNode());
		$$ = new symbol_info("simple_expression", "non_terminal", node);
	}
;        

term :	unary_expression //term can be void because of un_expr->factor
	{
		TreeNode* node = TreeNode::createNonTerminalNode("term");
		node->addChild($1->getNode());
		$$ = new symbol_info("term", "non_terminal", node);
	}
	|  term MULOP unary_expression
	{
		TreeNode* node = TreeNode::createNonTerminalNode("term");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("MULOP", $2->getname().c_str()));
		node->addChild($3->getNode());
		$$ = new symbol_info("term", "non_terminal", node);
	}
;

unary_expression : ADDOP unary_expression  // un_expr can be void because of factor
	{
		TreeNode* node = TreeNode::createNonTerminalNode("unary_expression");
		node->addChild(TreeNode::createTerminalNode("ADDOP", $1->getname().c_str()));
		node->addChild($2->getNode());
		$$ = new symbol_info("unary_expression", "non_terminal", node);
	}
	| NOT unary_expression 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("unary_expression");
		node->addChild(TreeNode::createTerminalNode("NOT", $1->getname().c_str()));
		node->addChild($2->getNode());
		$$ = new symbol_info("unary_expression", "non_terminal", node);
	}
	| factor 
	{
		TreeNode* node = TreeNode::createNonTerminalNode("unary_expression"); /// WILL THERE
		node->addChild($1->getNode());
		$$ = new symbol_info("unary_expression", "non_terminal", node); /// WILL THERE
	}
;


factor : variable  // factor can be void
    {
	    TreeNode* node = TreeNode::createNonTerminalNode("factor"); /// WILL THERE
		node->addChild($1->getNode());
		$$ = new symbol_info("factor", "non_terminal", node); /// WILL THERE 
	}
	| id_name LPAREN argument_list RPAREN
	{
	   TreeNode* node = TreeNode::createNonTerminalNode("factor"); /// WILL THERE
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($3->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		$$ = new symbol_info("factor", "non_terminal", node); /// WILL THERE 
	}
	| LPAREN expression RPAREN
	{
	   TreeNode* node = TreeNode::createNonTerminalNode("factor"); /// WILL THERE
		node->addChild(TreeNode::createTerminalNode("LPAREN", "("));
		node->addChild($2->getNode());
		node->addChild(TreeNode::createTerminalNode("RPAREN", ")"));
		$$ = new symbol_info("factor", "non_terminal", node); /// WILL THERE 
	}
	| CONST_INT 
	{
	    $$ = new symbol_info("const_int", "terminal", TreeNode::createTerminalNode("const_int", $1->getname().c_str()));
	}
	| CONST_FLOAT
	{
	    $$ = new symbol_info("const_float", "terminal", TreeNode::createTerminalNode("const_float", $1->getname().c_str()));
	}
	| variable INCOP 
	{
	    TreeNode* node = TreeNode::createNonTerminalNode("increment_expression");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("INCOP", "++"));
		$$ = new symbol_info("increment_expression", "non_terminal", node);
	}
	| variable DECOP
	{
	    TreeNode* node = TreeNode::createNonTerminalNode("decrement_expression");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("DECOP", "--"));
		$$ = new symbol_info("decrement_expression", "non_terminal", node);
	}
;

argument_list : arguments         /// WILL THERE
	{	
		TreeNode* node = TreeNode::createNonTerminalNode("argument_list");
		node->addChild($1->getNode());
		$$ = new symbol_info("argument_list", "non_terminal", node);
	}
	|
	{
	}
;/////// THERE

arguments : arguments COMMA logic_expression
	{
		TreeNode* node = TreeNode::createNonTerminalNode("arguments");
		node->addChild($1->getNode());
		node->addChild(TreeNode::createTerminalNode("COMMA", ","));
		node->addChild($3->getNode());
		$$ = new symbol_info("arguments", "non_terminal", node);
	}
	| logic_expression
	{
		TreeNode* node = TreeNode::createNonTerminalNode("arguments");
		node->addChild($1->getNode());
		$$ = new symbol_info("arguments", "non_terminal", node);
	}
;

%%

int main(int argc, char *argv[])
{
    if (argc != 2) 
    {
        std::cout << "Please input file name" << std::endl;
        return 0;
    }
    yyin = fopen(argv[1], "r");
    outlog.open("my_log.txt", std::ios::trunc);

    if (yyin == NULL)
    {
        std::cout << "Couldn't open file" << std::endl;
        return 0;
    }

    yyparse();

    if (rootNode) {
        rootNode->postOrderTraversal(outlog);
    }

    outlog.close();
    fclose(yyin);

    return 0;
}