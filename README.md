README.md
======

LibrarPy is a project to begin a working library amongst Portland PyLadies.  We have
been given a number of technical manuals and other books and have structured a way
for these books to be safely lent out and tracked so that all may benefit.

We would like to break this project into first several smaller sub-components,
then break those into several more, and so forth, in order to make the project
approachable for group members who would like to lend their support (or potentially
first FOSS contribution!) to this future web app.

====

DRAFT: What our product does.

Structure
- Hosted on Heroku FTTB
- Dev environment process & creation
- Flask python web framework
- Postgres DB
- bootstrap/skeleton css framework

Components
- Book Model
- User Model
- Pages: sign-up, sign-in, log out, book list, book detail per entry (with request),
profile, about Library ... (PyBrary?)
- static folder of css/JS/images.
- Tests

Features
- Who has a book right now?
- What books are available/checked out?
- How many books are "checked out"?
- Granular user data: how long has a given user had a book checked out & its info
- Checkout process
- External user creation
- login/auth
- User-designated availability
- Availability "switch" after (x) weeks (or notification)
 - this is a bigger problem :)
 - simplification (for now): "who has the book?  rachel.  go bug her.  BYE"



last (re)-created 12/29/2014
