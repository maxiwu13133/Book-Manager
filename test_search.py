from unittest import TestCase
from unittest.mock import patch

from books import search


class TestSearch(TestCase):

    @patch('builtins.input', side_effect=['ookkee'])
    def test_search_1_list_index(self, mock_input):
        menu_selection = 2
        library = [{'author': 'Max', 'title': 'The Bookkeeper', 'publisher': 'VAN', 'shelf': 2,
                    'category': 'Guide', 'subject': 'Games'}]
        expected = 1, [{'author': 'Max', 'title': 'The Bookkeeper', 'publisher': 'VAN', 'shelf': 2,
                        'category': 'Guide', 'subject': 'Games'}]
        actual = search(menu_selection, library)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    def test_search_1_list_index_empty_string(self, mock_input):
        menu_selection = 4
        library = [{'author': '', 'title': '', 'publisher': '', 'shelf': '',
                    'category': '', 'subject': ''}]
        expected = 1, [{'author': '', 'title': '', 'publisher': '', 'shelf': '',
                        'category': '', 'subject': ''}]
        actual = search(menu_selection, library)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['fIOnd34Skj'])
    def test_search_input_not_in_dicts(self, mock_input):
        menu_selection = 3
        library = [{'author': 'Joe', 'title': 'Dictionary', 'publisher': 'VAN', 'shelf': 6,
                    'category': 'Info', 'subject': 'English'},
                   {'author': 'Dan', 'title': 'Picture Book', 'publisher': 'GTT',
                    'shelf': 'Island', 'category': 'Visual', 'subject': 'Art'},
                   {'author': 'Hank', 'title': 'Games', 'publisher': 'Y8', 'shelf': 1,
                    'category': 'Guide', 'subject': 'Games'}]
        expected = 0, []
        actual = search(menu_selection, library)
        self.assertEqual(expected, actual)