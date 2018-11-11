# -*- coding:utf-8 -*-

from unittest import TestCase

from brackets_validation import validate, BracketValidationError


class ValidateTest(TestCase):

    def test_success_1(self):
        self.assertTrue(validate('()'))

    def test_success_2(self):
        self.assertTrue(validate('{[()]}'))

    def test_success_3(self):
        self.assertTrue(validate('[()()]'))

    def test_success_4(self):
        self.assertTrue(validate('{()[]{}}'))

    def test_success_5(self):
        self.assertTrue(validate('{[()]}{[()]}{}'))

    def test_success_6(self):
        self.assertTrue(validate('[]{}()'))

    def test_success_7(self):
        self.assertTrue(validate('[{}({})]'))

    def test_odd_length_1(self):
        self.assertFalse(validate('('))

    def test_odd_length_2(self):
        self.assertFalse(validate('()]'))

    def test_odd_length_3(self):
        self.assertFalse(validate('{[()]}}'))

    def test_fail_1(self):
        self.assertFalse(validate('{([]})'))

    def test_fail_2(self):
        self.assertFalse(validate('[]{}()(]'))

    def test_fail_3(self):
        self.assertFalse(validate('[[[['))

    def test_fail_4(self):
        self.assertFalse(validate('))))'))

    def test_fail_5(self):
        self.assertFalse(validate('}]))'))

    def test_fail_6(self):
        self.assertFalse(validate('[[({'))

    def test_fail_7(self):
        self.assertFalse(validate('}([]'))

    def test_fail_8(self):
        self.assertFalse(validate('{}[('))

    def test_fail_9(self):
        self.assertFalse(validate('({)[}]'))

    def test_raise_empty(self):
        with self.assertRaises(BracketValidationError) as e:
            validate('')
        self.assertEqual(BracketValidationError.EMPTY_STRING_MSG,
                         str(e.exception))

    def test_raise_none(self):
        with self.assertRaises(BracketValidationError) as e:
            validate(None)
        self.assertEqual(BracketValidationError.UNRESOLVED_TYPE_MSG,
                         str(e.exception))

    def test_raise_unresolved_symbols(self):
        with self.assertRaises(BracketValidationError) as e:
            validate('f()]l')
        self.assertEqual(BracketValidationError.UNRESOLVED_SYMBOLS_MSG,
                         str(e.exception))

    def test_raise_unresolved_type(self):
        with self.assertRaises(BracketValidationError) as e:
            validate(3454)
        self.assertEqual(BracketValidationError.UNRESOLVED_TYPE_MSG,
                        str(e.exception))

# end