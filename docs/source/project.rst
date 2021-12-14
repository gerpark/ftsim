
.. _project:

Database projects
=================

Warehouse layouts/configurations are called projects
and are stored in a SQLite Database.
`FTSim` comes with a few configurations, but 
for new projects the database has to be accessed.

A very convenient grafical tool to do this is the `DB-Browser für SQLite <https://sqlitebrowser.org/dl/>`_, 
which can be used with and without SQL knowlege.

Beside the DB-Browser I use the command-line-tool `sqlite3 <https://www.sqlite.org/download.html>`_
which is part of the SQLite Software.
It is nice for scripting and administrative tasks. 
An example for a script which re/builds a complete project is given in ``ftsim105.sql``.

The SQLite Database itself is just a single file.
If `FTSim` is installed with pip in the usual way, the database and the scripts are hidden or difficult to find.
But if you want to change or check something, it is easier to choose the directory for installation yourself.
This can be done with downloading a `tarball <https://en.wikipedia.org/wiki/Tar_(computing)>`_.

Looking into the details of `ftsim on PYPI <https://pypi.org/project/ftsim/>`_
You will find a Button "Download Files" and select the file ending  with `tar.gz`.

Open a terminal and change to the directory of the tarball::

    C:\SOME\DIRECTORY> pip install -t myftsim ftsim-0.9.2.tar.gz

Somewhere below the created directory `myftsim` exists a directory with the name `ftsim`,
which contains everything needed, that is the SQLight database ``ft.db``, some python- and
sqlscripts. Change to that directory and launch the main module `ftmain9`::

    C:\SOME\OTHER\DIRECTORY\FTSIM> python ftmain9.py

Examples
--------

Version 0.9.2 comes with 5 projects/configurations.
They start with the very, very basic example ``101``, just to show, what needs to be configured.
``102`` shows a loop and ``103`` introduces a simple picking place (=Workstation). 
``104`` has an additional loop and ``105`` has a small storage area.
Right now there are no examples with orders, - they follow soon.
