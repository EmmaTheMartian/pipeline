import os
import sys

prod = '-prod' in sys.argv

for module in [
	'io'
]:
	print('-> ' + module)
	os.system(f'gcc -o {module}.so -shared {'-O3' if prod else ''} {module}.c')
