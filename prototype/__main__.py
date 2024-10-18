import sys
import random
import ctypes
from typing import List
import antlr4

from prototype.interpreter import FuncValue, ListValue, NativeValue, Scope, TableValue, Value
from .syntax.LanguageLexer import LanguageLexer
from .syntax.LanguageParser import LanguageParser
from .syntax.LanguageListener import LanguageListener

class Visitor(LanguageListener):
	scope_stack: List[Scope]

	def __init__(self):
		self.scope_stack = [Scope(pure = False)]

	def get_root_scope(self) -> Scope:
		return self.scope_stack[0]

	def get_top_scope(self):
		return self.scope_stack[-1]

	def push_scope(self, is_pure: bool = True) -> Scope:
		self.scope_stack.append(self.get_top_scope().make_child_scope(is_pure))
		return self.scope_stack[-1]

	def pop_scope(self):
		del self.scope_stack[-1]

def wrap_func(scope: Scope) -> FuncValue:
	arg_spec = scope.get('arg_spec').value
	is_pure = scope.get('is_pure').value
	func = scope.get('object').value

	def wrapped(scope_in: Scope) -> Value:
		wrapped_args = []
		for arg, c_type in arg_spec.items():
			assert isinstance(c_type.value, str)
			wrapped_args.append(getattr(ctypes, c_type.value)(scope_in.get(arg).value.encode()))
		return Value(func(*wrapped_args))

	return FuncValue(arg_spec.keys(), is_pure, wrapped)

def run(file: str) -> Value:
	input_stream = antlr4.FileStream(file)
	lexer = LanguageLexer(input_stream)
	stream = antlr4.CommonTokenStream(lexer)
	parser = LanguageParser(stream)

	tree = parser.program()
	walker = antlr4.ParseTreeWalker()
	visitor = Visitor()

	builtins = {
		# Moved to the io module
		# 'print': FuncValue(['text'], False, lambda scope: print(scope.get('text').value, end='')),
		# 'println': FuncValue(['text'], False, lambda scope: print(scope.get('text').value)),
		'debug': FuncValue([], False, lambda scope: print(scope.scope)),
		'maybe': FuncValue([], False, lambda scope: Value(random.choice([True, False]))),
		'str': FuncValue(['something'], True, lambda scope: Value(str(scope.get('something').value))),
		'table': FuncValue([], True, lambda scope: TableValue({})),
		'list': FuncValue([], True, lambda scope: ListValue([])),
		'split': FuncValue(['text', 'splitter'], True, lambda scope: ListValue([
			Value(it) for it in
			scope.get('text').value.split(scope.get('splitter').value)
		])),
		'py_eval': FuncValue(['code'], False, lambda scope: Value(eval(scope.get('code').value))),
		'py_exec': FuncValue(['code'], False, lambda scope: Value(exec(scope.get('code').value))),
		'to_native': FuncValue(['object'], True, lambda scope: NativeValue(scope.get('object').value)),
		'get_native': FuncValue(['object', 'key'], True, lambda scope: NativeValue(scope.get('object').value.__getattr__(scope.get('key').value))),
		'wrap_func': FuncValue(['object', 'is_pure', 'arg_spec'], True, wrap_func),
		'import': FuncValue(['path'], True, lambda scope: run(scope.get('path').value)),
	}

	for name, value in builtins.items():
		visitor.get_root_scope().new(name, value)

	# Interpret
	walker.walk(visitor, tree)

	tree.removeLastChild() # Remove the EOF token
	for child in tree.getChildren():
		visitor.get_root_scope().evaluate_stat(child)

	# Invoke main, if it exists
	if visitor.get_root_scope().has('main'):
		main = visitor.get_root_scope().get('main')
		if isinstance(main, FuncValue):
			main.invoke(visitor.get_root_scope(), [])

	# print(tree.toStringTree(recog = parser))
	# print('Global scope breakdown:')
	# for name, value in visitor.get_root_scope().scope.items():
	# 	print(f'{name} = {'None' if value is None else value.value}')

	return visitor.get_root_scope().returned_value

if __name__ == '__main__':
	run(sys.argv[1])
