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

	def is_truthy(self) -> bool:
		return self.value is True

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

	# Set make_scope to False to force codeblocks to execute without making a new scope.
	# This is used for `if` and `for` statements
	def evaluate_expr(self, expr: LanguageParser.ExprContext, make_scope: bool = True) -> Value:
		# print('eval: ', [c for c in expr.getChildren()])
		if isinstance(expr, TerminalNodeImpl) or expr is None:
			return Value(None)

		# Literals
		if expr.INT() is not None:
			return Value(int(expr.INT().getText()))
		elif expr.STRING() is not None:
			return Value(expr.STRING().getText()[1:-1])
		elif expr.TRUE() is not None:
			return Value(True)
		elif expr.FALSE() is not None:
			return Value(False)
		# Control flow and friends
		elif expr.expr_func() is not None:
			func = expr.expr_func()
			func_expr = func.stat().expr()

			args = []
			for arg_index in range(2, func.getChildCount() - 2):
				args.append(func.getChild(arg_index).getText())

			return FuncValue(args, func.PURE() is not None, lambda scope: scope.evaluate_expr(func_expr))
		elif expr.expr_invoke() is not None:
			invoke = expr.expr_invoke()
			args = []
			func = self.get(invoke.ID().getText())
			if not isinstance(func, FuncValue):
				raise RuntimeError("Attempted to invoke a non-FuncValue value (value is: " + str(func) + ")")
			# Check if purity matches
			if not func.is_pure and self.pure:
				raise RuntimeError("Cannot invoke impure functions in a pure scope. Impure function was: " + invoke.ID().getText())
			for argument in range(2, invoke.getChildCount() - 1):
				args.append(self.evaluate_expr(invoke.getChild(argument)))
			return func.invoke(self, args)
		elif expr.expr_block() is not None:
			block = expr.expr_block()
			is_pure = block.PURE() is not None
			scope = self if not make_scope else self.make_child_scope(is_pure)
			# If we are pure, there is an extra `pure` keyword denoting that, which must be ignored here.
			start_index = 2 if is_pure else 1

			print(f'eval\'ing block. make_scope={make_scope} and is_pure={is_pure}')
			for statement_index in range(start_index, block.getChildCount() - 1):
				statement = block.getChild(statement_index)
				if isinstance(statement, TerminalNodeImpl):
					continue
				if statement.stat_return() is not None:
					print(f'found return: {statement.getChild(0).expr().getText()}')
					return scope.evaluate_expr(statement.getChild(0).expr())
				scope.evaluate_stat(statement)
			print('block eval done')
		elif expr.expr_if() is not None:
			if_ = expr.expr_if()

			if self.evaluate_expr(if_.getChild(2)).is_truthy():
				print('eval\'ing `if` expr where cond was true')
				return self.evaluate_expr(if_.getChild(4), make_scope = False)
			elif if_.ELSE() is not None:
				print('eval\'ing `else` expr where cond')
				return self.evaluate_expr(if_.getChild(6), make_scope = False)
		elif expr.expr_for() is not None:
			pass
		# Operators
		elif expr.OP_NOT() is not None: pass
		elif expr.OP_AND() is not None: pass
		elif expr.OP_OR() is not None: pass
		elif expr.OP_EQ() is not None: pass
		elif expr.OP_NEQ() is not None: pass
		elif expr.OP_GT() is not None: pass
		elif expr.OP_GTEQ() is not None: pass
		elif expr.OP_LT() is not None: pass
		elif expr.OP_LTEQ() is not None: pass
		elif expr.OP_IS() is not None: pass
		elif expr.OP_IN() is not None: pass
		elif expr.OP_DOT() is not None: pass
		elif expr.OP_INC() is not None: pass
		elif expr.OP_DEC() is not None: pass
		# ID
		elif expr.ID() is not None:
			return self.get(expr.ID().getText())

		return Value(None)

	def evaluate_stat(self, stat: LanguageParser.StatContext):
		# print('evaluating statement: ' + stat.getText())
		if isinstance(stat, TerminalNodeImpl):
			return Value(None)

		elif stat.stat_var() is not None:
			stat_var = stat.stat_var()
			self.new(stat_var.ID().symbol.text, self.evaluate_expr(stat_var.expr()))
		elif stat.stat_const() is not None:
			stat_const = stat.stat_const()
			self.new(stat_const.ID().symbol.text, self.evaluate_expr(stat_const.expr()))
		elif stat.stat_assign() is not None:
			stat_assign = stat.stat_assign()
			self.assign(stat_assign.ID().symbol.text, self.evaluate_expr(stat_assign.expr()))
		elif stat.expr() is not None:
			return self.evaluate_expr(stat.expr())
		elif stat.stat_return() is not None:
			return self.evaluate_expr(stat.stat_return().expr())
		return Value(None)

	def __enter__(self):
		return self

	def __exit__(self, *args):
		pass
