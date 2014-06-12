#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

from ply import yacc

from tinyc import common
from tinyc.lexer import Lexer


class Parser(object):
    tokens = common.TOKENS

    def p_program(self, t):
        """program : external_declaration
                   | program external_declaration"""
        pass

    def p_external_declaration(self, t):
        """external_declaration : declaration
                                | function_definition"""
        pass

    def p_declaration(self, t):
        """declaration : INT declarator_list SEMICOLON"""
        pass

    def p_declarator_list(self, t):
        """declarator_list : declarator
                           | declarator COMMA declarator_list"""
        pass

    def p_declarator(self, t):
        """declarator : ID"""
        pass

    def p_function_definition(self, t):
        """function_definition : INT declarator LPAREN parameter_type_list_opt RPAREN compound_statement"""
        pass

    def p_parameter_type_list_opt(self, t):
        """parameter_type_list_opt :
                                    | parameter_type_list"""
        pass

    def p_parameter_type_list(self, t):
        """parameter_type_list : parameter_declaration
                               | parameter_type_list COMMA parameter_declaration"""
        pass

    def p_parameter_declaration(self, t):
        """parameter_declaration : INT declarator"""
        pass

    def p_statement(self, t):
        """statement : SEMICOLON
                     | expression SEMICOLON
                     | compound_statement
                     | IF LPAREN expression RPAREN statement
                     | IF LPAREN expression RPAREN statement ELSE statement
                     | WHILE LPAREN expression RPAREN statement
                     | RETURN expression SEMICOLON"""
        pass

    def p_compound_statement(self, t):
        """compound_statement : LBRACE declaration_list_opt statement_list_opt RBRACE"""
        pass

    def p_declaration_list_opt(self, t):
        """declaration_list_opt :
                                | declaration_list"""
        pass

    def p_declaration_list(self, t):
        """declaration_list : declaration
                            | declaration_list declaration"""
        pass

    def p_statement_list_opt(self, t):
        """statement_list_opt :
                              | statement_list"""
        pass

    def p_statement_list(self, t):
        """statement_list : statement
                          | statement_list statement"""
        pass

    def p_expression(self, t):
        """expression : assign_expr
                      | expression COMMA assign_expr"""
        pass

    def p_assign_expr(self, t):
        """assign_expr : logical_OR_expr
                       | ID EQUALS assign_expr"""
        pass

    def p_logical_OR_expr(self, t):
        """logical_OR_expr : logical_AND_expr
                           | logical_OR_expr LOR logical_AND_expr"""
        pass

    def p_logical_AND_expr(self, t):
        """logical_AND_expr : equality_expr
                            | logical_AND_expr LAND equality_expr"""
        pass

    def p_equality_expr(self, t):
        """equality_expr : relational_expr
                         | equality_expr EQ relational_expr
                         | equality_expr NEQ relational_expr"""
        pass

    def p_relational_expr(self, t):
        """relational_expr : add_expr
                           | relational_expr LT add_expr
                           | relational_expr GT add_expr
                           | relational_expr LTE add_expr
                           | relational_expr GTE add_expr"""
        pass

    def p_add_expr(self, t):
        """add_expr : mult_expr
                    | add_expr PLUS mult_expr
                    | add_expr MINUS mult_expr"""
        pass

    def p_mult_expr(self, t):
        """mult_expr : unary_expr
                     | mult_expr MULT unary_expr
                     | mult_expr DIV unary_expr"""
        pass

    def p_unary_expr(self, t):
        """unary_expr : postfix_expr
                      | MINUS unary_expr"""
        pass

    def p_postfix_expr(self, t):
        """postfix_expr : primary_expr
                        | ID LPAREN argument_expression_list_opt RPAREN"""
        pass

    def p_primary_expr(self, t):
        """primary_expr : ID
                        | CONSTANT
                        | LPAREN expression RPAREN"""
        pass

    def p_argument_expression_list_opt(self, t):
        """argument_expression_list_opt :
                                          | argument_expression_list"""
        pass

    def p_argument_expression_list(self, t):
        """argument_expression_list : assign_expr
                                    | argument_expression_list COMMA assign_expr"""
        pass

    def p_error(self, t):
        message = "Line {line}: Syntax error at '{value}'. "
        print(
            message.format(
                line=t.lineno,
                value=t.value),
            file=sys.stderr)

    precedence = (
        ('right', 'ELSE',),
    )

    def build(self, **kwargs):
        self.lexer = Lexer()
        self.lexer.build()
        kwargs['debug'] = True
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data):
        return self.parser.parse(data)
