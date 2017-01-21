import unittest
from multiset import *


class TestMultiSet(unittest.TestCase):
    '''Inherit from the unittest class. Form test cases to check the methods
    in the targetted file.
    '''

    def test_contains_int(self):
        '''Test whether the __contains__ will work only with the int
        '''
        # initiate the multiset
        multiset1 = MultiSet()
        e = 2
        # insert e
        multiset1.content.insert(e)
        expected_value = True
        # check if e is in the multiset1
        self.assertEqual(e in multiset1, expected_value)

    def test_contains_str(self):
        '''Test whether the __contains__ will work only with the str
        '''
        # initiate the multiset
        multiset1 = MultiSet()
        e = 'Hello'
        # insert e
        multiset1.content.insert(e)
        expected_value = True
        # check whether e is in the multiset
        self.assertEqual(e in multiset1, expected_value)

    def test_count_int(self):
        # initiate the multiset
        multiset1 = MultiSet()
        e = 2
        num_repeat = 5
        # repeat the e with the pre-defined numbers of times
        for index in range(num_repeat):
            multiset1.insert(e)
        # check if it fits the number of times
        self.assertEqual(multiset1.count(e), num_repeat)

    def test_count_str(self):
        # initiate the multiset
        multiset1 = MultiSet()
        e = 'Hello'
        num_repeat = 5
        # repeat the e with the pre_defined numbers of times
        for index in range(num_repeat):
            multiset1.insert(e)
        # check if it fits the number of times
        self.assertEqual(multiset1.count(e), num_repeat)

    def test_insert_int(self):
        # initiate the multiset
        multiset1 = MultiSet()
        e = 5
        # insert the elements
        multiset1.insert(e)
        expected_value = True
        # see whether the element is inserted
        self.assertEqual(e in multiset1, expected_value)

    def test_insert_multiple_int(self):
        multiset1 = MultiSet()
        for e in range(0, 5):
            multiset1.insert(e)
        expected_value = [True, True, True, True, True]
        return_value = []
        for e in range(0, 5):
            return_value.append(e in multiset1)
        self.assertEqual(return_value, expected_value)

    def test_insert_str(self):
        multiset1 = MultiSet()
        e = 'Hello'
        multiset1.insert(e)
        expected_value = True
        self.assertEqual(e in multiset1, expected_value)

    def test_insert_multiple_str(self):
        multiset1 = MultiSet()
        insert_word = 'Hello'
        for e in insert_word:
            multiset1.insert(e)
        expected_value = [True, True, True, True, True]
        result_value = []
        for e in insert_word:
            result_value.append(e in multiset1)
        self.assertEqual(result_value, expected_value)

    def test_remove_int(self):
        multiset1 = MultiSet()
        for e in range(0, 5):
            multiset1.insert(e)
        multiset1.remove(4)
        expected_value = '{0, 1, 2, 3}'
        self.assertEqual(multiset1.__str__(), expected_value)

    def test_remove_multiple_int(self):
        multiset1 = MultiSet()
        for e in range(0, 5):
            multiset1.insert(e)
        for e in range(2, 4):
            multiset1.remove(e)
        expected_value = '{0, 1, 4}'
        self.assertEqual(multiset1.__str__(), expected_value)

    def test_remove_str(self):
        multiset1 = MultiSet()
        insert_word = {'Brian', 'Anna', 'Nick', 'CodeMangler'}
        for e in insert_word:
            multiset1.insert(e)
        multiset1.remove('CodeMangler')
        expected_value = '{Anna, Brian, Nick}'
        self.assertEqual(multiset1.__str__(), expected_value)

    def test_remove_multiple_str(self):
        multiset1 = MultiSet()
        insert_word = {'Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams'}
        for e in insert_word:
            multiset1.insert(e)
        multiset1.remove('CodeMangler')
        multiset1.remove('Brian')
        expected_value = '{Anna, Exams, Nick}'
        self.assertEqual(multiset1.__str__(), expected_value)

    def test_clear_str(self):
        multiset1 = MultiSet()
        insert_word = {'Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams'}
        for e in insert_word:
            multiset1.insert(e)
        multiset1.clear()
        self.assertEqual(multiset1.__str__(), '{}')

    def test_clear_int(self):
        multiset1 = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        multiset1.clear()
        self.assertEqual(multiset1.__str__(), '{}')

    def test_len_empty(self):
        multiset1 = MultiSet()
        self.assertEqual(len(multiset1), 0)

    def test_len_int(self):
        multiset1 = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        self.assertEqual(len(multiset1), 5)

    def test_len_str(self):
        multiset1 = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams']:
            multiset1.insert(e)
        self.assertEqual(len(multiset1), 5)

    def test_repr_empty(self):
        multiset1 = MultiSet()
        self.assertEqual(repr(multiset1), 'MultiSet([])')

    def test_repr_int(self):
        multiset1 = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        self.assertEqual(repr(multiset1), 'MultiSet([0, 1, 2, 3, 4])')

    def test_repr_str(self):
        multiset1 = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams']:
            multiset1.insert(e)
        self.assertEqual(repr(multiset1),
                         'MultiSet([Anna, Brian, CodeMangler, Exams, Nick])')

    def test_eq_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        self.assertEqual(multiset1 == multiset2, True)

    def test_eq_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams']:
            multiset1.insert(e)
            multiset2.insert(e)
        self.assertEqual(multiset1 == multiset2, True)

    def test_repr_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in range(5):
            multiset1.insert(e)
            multiset2.insert(e)
        self.assertEqual(multiset1 == multiset2, True)

    def test_le_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        self.assertEqual(multiset1 <= multiset2, True)

    def test_le_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams']:
            multiset1.insert(e)
            multiset2.insert(e)
        multiset2.insert('Yes')
        self.assertEqual(multiset1 <= multiset2, True)

    def test_le_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in range(5):
            multiset1.insert(e)
            multiset2.insert(e)
        multiset2.insert(5)
        self.assertEqual(multiset1 <= multiset2, True)

    def test_sub_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        self.assertEqual(multiset1 - multiset2, return_multiset)

    def test_sub_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams']:
            multiset1.insert(e)
            multiset2.insert(e)
        multiset1.insert('Yes')
        return_multiset.insert('Yes')
        self.assertEqual((multiset1 - multiset2).__str__(),
                         return_multiset.__str__())

    def test_sub_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
            multiset2.insert(e)
        multiset1.insert(5)
        return_multiset.insert(5)
        self.assertEqual((multiset1 - multiset2).__str__(),
                         return_multiset.__str__())

    def test_isub_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        multiset1 -= multiset2
        self.assertEqual(multiset1.__str__(), return_multiset.__str__())

    def test_isub_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams']:
            multiset1.insert(e)
            multiset2.insert(e)
        multiset1.insert('Yes')
        return_multiset.insert('Yes')
        multiset1 -= multiset2
        self.assertEqual(multiset1.__str__(),
                         return_multiset.__str__())

    def test_isub_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
            multiset2.insert(e)
        multiset1.insert(5)
        return_multiset.insert(5)
        multiset1 -= multiset2
        self.assertEqual(multiset1.__str__(), return_multiset.__str__())

    def test_add_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        self.assertEqual(multiset1 + multiset2, return_multiset)

    def test_add_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams', 'Yes']:
            multiset1.insert(e)
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams', 'CSCA48']:
            multiset2.insert(e)
        return_multiset.insert('Brian')
        return_multiset.insert('CSCA48')
        return_multiset.insert('Yes')
        self.assertEqual((multiset1 + multiset2).__str__(),
                         return_multiset.__str__())

    def test_add_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        for e in range(1, 6):
            multiset2.insert(e)
        return_multiset.insert(0)
        return_multiset.insert(5)
        self.assertEqual(multiset1 + multiset2, return_multiset)

    def test_iadd_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        multiset1 += multiset2
        return_multiset = MultiSet()
        self.assertEqual(multiset1, return_multiset)

    def test_iadd_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams', 'Yes']:
            multiset1.insert(e)
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams', 'CSCA48']:
            multiset2.insert(e)
        multiset1 += multiset2
        return_multiset.insert('Brian')
        return_multiset.insert('CSCA48')
        return_multiset.insert('Yes')
        self.assertEqual((multiset1).__str__(),
                         return_multiset.__str__())

    def test_iadd_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        for e in range(1, 6):
            multiset2.insert(e)
        multiset1 += multiset2
        return_multiset.insert(0)
        return_multiset.insert(5)
        self.assertEqual(multiset1, return_multiset)

    def test_and_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        self.assertEqual(multiset1 & multiset2, return_multiset)

    def test_and_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams', 'Yes']:
            multiset1.insert(e)
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams', 'CSCA48']:
            multiset2.insert(e)
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams']:
            return_multiset.insert(e)
        self.assertEqual((multiset1 & multiset2).__str__(),
                         return_multiset.__str__())

    def test_and_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        for e in range(1, 6):
            multiset2.insert(e)
        for e in range(1, 5):
            return_multiset.insert(e)
        self.assertEqual(multiset1 & multiset2, return_multiset)

    def test_iand_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        multiset1 &= multiset2
        return_multiset = MultiSet()
        self.assertEqual(multiset1, return_multiset)

    def test_iand_str(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams', 'Yes']:
            multiset1.insert(e)
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams', 'CSCA48']:
            multiset2.insert(e)
        multiset1 &= multiset2
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams']:
            return_multiset.insert(e)
        self.assertEqual(multiset1.__str__(),
                         return_multiset.__str__())

    def test_iand_int(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        for e in range(1, 6):
            multiset2.insert(e)
        multiset1 &= multiset2
        for e in range(1, 5):
            return_multiset.insert(e)
        self.assertEqual(multiset1, return_multiset)

    def test_disjoint_empty(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        self.assertEqual(multiset1.isdisjoint(multiset2), True)

    def test_disjoint_str_False(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams', 'Yes']:
            multiset1.insert(e)
        for e in ['Anna', 'Nick', 'CodeMangler', 'Exams', 'CSCA48']:
            multiset2.insert(e)
        self.assertEqual(multiset1.isdisjoint(multiset2),
                         False)

    def test_disjoint_str_True(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in ['Brian', 'Anna', 'Nick', 'CodeMangler', 'Exams', 'Yes']:
            multiset1.insert(e)
        for e in ['Kenneth', 'Giovanna', 'CSCA48']:
            multiset2.insert(e)
        self.assertEqual(multiset1.isdisjoint(multiset2),
                         True)

    def test_disjoint_int_False(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        return_multiset = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        for e in range(1, 6):
            multiset2.insert(e)
        self.assertEqual(multiset1.isdisjoint(multiset2), False)

    def test_disjoint_int_True(self):
        multiset1 = MultiSet()
        multiset2 = MultiSet()
        for e in range(5):
            multiset1.insert(e)
        for e in range(9, 17):
            multiset2.insert(e)
        self.assertEqual(multiset1.isdisjoint(multiset2), True)


unittest.main(exit=False)
