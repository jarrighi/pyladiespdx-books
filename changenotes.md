# Changes on 7/6-7

The following notes describe the commits I made on the night of 7/6

---
### modify database settings method to use with Heroku

```
commit c10393517d8da52a89258a6234a899cca600c23e
Author: Jules Arrighi <juliana.arrighi@gmail.com>
Date:   Mon Jul 6 22:27:27 2015 -0700

    modify database settings method to use with Heroku
```

This was necessary to get the app to find the database on heroku. Because of this change you must now `export DATABASE_URL="postgres://localhost/librarpy"` locally.

---

### Add books to db on form submit

```
commit e3a1fc04b80088088504268f1fff680e0887b8c0
Author: Jules Arrighi <juliana.arrighi@gmail.com>
Date:   Mon Jul 6 23:11:53 2015 -0700

    Add books to db on form submit
```

I said a few things wrong in our pairing session earlier, so I had to fix some bugs in the add_book.html template. Then I added a new route/view to handle the data from the form and create a new Book record based on that data. Then the browser is redirected to the main page.

---

### Books in main list link ot detail pages

```
commit a9599109c452c4883173ff0661df9c30d6fa7642
Author: Jules Arrighi <juliana.arrighi@gmail.com>
Date:   Mon Jul 6 23:22:14 2015 -0700

    Books in main list link ot detail pages
```

I added the id to the data that is passed into the main book list so that each item in that list couls also use the id to create a link to the book detail page. I also added a link on the main page to create a new book, which links to the /books/new page.

---

### Make book detail page look up actualy book details

```
commit abd34da2c96e216ba25564d2acb29b29e658a1c1
Author: Jules Arrighi <juliana.arrighi@gmail.com>
Date:   Mon Jul 6 23:27:19 2015 -0700

    Make book detail page look up actualy book details
```

Now the book detail view is actually querying the database to get the data instead of just using dummy data. 

---

### Create a field for possessor in the models and make relevant updates througout app

```
commit 5daa123198d479314d3da97e9fbf77ca973213e0
Author: Jules Arrighi <juliana.arrighi@gmail.com>
Date:   Tue Jul 7 00:05:30 2015 -0700

    Create a field for possessor in the models and make relevant updates througout app
```


There is a database migration. You will need to run

```
python manage.py db upgrade
```

Also with this migration, if you already had data in your database, you will have to manually update the possessor attribute. You can do this in the python shell. This is how I did it:


```
$ python
Python 2.7.8 (default, Oct 19 2014, 16:06:28)
[GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db, models
>>> query = db.session.query(models.Book)
>>> for item in query:
...     print item
...
<id 1>
<id 2>
<id 3>
<id 4>
<id 5>
>>> for item in query:
...     item.possessor = "Jules"
...
>>> for item in query:
...     print item.possessor
...
Jules
Jules
Jules
Jules
Jules
>>> db.session.add_all(query)
>>> db.session.commit()
```
