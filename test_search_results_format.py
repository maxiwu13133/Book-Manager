from unittest import TestCase
from books import search_results_format


class TestSearchResultsFormat(TestCase):

    def test_search_results_format_one_result(self):
        number_of_results = 1
        list_of_dict = [{'author': 'Max', 'title': 'Games Guide', 'publisher': 'VAN', 'shelf': 2,
                         'category': 'Guide', 'subject': 'Games'}]
        expected = '1 results\n' \
                   '------------------------------------------\n' \
                   'Author: Max\n' \
                   'Title: Games Guide\n' \
                   'Publisher: VAN\n' \
                   'Shelf: 2\n' \
                   'Category: Guide\n' \
                   'Subject: Games\n' \
                   '------------------------------------------\n'
        actual = search_results_format(number_of_results, list_of_dict)
        self.assertEqual(expected, actual)

    def test_search_results_format_same_values(self):
        number_of_results = 3
        list_of_dict = [{'author': 'five', 'title': 'five', 'publisher': 'five', 'shelf': 'five',
                         'category': 'five', 'subject': 'five'},
                        {'author': 'five', 'title': 'five', 'publisher': 'five', 'shelf': 'five',
                         'category': 'five', 'subject': 'five'},
                        {'author': 'five', 'title': 'five', 'publisher': 'five', 'shelf': 'five',
                         'category': 'five', 'subject': 'five'}]
        expected = '3 results\n' \
                   '------------------------------------------\n' \
                   'Author: five\n' \
                   'Title: five\n' \
                   'Publisher: five\n' \
                   'Shelf: five\n' \
                   'Category: five\n' \
                   'Subject: five\n' \
                   '------------------------------------------\n' \
                   '------------------------------------------\n' \
                   'Author: five\n' \
                   'Title: five\n' \
                   'Publisher: five\n' \
                   'Shelf: five\n' \
                   'Category: five\n' \
                   'Subject: five\n' \
                   '------------------------------------------\n' \
                   '------------------------------------------\n' \
                   'Author: five\n' \
                   'Title: five\n' \
                   'Publisher: five\n' \
                   'Shelf: five\n' \
                   'Category: five\n' \
                   'Subject: five\n' \
                   '------------------------------------------\n'
        actual = search_results_format(number_of_results, list_of_dict)
        self.assertEqual(expected, actual)

    def test_search_results_format_empty_values(self):
        number_of_results = 2
        list_of_dict = [{'author': '', 'title': '', 'publisher': '', 'shelf': '', 'category': '',
                         'subject': ''},
                        {'author': '', 'title': '', 'publisher': '', 'shelf': '', 'category': '',
                         'subject': ''}]
        expected = '2 results\n' \
                   '------------------------------------------\n' \
                   'Author: \n' \
                   'Title: \n' \
                   'Publisher: \n' \
                   'Shelf: \n' \
                   'Category: \n' \
                   'Subject: \n' \
                   '------------------------------------------\n'\
                   '------------------------------------------\n' \
                   'Author: \n' \
                   'Title: \n' \
                   'Publisher: \n' \
                   'Shelf: \n' \
                   'Category: \n' \
                   'Subject: \n' \
                   '------------------------------------------\n'
        actual = search_results_format(number_of_results, list_of_dict)
        self.assertEqual(expected, actual)
