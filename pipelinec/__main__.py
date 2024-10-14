import sys
import random
from typing import List, Optional
import antlr4

from pipelinec.interpreter import FuncValue, ListValue, Scope, TableValue, Value
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

def main(argv):
	input_stream = antlr4.FileStream(argv[1])
	lexer = LanguageLexer(input_stream)
	stream = antlr4.CommonTokenStream(lexer)
	parser = LanguageParser(stream)

	tree = parser.program()
	walker = antlr4.ParseTreeWalker()
	visitor = Visitor()

	builtins = {
		'print': FuncValue(['text'], False, lambda scope: print(scope.get('text').value, end='')),
		'println': FuncValue(['text'], False, lambda scope: print(scope.get('text').value)),
		'debug': FuncValue([], False, lambda scope: print(scope.scope)),
		'maybe': FuncValue([], False, lambda scope: Value(random.choice([True, False]))),
		'str': FuncValue(['something'], True, lambda scope: Value(str(scope.get('something').value))),
		'table': FuncValue([], True, lambda scope: TableValue({})),
		'list': FuncValue([], True, lambda scope: ListValue([])),
		'split': FuncValue(['text', 'splitter'], True, lambda scope: ListValue([
			Value(it) for it in
			scope.get('text').value.split(scope.get('splitter').value)
		])),
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

if __name__ == '__main__':
	main(sys.argv)
