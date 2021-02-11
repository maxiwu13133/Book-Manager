"""
COMP 1510
Maximilian Wu
A01208571
Book collection manager.
"""


def SEARCH_NUMBER():
    search_number = (1, 2, 3, 4, 5, 6)
    return search_number


def SEARCH_TERMS():
    search_terms = {1: 'author', 2: 'title', 3: 'publisher', 4: 'shelf', 5: 'category', 6: 'subject'}
    return search_terms


def quit_books(results):
    """Store data user searched in a file

    :param results: a string
    :postcondition: dumps all data into a plaintext file
    :return:
    """
    filename = 'programming.txt'
    with open(filename, 'w', encoding='UTF-16') as file_object:
        file_object.write(results)

    quit()


def load_data():
    """Separate information coloumns from file and put into list in order

    :precondition: include a file for load_data() to read
    :postcondition: converts file content into string
    :return: a string
    """
    filename = 'books.txt'
    with open(filename, encoding='windows-1251') as file_object:
        for _ in file_object:
            file = file_object.readlines()

        return file


def books(file):
    r"""Store data from load_data() into lists of dictionaries

    :param file: a string
    :precondition: contents must be separated by \t
    :postcondition: groups information per line into dictionary into list
    :return: a list of dictionaries

    >>> books(['Max\tGames Guide\tVAN\t2\tGuide\tGames'])
    [{'author': 'Max', 'title': 'Games Guide', 'publisher': 'VAN', 'shelf': '2', 'category': 'Guide', 'subject': 'Games'}]
    >>> books(['Max\tGames Guide\tVAN\t2\tGuide\tGames', 'Duncan\tKingdom Warriors\tBD&L\t3\tFantasy\tFiction'])
    [{'author': 'Max', 'title': 'Games Guide', 'publisher': 'VAN', 'shelf': '2', 'category': 'Guide', 'subject': 'Game'}, {'author': 'Duncan', 'title': 'Kingdom Warriors', 'publisher': 'BD&L', 'shelf': '3', 'category': 'Fantasy', 'subject': 'Fiction'}]
    """
    book_list = []

    for index in file:
        if index != file[-1]:
            index = index[:-1]
        book_dict = zip(SEARCH_TERMS().values(), index.split('\t'))
        book_list.append(dict(book_dict))

    return book_list


def move_book(book_collection):
    """Move book to a new location

    :param book_collection: a list of dictionaries
    :precondition: dictionary must have 'title' and 'shelf' as keys
    :postcondition: shelf key in dictionary will have the new value of new_location
    :return: a list of dictionaries
    """
    results = 0
    indices_counter = 0
    target_book_index = 0
    target_book = input('Enter the title of the book:\n').strip().title()

    for index in book_collection:
        indices_counter += 1

        if target_book in index['title']:
            results += 1
            target_book_index = indices_counter - 1

    if results != 1:
        print('Only one book can be moved at a time, please be more precise next time!\n')
        return book_collection

    new_location = input('Enter a new shelf to move to:\n')
    replacement_book = book_collection[target_book_index]
    replacement_book['shelf'] = new_location
    book_collection[target_book_index] = replacement_book
    return book_collection


def search_results_format(results_number, search_results):
    r"""Format results into numbered list with number of results above

    :param results_number: a positive integer
    :param search_results: a list
    :precondition: list indices must be a dictionary with author, title, pulisher, shelf, category,
                   and subject as keys
    :postcondition: formats results for easier reading
    :return: a string

    >>> search_results_format(1, [{'author': 'Max', 'title': 'Games Guide', 'publisher': 'VAN', 'shelf': 2, 'category': 'Guide', 'subject': 'Games'}])
    '1 results\n------------------------------------------\nAuthor: Max\nTitle: Games Guide\nPublisher: VAN\nShelf: 2\nCategory: Guide\nSubject: Games\n------------------------------------------\n'
    """
    results = ''
    for index in search_results:
        results += f'------------------------------------------\nAuthor: {index["author"]}\n' \
                   f'Title: {index["title"]}\nPublisher: {index["publisher"]}\n' \
                   f'Shelf: {index["shelf"]}\nCategory: {index["category"]}\n' \
                   f'Subject: {index["subject"]}\n------------------------------------------\n'

    display = f'{str(results_number)} results\n{results}'
    return display


def search(menu_selection: int, library):
    """Prompt user for keyword and search accordingly

    :param menu_selection: an integer
    :precondition: must be a positive integer between 1 to 6 inclusive
    :param library: a list of dictionaries
    :precondition: dictionaries must have 6 key-value pairs
    :postcondition: fetches results from books()
    :return: the number of results, a string of the results
    """
    search_string = input('Enter a search string:\n').strip().lower()
    results = []
    results_num = 0

    for index in library:
        if search_string in index[SEARCH_TERMS()[menu_selection]].lower():
            results.append(index)
            results_num += 1

    return results_num, results


def menu():
    """Prompt user for options

    :postcondition: calls search function to search, move_book function to move books,
                    and quit_books to quit
    """
    total_results = ''
    book_list = books(load_data())
    while True:
        choice = int(input('1. Search by author\n2. Search by title\n3. Search by publisher\n'
                           '4. Search by shelf\n5. Search by category\n6. Search by subject\n'
                           '7. Move a book\n8. Quit\nEnter a number:\n'))

        if choice in SEARCH_NUMBER():
            num, results = search(menu_selection=choice, library=book_list)
            total_results += search_results_format(results_number=num, search_results=results)
            print(search_results_format(results_number=num, search_results=results))

        elif choice == 7:
            book_list = move_book(book_list)

        elif choice == 8:
            quit_books(total_results)


def main():
    """
    Execute the program
    """
    # import doctest
    # doctest.testmod()
    menu()


if __name__ == "__main__":
    main()
