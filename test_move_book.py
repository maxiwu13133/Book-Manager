from unittest import TestCase
from unittest.mock import patch

from books import move_book


class TestMoveBook(TestCase):

    @patch('builtins.input', side_effect=['Guide', 'closet'])
    def test_move_book_shelf_is_string(self, mock_input):
        book_collection = [{'title': 'Guide', 'shelf': 2}]
        expected = [{'title': 'Guide', 'shelf': 'closet'}]
        actual = move_book(book_collection)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Guide', '2'])
    def test_move_book_shelf_is_same(self, mock_input):
        book_collection = [{'title': 'Guide', 'shelf': 2}]
        expected = [{'title': 'Guide', 'shelf': '2'}]
        actual = move_book(book_collection)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Guide', ''])
    def test_move_book_shelf_is_empty_string(self, mock_input):
        book_collection = [{'title': 'Guide', 'shelf': 2}]
        expected = [{'title': 'Guide', 'shelf': ''}]
        actual = move_book(book_collection)
        self.assertEqual(expected, actual)
