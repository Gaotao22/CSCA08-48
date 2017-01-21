import unittest
from ex9_code import *


class TestHeaps(unittest.TestCase):

    def test_is_empty(self):
        test_list = []
        my_heap = Heap(test_list)
        self.assertEqual(my_heap.is_empty(), True)

    def test_insert_non_root(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        my_heap.insert(3)
        self.assertEqual(my_heap._heap, [9, 6, 8, 5, 1, 4, 3])

    def test_insert_root(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        my_heap.insert(10)
        self.assertEqual(my_heap._heap, [10, 6, 9, 5, 1, 4, 8])

    def test_insert_to_empty(self):
        my_heap = Heap([])
        my_heap.insert(10)
        self.assertEqual(my_heap._heap, [10])

    def test_bubble_up(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        my_heap._heap.append(10)
        my_heap._bubble_up(len(my_heap._heap) - 1)
        self.assertEqual(my_heap._heap, [10, 6, 9, 5, 1, 4, 8])

    def test_bubble_up_empty(self):
        my_heap = Heap([])
        my_heap._bubble_up(len(my_heap._heap) - 1)
        self.assertEqual(my_heap._heap, [])

    def test_swap_different_level(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        my_heap._swap(1, 3)
        self.assertEqual(my_heap._heap, [9, 5, 8, 6, 1, 4])

    def test_swap_same_level(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        my_heap._swap(4, 5)
        self.assertEqual(my_heap._heap, [9, 6, 8, 5, 4, 1])

    def test_remove_top(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        self.assertEqual(my_heap.remove_top(), 9)

    def test_remove_top_single(self):
        my_heap = Heap([5])
        self.assertEqual(my_heap.remove_top(), 5)

    def test_bubble_down(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        my_heap._heap.pop(0)
        my_heap._bubble_down(0)
        self.assertEqual(my_heap._heap, [8, 6, 5, 1, 4])

    def test_bubble_down_single(self):
        my_heap = Heap([5])
        my_heap._heap.pop(0)
        my_heap._bubble_down(0)
        self.assertEqual(my_heap._heap, [])

    def test_violates_bigger_than_length(self):
        my_heap = Heap([5, 8, 9, 6, 1, 4])
        self.assertEqual(my_heap._violates(4), False)

    def test_violates_one_child(self):
        my_heap = Heap([5, 8, 9])
        my_heap._heap.pop(0)
        self.assertEqual(my_heap._violates(0), True)

    def test_violates_two_children(self):
        my_heap = Heap([5, 8, 9, 6, 1, 10])
        my_heap._heap.pop(0)
        self.assertEqual(my_heap._violates(0), True)


unittest.main(exit=False)
