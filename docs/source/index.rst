
Introduction to FTSim
=====================

This document refers to version 0.9.2 of `FTSim` /  18.12.2021


`FTSim` is now on `PYPI <https://pypi.org/project/ftsim/>`_ but there is still a lot to do.
The program runs stable under MS-Windows and linux, and probably also under MacOS.

What is it all about:

This program simulates and visualizes the transport of loadunits 
in a simple warehouse environment. These loadunits are called
Transport Units, as the inventory is only imagined.
Transport Units can be moved manually or automatically
on conveyor belts. It is possible to configure Orders, so the
Transport Units can move automatically between storage areas and Workstations.

From a technical view the configuration of the warehouse site is
stored in a sqlite3 database. The software itself is written in python3, the GUI
uses tkinter and each conveyor belt, the storage area and the Workstations
are running in seperate threads.

Originally the idea for this project was dealing with the time behavior
of orders in a complex warehouse system. So the question was, how long will it take
to pick a certain batch of orders and is the required time predictable.

But the software can be used as well for playing with and building 
of nice and simple warehouse sites (sql exercise).

Have a try and if there any questions, suggestions, corrections, don't hesitate to contact me at g.w.sachs@gmx.de.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   basic.rst
   component.rst
   usage.rst
   config.rst
   project.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
