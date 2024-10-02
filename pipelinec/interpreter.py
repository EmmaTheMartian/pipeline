from enum import Enum
from typing import Any, Callable, Optional

from antlr4.tree.Tree import TerminalNodeImpl

from pipelinec.syntax.LanguageParser import LanguageParser


class Value:
	value: Any

	def __init__(self, value: Any):
		self.value = value

	def evaluate(self) -> 'Value':
		return Value(self.value)

class FuncValue(Value):
	args: list[str]
	is_pure: bool

	def __init__(self, args: list[str], is_pure: bool, func: Callable):
		super().__init__(func)
		self.args = args
		self.is_pure = is_pure

	def invoke(self, scope: 'Scope', args: list['Value']) -> 'Value':
		child_scope = scope.make_child_scope(self.is_pure)
		for name, value in zip(self.args, args):
			child_scope.new(name, value)
		return self.value(child_scope)


class Scope:
	parent: Optional['Scope']
	scope: dict[str, Value]
	pure: bool

	def __init__(self, parent: Optional['Scope'] = None, pure: bool = True):
		self.parent = parent
		self.scope = {}
		self.pure = pure
		# Set this to false to make this scope unable to get variables from outside of its scope
		self.allow_impure_get = True

	def has(self, name: str) -> bool:
		return name in self.scope or (self.parent is not None and self.parent.has(name))

	def has_own(self, name: str) -> bool:
		return name in self.scope

	def new(self, name: str, value: Value):
		if self.has_own(name):
			raise RuntimeError("Attempted to initialize variable that already exists.")
		self.scope[name] = value

	def assign(self, name: str, value: Value):
		if self.has_own(name):
			self.scope[name] = value
		elif self.parent is not None and self.parent.has(name) and not self.pure:
			self.parent.assign(name, value)
		else:
			raise RuntimeError("Attempted to assign to a variable that does not exist.")

	def get(self, name: str) -> Value:
		if self.has_own(name):
			return self.scope[name]
		elif self.parent is not None and self.parent.has(name) and (not self.pure or self.allow_impure_get):
			return self.parent.get(name)
		else:
			raise RuntimeError("Attempted to get unknown variable: " + name)

	def make_child_scope(self, is_pure: bool = True) -> 'Scope':
		return Scope(self, is_pure)

	def evaluate_expr(self, expr: LanguageParser.ExprContext) -> Value:
		# print('eval: ', [c for c in expr.getChildren()])
		if isinstance(expr, TerminalNodeImpl) or expr is None:
			return Value(None)
		if expr.ID() is not None:
			return self.get(expr.ID().getText())
		elif expr.INT() is not None:
			return Value(int(expr.INT().getText()))
		elif expr.STRING() is not None:
			return Value(expr.STRING().getText()[1:-1])
		elif expr.invoke() is not None:
			invoke = expr.invoke()
			args = []
			func = self.get(invoke.ID().getText())
			# print('invoking ' + invoke.ID().getText())
			# if func is FuncValue:
			# 	raise RuntimeError("Attempted to invoke a non-FuncValue value (value is: " + str(func) + ")")
			for argument in range(2, invoke.getChildCount() - 1):
				# print('found arg: ' + invoke.getChild(argument).getText())
				args.append(self.evaluate_expr(invoke.getChild(argument)))
			return func.invoke(self, args)
		elif expr.func() is not None:
			func = expr.func()
			func_expr = func.stat().expr()
			is_pure = func_expr is not None and func_expr.block() is not None and func_expr.block().PURE() is not None
			func_wrapper = lambda scope: scope.evaluate_expr(func_expr)

			args = []
			for arg_index in range(1, func.getChildCount() - 2):
				args.append(func.getChild(arg_index).getText())

			return FuncValue(args, is_pure, func_wrapper)
		elif expr.block() is not None:
			block = expr.block()
			scope = Scope(self, block.PURE() is not None)
			for statement_index in range(2, block.getChildCount() - 1):
				statement = block.getChild(statement_index)
				if isinstance(statement, LanguageParser.Stat_returnContext):
					return scope.evaluate_expr(statement.expr())
				scope.evaluate_stat(statement)
		elif expr.TRUE() is not None:
			return Value(True)
		elif expr.FALSE() is not None:
			return Value(False)
		return Value(None)

	def evaluate_stat(self, stat: LanguageParser.StatContext):
		# print('evaluating statement: ' + stat.getText())
		if isinstance(stat, TerminalNodeImpl):
			return Value(None)
		elif stat.stat_var() is not None:
			stat_var = stat.stat_var()
			self.new(stat_var.ID().symbol.text, self.evaluate_expr(stat_var.expr()))
		elif stat.stat_assign() is not None:
			stat_assign = stat.stat_assign()
			self.assign(stat_assign.ID().symbol.text, self.evaluate_expr(stat_assign.expr()))
		elif stat.expr() is not None:
			self.evaluate_expr(stat.expr())
		elif stat.stat_return() is not None:
			stat_return = stat.stat_return()
			return self.evaluate_expr(stat_return.expr())
