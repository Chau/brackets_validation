# -*- coding:utf-8 -*-


BRACKETS = '{}[]()'
CLOSED_BRACKETS = ')]}'

PAIRS_DICT = {
	'(': ')',
	'[': ']',
	'{': '}'
}


class BracketValidationError(Exception):

	UNRESOLVED_TYPE_MSG = "Unresolved type of input params type. Resolved types are 'str', 'unicode'"
	EMPTY_STRING_MSG = "Empty string is not implemented in input params"
	UNRESOLVED_SYMBOLS_MSG = "Unresolved symbols in input param. Resolved symbols are (, ), [, ], {, }."


def validate(input_brackets):
	'''
	Дано: на входе строка, состоящая из скобок (, ), [, ], {, }.
	Надо определить является ли строка валидной по вложенности скобок
	[()]{} - валидная
	[{(]] - не валидная
	:param input_brackets: String
	'''

	# проверка входящей строки на валидный тип
	if type(input_brackets) not in (str, unicode):
		raise BracketValidationError(BracketValidationError.UNRESOLVED_TYPE_MSG)

	if not input_brackets:
		raise BracketValidationError(BracketValidationError.EMPTY_STRING_MSG)

	slen = len(input_brackets)

	# проверка на отсутствие левых символов
	for s in input_brackets:
		if s not in BRACKETS:
			raise BracketValidationError(BracketValidationError.UNRESOLVED_SYMBOLS_MSG)

	# если первый символ - закрывающая скобка
	if input_brackets[0] in CLOSED_BRACKETS:
		return False

	if slen % 2 == 1: # нечетное число символов в строке
		return False

	i = 0
	opened_brackets = [input_brackets[i]] # Список, содержащий только открывающие скобки.
	while opened_brackets or i < slen - 1:
		# Проходим по каждому символу входящей строки. Открывающие скобки добавляем в
		# список opened_brackets. Как только встречается закрывающая скобка, берем
		# последний элемента списка из opened_brackets и проверяем пару. Если пара совпадает,
		# то удаляем последний элемент из opened_brackets и продолжаем проверку,
		# в противном случае возвращаем False
		try:
			next_char = input_brackets[i+1]
		except IndexError:
			return False

		if next_char in CLOSED_BRACKETS:
			if opened_brackets and next_char == PAIRS_DICT.get(opened_brackets[-1]):
				opened_brackets.pop()
				i += 1
			else:
				return False
		else:
			opened_brackets.append(next_char)
			i += 1

	#
	if i + 1 == len(input_brackets):
		return True

	return False
		
	
	
	