
Configuration
=============

The layouts of different warehouse sites are configured in a SQLite3 Database.

The configurations are called projects, which have 
a Project-Id as primary key.

The so called Project-Id is specific to each configuration,
it is the primary key for all tables in the database.

This software comes with a number of different configurations,
but please feel free to create your own ones.

I usually do it step by step using the command line tool ``sqlite3``.
In between I run ``ftsim`` just to check if the layout 
looks as intended.

The basic configuration is read only once in the beginning.
Only the order-tables, if used, are changed during runtime.

Basic - Tables
--------------

The **central** Configuration Table::

    CREATE TABLE project(
	prjid INT,
	fieldx INT,
	fieldy INT,
	fieldpx INT)

prjid ist die zentrale Project-Id, und fieldx/y the overall size of the layout.

.. _cfg_ft:

The **areas**::

    CREATE TABLE ft(
	prjid INT,
	ftname VARCHAR(2),
	fttyp VARCHAR(2),
	PRIMARY KEY (prjid, ftname))
    
``ftname`` is the name of the area,
``fttyp`` may have these values:

 *     FT =  conveyor 
 *     LB =  storage area
 *     KP =  picking area
 *     DB =  Database
             if **orders** are used, a area of type DB needs to be configured 
             (because of the seperate database thread).

.. _cfg_lf:

Each area consists of a number of **Locations**::

    CREATE TABLE lf(
	prjid INT,
	lfname VARCHAR(6),
	ftname VARCHAR(2),
	lftyp VARCHAR(2),
	xkor INT,
	ykor INT,
	leid VARCHAR(3),
	PRIMARY KEY (prjid, lfname))


``xkor/ykor`` define the coordinates in the layout,
``lftyp`` is either NULL or KP for the picking place.

If the Location is occupied with a Transport Unit (LE), ``leid`` 
gets the name of it.
The seqence of the Locations is given by the order of the
Location names.

.. _cfg_le:

The **Transport Unit** also called **LE**::

    CREATE TABLE le(
	prjid INT,
	leid VARCHAR(3),
	lfname VARCHAR(6),
	ftziel VARCHAR(2),
	PRIMARY KEY (prjid, leid))

``lfname`` is the name of the Location 
which holds the Transport Unit in the beginning.
``ftziel`` is the target area of the LE.


If a Location is connected to a Location of a different area,
or the last Location is connected to the first
Location of the same area an **alternate Location**
has to be configured::

    CREATE TABLE lfalt(
	prjid INT,
	lfname VARCHAR(6),
	altlf VARCHAR(6),
	PRIMARY KEY (prjid, lfname))

``altlf`` is the name of the alternate Location.

If a Location is an entrance to a certain area,
many **target areas** can be configured::

    CREATE TABLE lfziel(
	prjid INT NOT NULL,
	lfname VARCHAR(6) NOT NULL,
	ftname VARCHAR(2) NOT NULL)

``ftname`` contains the area and is used
as routing information, how to get there.

Order - Tables
--------------


A Task contains the LE, which holds the imaginary inventory,
which has to be picked.

The Taskorder consists of one or more Tasks. In this way all
Tasks can be picked at the same Workstation.
Taskorder and Tasks are updated during runtime.

If there is a open Taskorder it will be assigned to a free workstation.
After all Transport Unit's have been processed (virtually picked)
the **Taskorder** is closed and the workstation freed again::

    CREATE TABLE tasko(
	prjid INT NOT NULL,
	taskoid VARCHAR(3) NOT NULL,
	wsid VARCHAR(6),
	taskostat INT NOT NULL,
	startt VARCHAR(23),
	endt VARCHAR(23),
	seq INT,
	PRIMARY KEY (prjid, taskoid))

If a Taskorder is assignet to a Workstation ``wsid`` contains the name
of that Workstation. ``Seq`` is used internally,
it contains the order of the taskorder and is randomized.
``Startt`` and ``endt`` contain the time information.
``Taskostat`` ist the state of the Taskorder and can have these values:

 *      0  = ready to be used
 *      20 = started, assigned to a workstation
 *      95 = closed, all LEs picked

The **task** contains just the Transport Unit
and the ``taskoid`` it belongs to::

    CREATE TABLE task(
	prjid INT,
	leid VARCHAR(3) NOT NULL,
	taskstat INT NOT NULL,
	ftziel VARCHAR(2),
	taskoid VARCHAR(3) NOT NULL,

``Taskstat`` is the state of the Task and can have these values:

      * 0   ready to be used
      * 20  Tasko started
      * 60  LE at workstation
      * 95  LE picked and left the workstation

The table ``le`` is not updated, everything
about the state of a Transport Unit is stored in the table Task.

The remaining tables are about statistics,
the times for each Taskorder are written into 
table ``zeiten``::

    CREATE TABLE zeiten(
	prjid INT NOT NULL,
	taskoid VARCHAR(3),
	startt VARCHAR(23),
	endt VARCHAR(23),
	seq INT)

and the times for the complete batch is summarized
in the table ``summen``::

    CREATE TABLE summen(
	prjid INT NOT NULL,
	startt VARCHAR(23),
	endt VARCHAR(23))
