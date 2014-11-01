===========================
Guidelines for Contributing
===========================

Please review all of this page before starting work on a patch

Coding Style
------------
To keep things simple, we will be using the style outlined by the `PEP8 Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008/>`_

Documentation
-------------
Keeping the documentation current, complete and correct is of utmost importance. If you change or add a feature, it must be documented. 

Of course, your contribution may be documentation itself! Yea! We love this. You will simply issue a :doc:`pull request <pullrequest>`, for the piece of documentation you have added. This may be a great place to start if you are new to programming or open source projects. Take a look at the existing documentation, and use this as a guide as to how to structure your addition. Unless you are adding whole new sections, there should be sufficient examples here. You may also have a look at the `project wiki <https://github.com/jarrighi/pyladiespdx-books/wiki>`_ for further resources.

If you are contributing code, a patch submission will not be accepted without proper documentation (but don't worry, we will help you with this if you need it!). For example, this could be simply adding the correctly formatted docstring to your new class or function.

We are using the `Sphinx <http://sphinx-doc.org/>`_ documentation system, which employs `reStructuredText <http://sphinx-doc.org/rest.html#rst-primer>`_ to translate simple text files into inteligent and beautiful HTML files. Again, for simplicity, we are going to use `Python Documentation guidelines <http://docs.python.org/devguide/documenting.html>`_, for the style of the documentation.

Once we actually get some code and document it, we will detail the organization of it here. And provide an example docstring.

If you have any questions about how or where to add documentation, please contact `Amy <my@email.com>`_


Testing
-------
If you add a feature, it must include a test. Hmmm, have we decided on a testing module?


Code Review
-----------
The last step before having your contribution pulled into the project is a code review. Before having another person look at your code, we ask that contributors perform a self-review. We have provided a `checklist <http://code.google.com/p/rad2py/wiki/CodeReview>`_ that you should go through, prior to making a pull-request. Once you are satisfied with your code, issue a :doc:`pull request <pullrequest>`, and someone will be assigned to review your code. The person assigned to reivew your code will provide you with feedback for suggested improvements. Once you have made this improvements, issue another pull requested, which will cause your code to be reviewed again, and this process will continue until your patch is accepted, and integrated into the project.