.. ftsim documentation master file, created by
   sphinx-quickstart on Sat Sep  4 11:32:51 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Introduction to ftsim
=====================

This Softwareproject `ftsim` is still **at work**, the documentation is not finished but live.
The software is  still on `test.pyp.org`  and should work under linux.
It will be moved to pypi in the next weeks, so it should be ready before christmas 21.

Now what is it all about:

This project simulates and visualizes the transport of loadunits 
in a simple warehouse environment. These loadunits are called
Transport Units, as the inventory is only imagined.
Transport Units can be moved manually or automatically
on conveyor belts. It is possible to configure Orders, so the
Transport Units can move automatically between storage areas and Workstations.

From a technical view the configuration of the warehouse site is
stored in a sqlite3 database. The software itself is written in python3, the GUI
uses tkinter and each conveyor belt, the storage area and the Workstations
are running in seperate threads.

Originally the idea for this project was about questions 
concerning the time behavior of orders in a complex warehouse system.
So the question was, how long will it take to pick a certain batch of orders
and is the required time time predictable.

But the software can be used as well for playing with and building 
of nice and simple warehouse sites (sql exercise).


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   basic.rst
   component.rst
   usage.rst
   config.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
