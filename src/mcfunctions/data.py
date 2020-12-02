import re
def _parse_num(n):
	clean = re.sub('~|x|y|z|X|Y|Z|\\(|\\)|,|\\s','',str(n))
	if len(clean) == 0:
		return 0
	if '.' in clean:
		return float(clean)
	else:
		return int(clean)
class NumVal:
	def __init__(self, n):
		if type(n) == NumVal:
			self.val = n.val
			self.is_relative = n.is_relative
		self.val = _parse_num(n)
		self.is_relative = str(n).strip().startswith('~')
	def __str__(self):
		if self.is_relative:
			if self.val == 0:
				return '~'
			else:
				return '~%s' % self.val
		else:
			return '%s' % self.val
	def __copy__(self):
		return self.copy()
	def copy(self):
		return NumVal(self)
	def __add__(self, other):
		cp = self.copy()
		if type(other) == NumVal:
			cp.val += other.val
		else:
			cp.val += other
		return cp
	def __sub__(self, other):
		cp = self.copy()
		if type(other) == NumVal:
			cp.val -= other.val
		else:
			cp.val -= other
		cp.is_relative = True # a difference is always relative
		return cp
	def __mul__(self, other):
		cp = self.copy()
		if type(other) == NumVal:
			cp.val *= other.val
		else:
			cp.val *= other
		return cp
	def __truediv__(self, other):
		cp = self.copy()
		if type(other) == NumVal:
			cp.val /= other.val
		else:
			cp.val /= other
		return cp
	def __floordiv__(self, other):
		cp = self.copy()
		if type(other) == NumVal:
			cp.val = cp.val // other.val
		else:
			cp.val = cp.val // other
		return cp
	def make_absolute(self, relative_to=0):
		cp = self.copy() - relative_to
		cp.is_relative = False
		return cp
	def make_relative(self, relative_to=0):
		cp = self.copy() - relative_to
		cp.is_relative = True
		return cp
	def __int__(self):
		return int(self.val)
	def block_pos(self):
		cp = self.copy()
		cp.val = int(cp.val)
		return cp
class Pos:
	def __init__(self, *args):
		self.x = 0
		self.y = None
		self.z = 0
		if len(args) == 0:
			raise ValueError('mcfunctions.data.Pos.__init__(*args) requires at least 1 argument')
		if len(args) == 1:
			# single argument. String or tuple?
			arg = args[0]
			if type(arg) == str:
				comps = re.split('[, ]+',arg)
			else:
				comps = arg
		else:
			comps = args
		if len(comps) == 3:
			self.x = NumVal(comps[0])
			self.y = NumVal(comps[1])
			self.z = NumVal(comps[2])
		elif len(comps) == 2:
			self.x = NumVal(comps[0])
			self.z = NumVal(comps[1])
		else:
			raise ValueError('mcfunctions.data.Pos.__init__(*args) must be a 2D (X,Z) or 3D (X,Y,Z) coordinate')
	def __str__(self):
		if self.y is not None:
			return '%s %s %s' % (self.x, self.y, self.z)
		else:
			return '%s %s' % (self.x, self.z)
	def __copy__(self):
		return self.copy()
	def copy(self):
		return Pos(self.x, self.y, self.z)
	def __getitem__(self, item):
		if type(item) == str:
			item = item.lower()
			if item == 'x': return self.x
			if item == 'y': return self.y
			if item == 'z': return self.z
		if item == 0:
			return self.x
		elif item == 1:
			if self.y is not None:
				return self.y
			else:
				return self.z
		elif item == 2:
			if self.y is not None:
				return self.z
		raise KeyError('Error: Pos has no index "%s"' % item)
	def __setitem__(self, item, value):
		if type(item) == str:
			item = item.lower()
			if item == 'x': self.x = NumVal(value)
			if item == 'y': self.y = NumVal(value)
			if item == 'z': self.z = NumVal(value)
			return
		if item == 0:
			self.x = NumVal(value)
			return
		elif item == 1:
			if self.y is not None:
				self.y = NumVal(value)
			else:
				self.z = NumVal(value)
			return
		elif item == 2:
			if self.y is not None:
				self.z = NumVal(value)
				return
		raise KeyError('Error: Pos has no index "%s"' % item)
	def __len__(self):
		if self.y is not None:
			return 3
		else:
			return 2
	def __add__(self, other):
		if type(other) == str:
			return self + Pos(other)
		if len(self) != len(other):
			raise KeyError('%s and %s are not the same dimensionality' % (self,other))
		cp = self.copy()
		for i in range(0, len(cp)):
			cp[i] = NumVal(cp[i]) + NumVal(other[i])
		return cp
	def __sub__(self, other):
		if type(other) == str:
			return self - Pos(other)
		if len(self) != len(other):
			raise KeyError('%s and %s are not the same dimensionality' % (self,other))
		cp = self.copy()
		for i in range(0, len(cp)):
			cp[i] = NumVal(cp[i]) - NumVal(other[i])
		return cp
	def __mul__(self, other):
		if type(other) == str:
			return self * Pos(other)
		if type(other) == int or type(other) == float or type(other) == NumVal:
			return self * Pos([other] * len(self))
		if len(self) != len(other):
			raise KeyError('%s and %s are not the same dimensionality' % (self,other))
		cp = self.copy()
		for i in range(0, len(cp)):
			cp[i] *= other[i]
		return cp
	def __truediv__(self, other):
		if type(other) == str:
			return self.__truediv__(Pos(other))
		if type(other) == int or type(other) == float or type(other) == NumVal:
			return self.__truediv__(Pos([other] * len(self)))
		if len(self) != len(other):
			raise KeyError('%s and %s are not the same dimensionality' % (self,other))
		cp = self.copy()
		for i in range(0, len(cp)):
			cp[i] = NumVal(cp[i]) / NumVal(other[i])
		return cp
	def __floordiv__(self, other):
		if type(other) == str:
			return self.__floordiv__(Pos(other))
		if type(other) == int or type(other) == float or type(other) == NumVal:
			return self.__floordiv__(Pos([other] * len(self)))
		if len(self) != len(other):
			raise KeyError('%s and %s are not the same dimensionality' % (self,other))
		cp = self.copy()
		for i in range(0, len(cp)):
			cp[i] = NumVal(cp[i]) // NumVal(other[i])
		return cp
	def make_absolute(self, relative_to=None):
		cp = self.copy()
		if relative_to is not None:
			cp = cp - Pos(relative_to)
		cp.x = NumVal(cp.x).make_absolute()
		if cp.y is not None: cp.y = NumVal(cp.y).make_absolute()
		cp.z = NumVal(cp.z).make_absolute()
		return cp
	def make_relative(self, relative_to=None):
		cp = self.copy()
		if relative_to is not None:
			cp = cp - Pos(relative_to)
		cp.x = NumVal(cp.x).make_relative()
		if cp.y is not None: cp.y = NumVal(cp.y).make_relative()
		cp.z = NumVal(cp.z).make_relative()
		return cp
	def block_pos(self):
		cp = self.copy()
		for i in range(0, len(cp)):
			cp[i] = NumVal(cp[i]).block_pos()
		return cp
