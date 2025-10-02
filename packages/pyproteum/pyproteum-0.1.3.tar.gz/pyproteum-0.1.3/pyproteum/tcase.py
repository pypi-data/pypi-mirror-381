import sys
import os, types
from pyproteum.models.models import *
import unittest
import importlib.util

from pyproteum.moperators.myoperator import *
from pyproteum.utiles import red,green,get_test_files_with_discover



def change_dir_connect(d, session_name):
	print('Session: ', session_name)
	try :
		if d:
			os.chdir(d)
			sys.path.append(os.getcwd())
		database = SqliteDatabase(session_name+'.db')
		db.initialize(database)  # aqui o proxy é vinculado ao banco real
		db.pragma('foreign_keys', 1, permanent=True)
	except Exception as ex:
		print(red('Error: test session not found'))
		print(red(ex))
		sys.exit()


def _ensure_module_hierarchy(path_filename):
	"""
	Garante que a hierarquia de pacotes/módulos existe em sys.modules
	e retorna (fullname, parent).
	
	Exemplo:
	"path/arquivo.py" -> cria "path.arquivo"
	"""
	module_name = os.path.splitext(path_filename)[0].replace(os.sep, ".")
	parts = module_name.split(".")

	parent = None
	fullname = ""
	for part in parts[:-1]:
		fullname = f"{fullname}.{part}" if fullname else part
		if fullname not in sys.modules:
			package = types.ModuleType(fullname)
			package.__path__ = []  # marca como pacote
			sys.modules[fullname] = package
			if parent is not None:
				setattr(parent, part, package)
		parent = sys.modules[fullname]

	return module_name, parent, parts

def load_modulex(filename):
	nome_modulo = os.path.splitext(os.path.basename(filename))[0]
	spec = importlib.util.spec_from_file_location(nome_modulo, filename)
	modulo = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(modulo)
	return modulo

def load_module(filename):
	module_name, parent, parts = _ensure_module_hierarchy(filename)

	spec = importlib.util.spec_from_file_location(module_name, filename)
	modulo = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(modulo)

	sys.modules[module_name] = modulo
	if parent is not None:
		setattr(parent, parts[-1], modulo)

	return modulo

def get_test_names(filename):
	module = load_module(filename)
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromModule(module)
	tests = []
	for test_group in suite:
		for test in test_group:
			tests.append(test.id())
	return sorted(tests)

def __add():
	session_name = sys.argv[-1]
	directory = None
	tests = []
	i = 2
	while i < len(sys.argv[:-2]):
		s = sys.argv[i]
		match s:
			case '--D':
				i += 1
				directory = sys.argv[i]
			case '--S':
				i += 1
				tests.append(sys.argv[i])
			case '--discover':
				i += 1
				vnd = get_test_files_with_discover(sys.argv[i])
				tests += vnd 
			case _:
				usage()
				return
		i += 1

	
	if len(tests) == 0:
		tests = ['test_'+session_name+'.py']
	
	change_dir_connect(directory, session_name)

	for test_file in tests:
		try :
			test_names = get_test_names(test_file)
			TestCase.create(filename=test_file)
		except Exception as ex:
			print(red(f'Error: can not insert test file {test_file}'))
			print(red(ex))
			continue

		print(f'\nTests form file {test_file}')
		i = 1
		for t in test_names:
			t = t.split('.')[-1]
			print(f'\t{i}) {t}')
			i += 1


def __list():
	session_name = sys.argv[-1]
	directory = None
	tests = []
	i = 2
	while i < len(sys.argv[:-2]):
		s = sys.argv[i]
		match s:
			case '--D':
				i += 1
				directory = sys.argv[i]
			case _:
				usage()
				return
		i += 1

	
	change_dir_connect(directory, session_name)


	k = 1
	nn = len(TestCase)
	for test_file in TestCase:
		test_file = test_file.filename
		try :
			test_names = get_test_names(test_file)
		except Exception as ex:
			print(red(f'Error: can not find test file {test_file}'))
			print(red(ex))
			continue

		print(f'\nTests form file {test_file} ({k})')
		i = 1
		for t in test_names:
			t = t.split('.')[-1]
			print(f'\t{k}:{i}) {t}')
			i += 1
		k += 1


def get_all_test_names():
	k = 1
	all = []
	for test_file in TestCase:
		test_file = test_file.filename
		try :
			test_names = get_test_names(test_file)
			all += test_names
		except Exception as ex:
			print(red(f'Error: can not find test file {test_file}'))
			print(red(ex))
			continue

		k += 1
	return all



def __delete():
	session_name = sys.argv[-1]
	directory = None
	tests = []
	i = 2
	while i < len(sys.argv[:-2]):
		s = sys.argv[i]
		match s:
			case '--D':
				i += 1
				directory = sys.argv[i]
			case '--S':
				i += 1
				tests.append(sys.argv[i])
			case '--discover':
				i += 1
				vnd = get_test_files_with_discover(sys.argv[i])
				tests += vnd 			
			case _:
				usage()
				return
		i += 1

	if len(tests) == 0:
		tests = ['test_'+session_name+'.py']
	
	change_dir_connect(directory, session_name)

	k = 1
	for test_file in tests:
		try:
			tc = TestCase.get(TestCase.filename == test_file)
			tc.delete_instance()
			print(f'Succesfuly removed "{test_file}"')
		except TestCase.DoesNotExist:
			print(red(f'No file "{test_file}" found.'))

def main():
	n = len(sys.argv)-2
	if n < 1:
		usage()
	
	if sys.argv[1] == '--add':
		__add()
		return
	elif sys.argv[1] == '--del':
		__delete()
		return	
	elif sys.argv[1] == '--list':
		__list()
		return 
	else:
		usage()

 
def usage():
	print('Usage:')
	print('tcase --add [--D <directory> ] [--S <test file name> ... ] [--discover <directory name>] <session name>')
	print('tcase --del [--D <directory> ] [--S <test file name> ...]  <session name>')
	print('tcase --list [--D <directory> ]  <session name>')
	sys.exit()


if __name__ == '__main__' :
	main()
