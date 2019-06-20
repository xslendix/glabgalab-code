from .value import *
from .symboltable import *
from .rtresult import *
from .context import *
from .error import *
from .number import *
from .String import *
from .List import *

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)

class BaseFunction(Value):
	def __init__(self, name):
		super().__init__()
		self.name = name or '<anonymous>'

	def generate_new_context(self):
		new_context = Context(self.name, self.context, self.pos_start)
		new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
		return new_context

	def check_args(self, arg_names, args):
		res = RTResult()

		if len(args) > len(arg_names):
			return res.failure(RTError(
				self.pos_start, self.pos_end,
				f"{len(args) - len(arg_names)} too many args passed into '{self.name}'",
				self.context
			))
		
		if len(args) < len(arg_names):
			return res.failure(RTError(
				self.pos_start, self.pos_end,
				f"{len(arg_names) - len(args)} too few args passed into '{self.name}'",
				self.context
			))
		
		return res.success(None)
	
	def populate_args(self, arg_names, args, exec_ctx):
		for i in range(len(args)):
			arg_name = arg_names[i]
			arg_value = args[i]
			arg_value.set_context(exec_ctx)
			exec_ctx.symbol_table.set(arg_name, arg_value)

	def check_and_populate_args(self, arg_names, args, exec_ctx):
		res = RTResult()
		res.register(self.check_args(arg_names, args))
		if res.error: return res
		self.populate_args(arg_names, args, exec_ctx)
		return res.success(None)

class Function(BaseFunction):
	def __init__(self, name, body_node, arg_names):
		super().__init__(name)
		self.body_node = body_node
		self.arg_names = arg_names

	def execute(self, args):
		res = RTResult()
		interpreter = Interpreter()
		exec_ctx = self.generate_new_context()

		res.register(self.check_and_populate_args(self.arg_names, args, exec_ctx))
		if res.error: return res

		value = res.register(interpreter.visit(self.body_node, exec_ctx))
		if res.error: return res
		return res.success(value)

	def copy(self):
		copy = Function(self.name, self.body_node, self.arg_names)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		return copy

	def __repr__(self):
		return f"<function {self.name}>"

class BuiltInFunction(BaseFunction):
	def __init__(self, name):
		super().__init__(name)
	
	def execute(self, args):
		res = RTResult()
		exec_ctx = self.generate_new_context()

		method_name = f'execute_{self.name}'
		method = getattr(self, method_name, self.no_visit_method)

		res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
		if res.error: return res
		
		return_value = res.register(method(exec_ctx))
		if res.error: return res
		
		return res.success(return_value)

	def no_visit_method(self, node, context):
		raise Exception(f'No execute_{self.name} method defined')

	def copy(self):
		copy = BuiltInFunction(self.name)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		
		return copy
	
	def __repr__(self):
		return f'<built-in function {self.name}>'
	
	############# Built-in function definitions ################

	def execute_print(self, exec_ctx):
		print(str(exec_ctx.symbol_table.get('value')), end='')

		return RTResult().success(Number.null)
	execute_print.arg_names = ['value']
	
	def execute_print_ret(self, exec_ctx):
		return RTResult().success(String(str(exec_ctx.symbol_table.get('value'))))
	execute_print_ret.arg_names = ['value']

	def execute_input(self, exec_ctx):
		text = input(str(exec_ctx.symbol_table.get('prompt')) or '')

		return RTResult().success(String(text))
	execute_input.arg_names = ['prompt']

	def execute_input_int(self, exec_ctx):
		i = 1

		while True:
			input1 = input(str(exec_ctx.symbol_table.get('prompt')) or '')
			try:
				input1 = int(input1)
				break
			except ValueError:
				pass

		return RTResult().success(Number(input1))
	execute_input.arg_names = ['prompt']

	def execute_clearsrc(self, exec_ctx):
		from os import system, name
		if name == 'nt': _ = system('cls')
		else: _ = system('clear')
		
		return RTResult().success(Number.null)
	execute_clearsrc.arg_names = []

	def execute_is_number(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_tabel.get('value'), Number)

		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_number = ['value']

	def execute_is_string(self, exec_ctx):
		is_string = isinstance(exec_ctx.symbol_tabel.get('value'), String)

		return RTResult().success(Number.true if is_string else Number.false)
	execute_is_string = ['value']

	def execute_is_list(self, exec_ctx):
		is_list = isinstance(exec_ctx.symbol_tabel.get('value'), List)

		return RTResult().success(Number.true if is_list else Number.false)
	execute_is_list = ['value']

	def execute_is_function(self, exec_ctx):
		is_function = isinstance(exec_ctx.symbol_tabel.get('value'), BaseFunction)

		return RTResult().success(Number.true if is_function else Number.false)
	execute_is_function = ['value']

	def execute_append(self, exec_ctx):
		list_ = exec_ctx.symbol_tabel.get('list')
		value = exec_ctx.symbol_tabel.get('value')

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'First argument must be a list',
				exec_ctx
			))
		
		list_.elements.append(value)
		return RTResult().success(Number.null)
	execute_append.arg_names = ['list', 'value']

	def execute_pop(self, exec_ctx):
		list_ = exec_ctx.symbol_tabel.get('list')
		index = exec_ctx.symbol_tabel.get('index')

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'First argument must be a list',
				exec_ctx
			))
		
		if not isinstance(index, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'Second argument must be a number',
				exec_ctx
			))
		
		try:
			element = list_.elements.pop(index.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'Element at this index cannot be removed because the index is out of bounds.',
				exec_ctx
			))
		return RTResult().success(element)
	execute_pop.arg_names = ['list', 'index']

	def execute_extend(self, exec_ctx):
		listA = exec_ctx.symbol_tabel.get('listA')
		listB = exec_ctx.symbol_tabel.get('listB')

		if not isinstance(listA, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'First argument must be a list',
				exec_ctx
			))

		if not isinstance(listB, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				'Second argument must be a list',
				exec_ctx
			))

			listA.elements.extend(listB.elements)
		return RTResult().success(Number.null)
	execute_extend.arg_names = ["listA", 'listB']

BuiltInFunction.print = BuiltInFunction('print')
BuiltInFunction.print_ret = BuiltInFunction('print_ret')
BuiltInFunction.input = BuiltInFunction('input')
BuiltInFunction.input_int = BuiltInFunction('input_int')
BuiltInFunction.clear = BuiltInFunction('clear')
BuiltInFunction.is_number = BuiltInFunction('is_number')
BuiltInFunction.is_string = BuiltInFunction('is_string')
BuiltInFunction.is_list = BuiltInFunction('is_list')
BuiltInFunction.is_function = BuiltInFunction('is_function')
BuiltInFunction.append = BuiltInFunction('append')
BuiltInFunction.pop = BuiltInFunction('pop')
BuiltInFunction.extend = BuiltInFunction('extend')

from .interpreter import Interpreter