
Configuration
=============

The layouts of different warehouse sites are configured in a SQLite3 Database.

The configurations are called projects, which have 
a Project-Id as primary key.

The so called Project-Id is specific to each configuration,
it is the primary key for all tables in the database.

FTSim comes with a number of different configurations,
but please feel free to create your own ones.

I usually do it step by step using the command line tool ``sqlite3``.
In between I run ``ftsim`` just to check if the layout 
looks as intended.

The basic configuration **is read only once** in the beginning
when the program is started.
Only the **order-tables**, if in use, are changed during runtime.

Basic - Tables
--------------

Most tables have foreign keys, which can be looked up in the
database. The foreign keys will help to keep the configuration consistent.

The **central** Configuration Table::

    CREATE TABLE project(
	prjid INT,
	fieldx INT,
	fieldy INT,
	fieldpx INT)

prjid stands for the project-id, und fieldx/y is the overall size of the layout.

.. _cfg_ft:

The **areas**::

    CREATE TABLE ft(
	prjid INT,
	ftname VARCHAR(2),
	fttyp VARCHAR(2),
	PRIMARY KEY (prjid, ftname))
    
``ftname`` is the name of the area,
``fttyp`` may have these values:

 *     FT =  automatic conveyor belt
 *     LB =  storage area
 *     KP =  picking area
 *     DB =  Database
             if **orders** are used, a area of type DB needs to be configured 
             (because of the seperate database thread).

.. _cfg_lf:

Each Area consists of a number of **Locations**::

    CREATE TABLE lf(
	prjid INT,
	lfname VARCHAR(6),
	ftname VARCHAR(2),
	lftyp VARCHAR(2),
	xkor INT,
	ykor INT,
	leid VARCHAR(3),
	PRIMARY KEY (prjid, lfname))


``ftname`` is the Area the Location belongs to.
``xkor/ykor`` define the coordinates in the layout and
``lftyp`` is either NULL or KP for a picking place.

If a Location is occupied with a Transport Unit (LE), the 
Databasefield ``leid`` needs to be set.
Locations of a certain Area form a sequence, which ist determined
by the order of the location names.


.. _cfg_le:

The **Transport Unit** also called **LE**::

    CREATE TABLE le(
	prjid INT,
	leid VARCHAR(3),
	lfname VARCHAR(6),
	ftziel VARCHAR(2),
	PRIMARY KEY (prjid, leid))

``ftziel`` is the target area of the LE.
``lfname`` is only for documentation, the Location
of the LE must be set in table ``lf``.


If a Location is connected to a Location of a different Area,
or the last Location is connected to the first
Location of the same area an **alternate Location**
has to be configured::

    CREATE TABLE lfalt(
	prjid INT,
	lfname VARCHAR(6),
	altlf VARCHAR(6),
	PRIMARY KEY (prjid, lfname))


``lfname`` is the source Location and
``altlf`` is the name of the alternate Location.


If a Location is the entrance to a certain area,
a list of **target areas** can be configured.
The first area will be the Area of that Location , further areas
will be used for routing::

    CREATE TABLE lfziel(
	prjid INT NOT NULL,
	lfname VARCHAR(6) NOT NULL,
	ftname VARCHAR(2) NOT NULL)

``lfname`` specifies the Location, ``ftname`` contains the target area.


.. _cfg_order:

Order - Tables
--------------

A Task contains the `LE` with the imaginary inventory,
that needs to be picked at the Picking Place / the `Workstation`.

A Taskorder consists of one or more Tasks, which have to be picked at the same Workstation.
Taskorder and Tasks are updated during runtime.

If there is a open Taskorder it will be assigned to a free workstation.
After all Transport Unit's have been processed (virtually picked)
the **Taskorder** is closed and the workstation can by used by the next Taskorder::

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
it is a randomized sorting key.
``Startt`` and ``endt`` contain time information.
``Taskostat`` is the state of the Taskorder and can have these values:

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

The table ``le`` is not changed during runtime,
all information about the LE  is stored in the table Task.

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
