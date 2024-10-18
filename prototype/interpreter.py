from typing import Any, Callable, Dict, List, Optional
from antlr4.tree.Tree import TerminalNodeImpl
from prototype.syntax.LanguageParser import LanguageParser


ESCAPES = {
	"\\\"": "\"",
	"\\'": "'",
	"\\r": "\r",
	"\\n": "\n",
	"\\t": "\t",
	"\\f": "\f",
}


class Value:
	members: Dict[str, 'Value']
	value: Any

	def __init__(self, value: Any):
		self.value = value
		self.members = { }

	def evaluate(self) -> 'Value':
		return Value(self.value)

	def is_truthy(self) -> bool:
		return self.value is True

	def get_native(self, scope: 'Scope'):
		return self.value.__dict__[scope.get('name').value]

	# Operators
	def add(self, other: 'Value')  -> 'Value': return Value(self.value + other.value)
	def sub(self, other: 'Value')  -> 'Value': return Value(self.value - other.value)
	def mul(self, other: 'Value')  -> 'Value': return Value(self.value * other.value)
	def div(self, other: 'Value')  -> 'Value': return Value(self.value / other.value)
	def mod(self, other: 'Value')  -> 'Value': return Value(self.value % other.value)
	def eq(self, other: 'Value')   -> 'Value': return Value(self.value == other.value)
	def gt(self, other: 'Value')   -> 'Value': return Value(self.value > other.value)
	def gteq(self, other: 'Value') -> 'Value': return Value(self.value >= other.value)
	def lt(self, other: 'Value')   -> 'Value': return Value(self.value < other.value)
	def lteq(self, other: 'Value') -> 'Value': return Value(self.value <= other.value)
	def is_(self, other: 'Value')  -> 'Value': return Value(other is self)
	def in_(self, other: 'Value')  -> 'Value': return Value(other.value in self)

	def inc(self) -> 'Value':
		self.value += 1
		return self.value

	def dec(self) -> 'Value':
		self.value -= 1
		return self.value

	def dot(self, id_: str) -> 'Value':
		if id_ in self.members:
			return self.members[id_]
		raise RuntimeError(f"Unknown variable: {id_}")


class NativeValue(Value):
	def __init__(self, value: Any):
		super().__init__(value)

	def dot(self, id_: str) -> 'NativeValue':
		if id_ in self.__dict__:
			return self.__dict__[id_]
		raise RuntimeError(f"Unknown native variable: {id_}")


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


class TableValue(Value):
	def __init__(self, value: Optional[Dict[str, Value]] = None):
		super().__init__(value or {})
		self.members['get'] = FuncValue(['index'], True, lambda scope: self.get(scope.get('index').value))
		self.members['put'] = FuncValue(['index', 'value'], True, lambda scope: self.put(scope.get('index').value, scope.get('value')))
		def _put_ip(scope: Scope) -> TableValue:
			self.put(scope.get('index').value, scope.get('value'))
			return self
		self.members['put_ip'] = FuncValue(['index', 'value'], True, _put_ip)

	def get(self, index: str) -> Value:
		return self.value[index]

	def put(self, index: str, value: Value):
		self.value[index] = value

	def dot(self, id_: str) -> Value:
		if id_ in self.value:
			return self.value[id_]
		return super().dot(id_)


class ListValue(Value):
	def __init__(self, value: Optional[List[Value]] = None):
		super().__init__(value or [])
		self.members['append'] = FuncValue(['value'], True, lambda scope: self.value.append(scope.get('value')))
		self.members['prepend'] = FuncValue(['value'], True, lambda scope: self.value.insert(0, scope.get('value')))
		self.members['insert'] = FuncValue(['index', 'value'], True, lambda scope: self.value.insert(int(scope.get('index').value), scope.get('value')))
		self.members['pop'] = FuncValue([], True, lambda scope: Value(self.value.pop()))
		self.members['get'] = FuncValue(['index'], True, lambda scope: Value(self.value[int(scope.get('index').value)]))
		self.members['count'] = FuncValue([], True, lambda scope: Value(len(self.value)))
		self.members['for_each'] = FuncValue(['callback'], False, lambda scope: ListValue([scope.get('callback').invoke(scope, [it]) for it in self.value]))
		def _append_ip(scope):
			self.value.append(scope.get('value').value)
			return self
		self.members['append_ip'] = FuncValue(['value'], True, _append_ip)


class Scope:
	parent: Optional['Scope']
	scope: dict[str, Value]
	pure: bool
	returned_value: Value

	def __init__(self, parent: Optional['Scope'] = None, pure: bool = True):
		self.parent = parent
		self.scope = {}
		self.pure = pure
		self.returned_value = Value(None)
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

	def format_string(self, string: str) -> str:
		# Replace escape sequences with the actual characters
		for escape, value in ESCAPES.items():
			string = string.replace(escape, value)
		# todo: string formatting
		return string

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
			return Value(self.format_string(expr.STRING().getText()[1:-1]))
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
				argument = func.getChild(arg_index)
				if isinstance(argument, TerminalNodeImpl) and argument.getText() == ',':
					continue
				args.append(argument.getText())

			return FuncValue(args, func.PURE() is not None, lambda scope: scope.evaluate_expr(func_expr))
		elif expr.part_invoke() is not None:
			# Get the function
			func = self.evaluate_expr(expr.getChild(0))
			if not isinstance(func, FuncValue):
				raise RuntimeError("Attempted to invoke a non-FuncValue value (value is: " + str(func) + ")")

			# Check if purity matches
			if not func.is_pure and self.pure:
				raise RuntimeError("Cannot invoke impure functions in a pure scope.")

			# Evaluate arguments
			invoke = expr.part_invoke()
			args = []
			for arg_index in range(1, invoke.getChildCount() - 1):
				argument = invoke.getChild(arg_index)
				if isinstance(argument, TerminalNodeImpl) and argument.getText() == ',':
					continue
				args.append(self.evaluate_expr(argument))

			# Invoke
			return func.invoke(self, args)
		elif expr.expr_block() is not None:
			block = expr.expr_block()
			is_pure = block.PURE() is not None
			scope = self if not make_scope else self.make_child_scope(is_pure)
			# If we are pure, there is an extra `pure` keyword denoting that, which must be ignored here.
			start_index = 2 if is_pure else 1

			for statement_index in range(start_index, block.getChildCount() - 1):
				statement = block.getChild(statement_index)
				if isinstance(statement, TerminalNodeImpl):
					continue
				if statement.stat_return() is not None:
					return scope.evaluate_expr(statement.getChild(0).expr())
				scope.evaluate_stat(statement)
		elif expr.expr_if() is not None:
			if_ = expr.expr_if()

			if self.evaluate_expr(if_.getChild(2)).is_truthy():
				return self.evaluate_expr(if_.getChild(4), make_scope = False)
			elif if_.ELSE() is not None:
				return self.evaluate_expr(if_.getChild(6), make_scope = False)
		elif expr.expr_for() is not None:
			pass
		# Operators
		elif expr.OP_DOT() is not None: return self.evaluate_expr(expr.getChild(0)).dot(expr.getChild(2).getText())
		elif expr.OP_NOT() is not None: return Value(not self.evaluate_expr(expr.getChild(2)).value)
		elif expr.OP_AND() is not None: return Value(self.evaluate_expr(expr.getChild(2)).value and expr.getChild(0).value)
		elif expr.OP_OR() is not None: return Value(self.evaluate_expr(expr.getChild(2)).value or self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_EQ() is not None: return self.evaluate_expr(expr.getChild(2)).eq(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_NEQ() is not None: return Value(not self.evaluate_expr(expr.getChild(2)).eq(self.evaluate_expr(expr.getChild(0))))
		elif expr.OP_GT() is not None: return self.evaluate_expr(expr.getChild(2)).gt(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_GTEQ() is not None: return self.evaluate_expr(expr.getChild(2)).gteq(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_LT() is not None: return self.evaluate_expr(expr.getChild(2)).lt(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_LTEQ() is not None: return self.evaluate_expr(expr.getChild(2)).lteq(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_IS() is not None: return self.evaluate_expr(expr.getChild(2)).is_(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_IN() is not None: return self.evaluate_expr(expr.getChild(2)).in_(self.evaluate_expr(expr.getChild(0)))
		elif expr.OP_INC() is not None: return self.evaluate_expr(expr.getChild(0)).inc()
		elif expr.OP_DEC() is not None: return self.evaluate_expr(expr.getChild(0)).dec()
		# Math operators
		elif expr.ADD() is not None: return self.evaluate_expr(expr.getChild(0)).add(self.evaluate_expr(expr.getChild(2)))
		elif expr.SUB() is not None: return self.evaluate_expr(expr.getChild(0)).add(self.evaluate_expr(expr.getChild(2)))
		elif expr.MUL() is not None: return self.evaluate_expr(expr.getChild(0)).add(self.evaluate_expr(expr.getChild(2)))
		elif expr.DIV() is not None: return self.evaluate_expr(expr.getChild(0)).add(self.evaluate_expr(expr.getChild(2)))
		elif expr.MOD() is not None: return self.evaluate_expr(expr.getChild(0)).add(self.evaluate_expr(expr.getChild(2)))
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
			self.returned_value = self.evaluate_expr(stat.stat_return().expr())
			return self.returned_value
		return Value(None)

	def __enter__(self):
		return self

	def __exit__(self, *args):
		pass
