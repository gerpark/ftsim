.. Sollte mit index.rst in docs abgestimmt sein !

FTSIM - Warehouse Transport Simulation
======================================

This project simulates and visualizes the transport of loadunits 
in a simple warehouse environment. These loadunits are called
Transport Units, as there inventory is only imagined.
Transport Units can be moved manually or automatically
on conveyor belts. It is possible to configure Orders, so the
Transport Units can move automatically between storage areas and picking stations.

From a technical view the configuration of the warehouse site is
stored in a sqlite3 database. The software itself is written in python3, the GUI
uses tkinter and each conveyor belt, the storage area and the picking stations
are running in seperate threads.

Originally the idea for this project was about questions 
concerning the time behavior of orders in a complex warehouse system.
So the question was, how long will it take to pick a certain batch of orders
and is this time predictable.

But the software can be used as well for playing with and building 
of nice and simple warehouse sites.
