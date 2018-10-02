"""
TomeRater:
# Desciption:
    - class TomeRater manages the many methods of class User and class Book, 
      keeps records of users and books, and has methods to analyze object data 
    
# Method Organization:
    - Basic Methods
    - Analysis Methods
    - Extension Methods:
        - Input Validation
        - Dunder Methods
        - Advanced Analysis Methods
        - Get Creative!
"""
class TomeRater():
    
    """
    Basic Methods
    """
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        if(self.check_isbn_exists(isbn)): 
            print("Book with isbn {} already exists.  Cannot add this book again".format(isbn))
        else:
            return (Book(title, isbn))
    
    def create_novel(self, title, author, isbn):
        if(self.check_isbn_exists(isbn)): 
            print("Book with isbn {} already exists.  Cannot add this book again".format(isbn))
        else:
            return(Fiction(title, author, isbn))
    
    def create_non_fiction(self, title, subject, level, isbn):
        if(self.check_isbn_exists(isbn)): 
            print("Book with isbn {} already exists.  Cannot add this book again".format(isbn))
        else:
            return(Non_Fiction(title, subject, level, isbn))
    
    def add_user(self, name, email, user_books=None):
        if(email not in self.users.keys()):
            self.users[email] = User(name, email)
            if isinstance(user_books, list):
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("This user already exists.")
    
    def add_book_to_user(self, book, email, rating=None):
        if(email in self.users.keys()):
            self.users[email].read_book(book, rating)
            if(rating is not None):
                book.add_rating(rating)
            if(book in self.books.keys()):
                self.books[book] += 1
            elif(book not in self.books.keys()):
                self.books[book] = 1
        else:
            return("No user with email {email}!".format(email=email))
    
    
    """
    Analysis Methods
    """
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for user in self.users.values():
            print(user)
    
    def get_most_read_book(self):
        return(max(self.books, key=self.books.get))
    
    def highest_rated_book(self):
        max_avg_rating = 0
        rated_book = None
        for book in self.books:
            if max_avg_rating <= book.get_average_rating():
                max_avg_rating = book.get_average_rating()
                rated_book = book
            return rated_book   
        #return(str([book for book in self.books.keys() if book.get_average_rating() == max(rating.get_average_rating() for rating in self.books.keys())]).strip('[]'))
    
    def most_positive_user(self):
        '''
        max_avg_rating = 0
        rated_user = None
        for user in self.users:
            if max_avg_rating <= user.get_average_rating():
                max_avg_rating = user.get_average_rating()
                rated_user = user
            return rated_user
        '''
        return(str([user for user in self.users.values() if user.get_average_rating() == max(rating.get_average_rating() for rating in self.users.values())]).strip('[]'))
    
    
    """
    Extension Methods
    """
    # Input Validation
    def check_user_exists(self, username):
        return(bool(username in [username.get_username() for username in self.users.keys()]))
    
    def check_isbn_exists(self, isbn):
        return (bool(isbn in [book.get_isbn() for book in self.books.keys()]))
    
    def check_email_format(self, email):
        if '@' in email and (email.endswith('.com') or email.endswith('.edu') or email.endswith('.org')):
            return True
        return False
    
    # Dunder Methods
    def __repr__(self):
        print(
            "Number of Users: {users_count} \n" \
            "Number of Books: {books_count} \n" \
            "Total number of times books have been read: {reading_times} \n" \
            .format(
                users_count=len(self.users),
                books_count=len(self.books),
                most_read_book=self.most_read_book()))
    
    def __eq__(self, alternate_tomerater):
        return(bool((self.users == alternate_tomerater.users) and (self.books == alternate_tomerater.books)))
    
    def __hash__(self):
        return(hash((self.users, self.books)))
    
    
    # Advanced Analysis Methods

    def get_n_most_read_book(self, n):
        max_read = max(self.books.values())

        max_read_books = []

        for book, times_read in self.books.items():
            if (times_read == max_read):
                max_read_books.append(book)

        return(str(max_read_books).strip('[]'))
    
    def get_n_most_prolific_readers(self, n):
        if(0 < n):
			
            dictSortedUsers = {}
			
            for user in self.users.values():
                dictSortedUsers[user] = user.get_book_read_count()
                		
            dictSortedUsers = sorted(dictSortedUsers.items(), key=lambda key_value: key_value[1], reverse=True)[:n]
            
            for user, books_read_count in dictSortedUsers:
                print("{}\n".format(user))

            if n > len(self.users):
                print(
                    "Only printed: {count}\n" \
                    "Didn't print the remaining {remaining}, because there is not enough data." \
                    .format(
                        count=len(self.users),
                        remaining=n - len(self.users)
                    )
                )
        else:
            return("Expected intLimiter argument to be greater than one, got less than one.")

    
    #def get_n_most_expensive_books():
        #pass
    
    #def get_worth_of_user():
        #pass
    
    
    # Creativity
    #def creative_swag():
        #pass



"""
User:
# Desciption:
    - class User handles attributes associated with users
#Method Organization:
    - Basic Methods
    - Additional Methods
"""
class User():
    
    """
    Basic Methods
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    
    def get_email(self):
        return (self.email)
    
    def change_email(self, new_email):
        self.email = new_email
        print('email updated to ', str(self.email))
    
    def get_username(self):
        return(self.name)
    
    def set_username(self, new_username):
        self.name = new_username
    
    def __repr__(self):
        return(
            "User: {username}\n" \
            "Email: {email}\n" \
            "Books read: {books}\n" \
            .format(
                username=self.name,
                email=self.email,
                books=len(self.books)
            )
        )
    
    def __eq__(self, alternate_user):
        return(bool((self.name == alternate_user.get_username()) and (self.email == alternate_user.email)))
    
    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        values = [val for val in self.books.values() if val is not None]
        return sum(values)/len(values)

    
    """
    Additional Methods
    """
    def read_book(self, title, rating=None):
        self.books[title] = rating
    
    def get_average_rating(self):
        return(float(sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)))

"""
Book:
# Desciption:
    - class User handles attributes associated with books
# Method Organization:
    - Basic Methods
    - Additional Methods
"""
class Book(object):
    
    """
    Basic Methods
    """
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = None
    
    def get_title(self):
        return(self.title)
    
    def get_isbn(self):
        return(self.isbn)
    
    def set_title(self, new_title):
        self.title = new_title
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
    
    def add_rating(self, rating):
        try:
            if (0 <= rating <= 4):
                self.ratings.append(rating)
            else:
                return("Invalid Rating.")
        except TypeError:
            print("Invalid Type.")
    
    def __eq__(self, alternate):
        return((self.title == alternate.title) and (self.isbn == alternate.isbn))
    """
    Additional Methods
    """
    def get_average_rating(self):
        return(float((sum([rating for rating in self.ratings])) / (len(self.ratings))))
    
    def __hash__(self):
        return(hash((self.title, self.isbn)))

    def __repr__(self):
        return(
            "Title: {title}\n" \
            "ISBN: {isbn}\n" \
            .format(
                title=self.title,
                isbn=self.isbn
            )
        )
"""
Fiction:
# Description
    - class Fiction is a subclass of book, and inherits title and author attributes,
      defines a class Fiction specific attribute: author
# Method Organization:
    - Basic Methods
"""
class Fiction(Book):
    
    """
    Basic Methods
    """
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return(self.author)
    
    def __repr__(self):
        return(
            "{title} by {author}\n".format(
                title=self.title,
                author=self.author))

"""
Non-Fiction:
# Desciption:
    - class NoN_Fiction is a subclass of book, and inherits title and author attributes,
      defines a class Non_Fiction specific attributes: subject, and level
# Method Organization:
    - Basic Methods
"""
class Non_Fiction(Book):
    
    """
    Basic Methods
    """
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return(self.subject)
    
    def get_level(self):
        return(self.level)
    
    def __repr__(self):
        return(
            "{title}, a {level} manual on {subject}".format(
                title=self.title,
                subject=self.subject,
                level=self.level))
    
