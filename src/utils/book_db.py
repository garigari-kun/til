
class BookDB():
    def titles(self):
        for id in database.keys():
            titles = [
                dict(id = id, title = database[id]['title']) for id in database.keys()
            ]
        return titles

    def get_info(self, id):
        return database.get(id, None)


database = {
    'id1': {
        'title': 'CherryPy Essentials: Rapid Python Web Application Development',
        'isbn': '978-1904811848',
        'publisher': 'Packt Publishing (March 31, 2007)',
        'author': 'Sylvain Hellegouarch',
    },
    'id2': {
        'title': 'Python for Software Design: How to Think Like a Computer Scientist',
        'isbn': '978-0521725965',
        'publisher': 'Cambridge University Press; 1 edition (March 16, 2009)',
        'author': 'Allen B. Downey',
    },
    'id3': {
        'title': 'Foundations of Python Network Programming',
        'isbn': '978-1430230038',
        'publisher': 'Apress; 2 edition (December 21, 2010)',
        'author': 'John Goerzen',
    },
    'id4': {
        'title': 'Python Cookbook, Second Edition',
        'isbn': '978-0-596-00797-3',
        'publisher': 'O''Reilly Media',
        'author': 'Alex Martelli, Anna Ravenscroft, David Ascher',
    },
    'id5': {
        'title': 'The Pragmatic Programmer: From Journeyman to Master',
        'isbn': '978-0201616224',
        'publisher': 'Addison-Wesley Professional (October 30, 1999)',
        'author': 'Andrew Hunt, David Thomas',
    },
    'id6': {
        'title': 'Learning scikit-learn: Machine Learning in Python',
        'isbn': '978-1783281930',
        'publisher': 'Packt Publishing (November 25, 2013)',
        'author': 'Raúl Garetta, Guillermo Moncecchi'
    }
}
