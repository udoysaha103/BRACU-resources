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

%start program

%%

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
		                                        
	}
	;

unit : var_declaration
	 {
		
	 }
     | func_definition
     {
		
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
			
		}
 		;

parameter_list : parameter_list COMMA type_specifier ID
		{
			
		}
		| parameter_list COMMA type_specifier
		{
			
		}
 		| type_specifier ID
 		{
			
		}
		| type_specifier
		{
			
		}
 		;

compound_statement : LCURL statements RCURL
		{ 
 			
		}
		| LCURL RCURL
		{ 
 			
		}
		;
var_declaration : type_specifier declaration_list SEMICOLON
		{
			
		}
		;






type_specifier : INT
		{
			$$ = new symbol_info("type", "terminal", TreeNode::createTerminalNode("type", "int"));
		}
		| FLOAT
		{
			
		}
		| VOID
		{
			$$ = new symbol_info("type", "terminal", TreeNode::createTerminalNode("type", "void"));
		}
		;






declaration_list : declaration_list COMMA id_name
		{
			
		}
		| declaration_list COMMA id_name LTHIRD CONST_INT RTHIRD //array after some declaration
		{
			
		}
		| id_name
		{
			

		}
		| id_name LTHIRD CONST_INT RTHIRD //array
		{
			
		}
		;









id_name : ID
		{
			$$ = new symbol_info("id", "terminal", TreeNode::createTerminalNode("id", $1->getname().c_str()));
		}
		;











statements : statement
		{
			
		}
		| statements statement
		{
			
		}
		;


statement : var_declaration
	  {
	    	
	  }
	  | expression_statement
	  {
	    	
	  }
	  | compound_statement
	  {
	    	
	  }
	  | FOR LPAREN expression_statement expression_statement expression RPAREN statement
	  {
	    	
	  }
	  | IF LPAREN expression RPAREN statement %prec LOWER_THAN_ELSE
	  {
	    	
	  }
	  | IF LPAREN expression RPAREN statement ELSE statement
	  {
	    	
	  }
	  | WHILE LPAREN expression RPAREN statement
	  {
	    	
	  }
	  | PRINTF LPAREN id_name RPAREN SEMICOLON
	  {
	    	
	  }
	  | RETURN expression SEMICOLON
	  {
	    	
	  }
	  ;

expression_statement : SEMICOLON
			{
				
	        }			
			| expression SEMICOLON 
			{
				
	        }
			;

variable : id_name 	
     {
	    $$ = $1;
	 }	
	 | id_name LTHIRD expression RTHIRD 
	 {
	 	
	 }
	 ;

expression : logic_expression //expr can be void
	   {
	    	
	   }
	   | variable ASSIGNOP logic_expression 	
	   {
	    	
	   }
	   ;

logic_expression : rel_expression //lgc_expr can be void
	     {
	    	
	     }	
		 | rel_expression LOGICOP rel_expression 
		 {
	    	
	     }	
		 ;

rel_expression	: simple_expression //rel_expr can be void
		{
	    	
	    }
		| simple_expression RELOP simple_expression
		{
	    	
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
		  ;             ////////WILL THERE

term :	unary_expression //term can be void because of un_expr->factor
     {
	    	
	 }
     |  term MULOP unary_expression
     {
	    	
	 }
     ;

unary_expression : ADDOP unary_expression  // un_expr can be void because of factor
		 {
	    	
	     }
		 | NOT unary_expression 
		 {
	    	
	     }
		 | factor 
		 {
	    	$$ = $1;
	     }
		 ;


factor : variable  // factor can be void
    {
	    $$ = $1;
	}
	| id_name LPAREN argument_list RPAREN
	{
	   
	}
	| LPAREN expression RPAREN
	{
	   
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
					$$ = $1;
			  }
			  |
			  {
			  }
			  ;/////// THERE

arguments : arguments COMMA logic_expression
		  {
				TreeNode* node = TreeNode::createNonTerminalNode("argument_list");
				node->addChild($1->getNode());
				node->addChild(TreeNode::createTerminalNode("COMMA", ","));
				node->addChild($3->getNode());
				$$ = new symbol_info("argument_list", "non_terminal", node);
		  }
	      | logic_expression
	      {
				TreeNode* node = TreeNode::createNonTerminalNode("argument_list");
				node->addChild($1->getNode());
				$$ = new symbol_info("argument_list", "non_terminal", node);
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