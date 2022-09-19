from pickle import NONE
import ply.lex as lex
import ply.yacc as yacc
import sys
import basesMod
import pOperations



tokens= [
    "PINT",
    "INT",
    "FLOAT",
    "NAME",
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "EQUALS",
    "LPAREN",
    "RPAREN",
]

t_PLUS= r'\+'
t_MINUS= r'\-'
t_MULTIPLY= r'\*'
t_EQUALS= r'\='
t_LPAREN=r'\('
t_RPAREN=r'\)'

t_ignore=r'\ '


def t_PINT(t):
    r'\d+\$\d+'
    t.value=basesMod.Pbasify(t.value,Pbase)
    return t


    

def t_FLOAT(t):
    r'\d+\.\d+'
    value=float(t.value)
    t.value=pOperations.pInt(basesMod.base([0],Pbase),basesMod.base(value,Pbase),Pbase)

    return t

def t_INT(t):
    r'\d+'
    value=int(t.value)
    t.value=pOperations.pInt(basesMod.base([0],Pbase),basesMod.base(value,Pbase),Pbase)
    return t



def t_Name(t):
    r'[a-zA-Z_][a-zA-z_0-9]*'
    t.type='NAME'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip

lexer= lex.lex()

precedence= (

    ('left', 'PLUS','MINUS'),
    ('left', 'MULTIPLY'),
    ('left', 'LPAREN','RPAREN')

)

def p_calc(p):
    ''' 
    calc : expression
         | var_assign 
         | empty
     '''
    print(run(p[1]))
    #print(p[1])

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression PLUS expression
               | expression MINUS expression
    '''

    p[0]=(p[2], p[1], p[3])

def p_expression_int_float_Pint(p):
    '''
    expression : INT
               | FLOAT
               | PINT
    '''
    p[0]=p[1]

def p_expression_Paren(p):
    '''
    expression : LPAREN expression PLUS expression RPAREN
               | LPAREN expression MINUS expression RPAREN
               | LPAREN expression MULTIPLY expression RPAREN
    '''
    p[0]=(p[3],p[2],p[4])

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0]=('var', p[1])

def p_error(p):
    print("Syntax error")

def p_empty(p):
    '''
    empty :
    '''
    p[0]=None

parser=yacc.yacc()

env={}

def run(p):
    global env
    if type(p)==tuple:
        if p[0]=='+':
            return run(p[1])+run(p[2])
        elif p[0]=='-':
            return run(p[1])-run(p[2])
        elif p[0]=='*':
            return run(p[1])*run(p[2])
        elif p[0]=='=':
            env[p[1]]=run(p[2])
            print(env)
        elif p[0]=='var':
            if p[1] not in env:
                return 'undeclared variable found'
            else:
                return env[p[1]]

    else:
        return p

while True:
    try:
        Pbase=int(input("Enter the base (2-10): "))
        s=input('')
    except EOFError:
        break
    parser.parse(s)    
    






