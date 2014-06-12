#!/usr/bin/env python
# -*- coding: utf-8 -*-

KEYWORDS = {
    # Keywords
    'int': 'INT',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'while': 'WHILE',
}

TOKENS = (
    # Operators
    'PLUS',     # +
    'MINUS',    # -
    'MULT',     # *
    'DIV',      # /
    'LAND',     # &&
    'LOR',      # ||
    'EQ',       # ==
    'NEQ',      # !=
    'LT',       # <
    'LTE',      # <=
    'GT',       # >
    'GTE',      # >=

    # Assignments
    'EQUALS',   # =

    # Literals
    'ID',       # identifiers
    'CONSTANT', # constant (int)

    # Delimiters
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # {
    'RBRACE',       # }
    'COMMA',        # ,
    'SEMICOLON',    # ;
) + tuple(KEYWORDS.values())
