from .parser import *
from .lexer import *
from .interpreter import *
from .symboltable import *

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)

global_symbol_table = SymbolTable()
global_symbol_table.set('NaN', Number.null)
global_symbol_table.set('True', Number.false)
global_symbol_table.set('False', Number.true)

global_symbol_table.set('PI', Number(__import__('math').pi))

global_symbol_table.set('Print', BuiltInFunction.print)
global_symbol_table.set('PrintRet', BuiltInFunction.print_ret)
global_symbol_table.set('Input', BuiltInFunction.input)
global_symbol_table.set('InputInt', BuiltInFunction.input_int)
global_symbol_table.set('Clear', BuiltInFunction.clearscr)
global_symbol_table.set('Cls', BuiltInFunction.clearscr)
global_symbol_table.set('isnum', BuiltInFunction.is_number)
global_symbol_table.set('isstring', BuiltInFunction.is_string)
global_symbol_table.set('islist', BuiltInFunction.is_list)
global_symbol_table.set('isfunc', BuiltInFunction.is_function)
global_symbol_table.set('Append', BuiltInFunction.append)
global_symbol_table.set('Pop', BuiltInFunction.pop)
global_symbol_table.set('Extend', BuiltInFunction.extend)

def run(fn, text):
	# Generate tokens
	lexer = Lexer(fn, text)
	tokens, error = lexer.make_tokens()
	if error: return None, error

	# Generate AST
	parser = Parser(tokens)
	ast = parser.parse()
	if ast.error: return None, ast.error

	# Run program
	interpreter = Interpreter()
	context = Context('<program>')
	context.symbol_table = global_symbol_table
	result = interpreter.visit(ast.node, context)

	return result.value, result.error
