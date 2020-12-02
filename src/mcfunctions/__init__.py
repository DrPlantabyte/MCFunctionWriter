# version info
VERSION='0.1.0'
MAJOR, MINOR, BUILD = VERSION.split('.')

# imports
from sys import stdout, stderr

def _init():
	global _output_filestream
	_output_filestream = stdout

# I/O methods
def set_output(destination):
	global _output_filestream
	if _output_filestream is not None and hasattr(_output_filestream, 'close'):
		if _output_filestream != stdout and _output_filestream != stderr: # don't close std outputs!
			_output_filestream.close()
	if destination is None:
		_output_filestream = None
		return
	if hasattr(destination, 'write'):
		_output_filestream = destination
	else:
		_output_filestream = open(destination, 'w')
	return _output_filestream
def write_output(line):
	global _output_filestream
	if _output_filestream is not None:
		_output_filestream.write('%s\n' % line)
		if hasattr(_output_filestream, 'flush'):
			_output_filestream.flush()

#####
_init()