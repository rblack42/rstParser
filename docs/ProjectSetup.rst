Setting up rstParser
####################

..  include::   /references.inc

As part of my PyLit6_ project, I am creating a new parser for reStructuredText_.
My goal is to decouple the parser from its current tight binding to Python and
make it easier to extend to other languages. Additionally, I want to create a
document management structure for folks (like me) who create a lot of documents
and modify them frequently. 

This project is going to be hosted on PyPi, and will use a number of modern
tools to verify that it is designed properly. In this note, the basic project
structure will be created.

Setting Up on GitHub
********************

It seems that all good projects end up living on GitHub_ these days, and this
one will be no exception. To begin the project, I created a new empty repository
using the GitHub_ web interface. The assigned project URL is:

    * https://github.com/rblack42/rstParser.git

Next, we set up a working project directory. On my development system this is
in ``~/_projects/rstParser``. After this is set up, we connect the local
repository to the GitHub_ project:

..  code-block:: text

    mkdir ~/_projects/rstParser
    cd ~/_projects/rstParser
    git init
    touch README.rst
    git add .
    git commit . -m "initial commit"
    git remote add origin https://github.com/rblack42/rstParser.git
    git push -U origin master

Setting up the project directory structure
******************************************

Next, we create a few standard directories:

..  code-block:: text

    mkdir docs
    mkdir tests
    mkdir rstparser
    touch rstparser/__init__.py

Setting up TravisCI
*******************

Once the project is up on Github, open up a web browser and navigate to your TravisCI_ accont page. On your main page, click on the small plus icon. Your repositories will be displayed. Click on :menuselection:`Sync now` to update this list. Once this has been done, scroll down until you see your new project, and turn on the control that will fire off tests.

From this point on, any time you push new changes to your site, the trsts will run and the status of your project will appran in your GitHub_ README file.



