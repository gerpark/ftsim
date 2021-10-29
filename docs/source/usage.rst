
How to use the program
======================

The program can be used with different configurations,
which are stored in the database.
To choose a certain configuration, You have to pass
the `project id` as parameter to the program.
So the program is usually startet from the command line.
More information about options can be shown using
the help option::

    ftsim --help

If nothing is specified the database name will be ``ft.db``,
and the project-id will be the highest number in the database.
More info about Locations and the transport of the `LE's` is
given with verbose 4.

So starting the program might look like this::

    ftsim.py --id 160 -v 4


If the option ``auto`` is given, the program will end as soon
as all `tasks` are finished. 

Transports
===========

All moves of the Transport units (=LE) depend on the target, which is stored in the `LE`.
The target contains the name of an area, if it is empty the LE will stay in the current area.

The target for a LE might be set in the configuration, or it might be
set later on at a Workstation. When the LE reaches a Storage Area or a Workstation,
the target is cleared again.


Manual transports
-----------------

Most areas have a name of just one letter.
If this letter is typed all LE's in that area are moved one step forward
to the next Location. Sometimes the letter needs to be typed twice,
because each LE moves only one step per cycle.

The name of a picking area starts with the letter 'k'
followed by a digit. Here the digit is typed instead of the
letter. Some Picking areas consist of one Location, but they might
have more Locations as well.


Automatic transports
--------------------

Automatic transports can be started or stopped with a 
button in the main dialog.
Every area is checked and all LE's are moved one step
forward. This cycle needs to be stopped explicitly,
otherwise it is is repeated forever.

If a LE arrives at a `workstation` a special Dialog pops up
representing that worksation. To forward the LE, a new target must 
be chosen before the transport button is clicked.


Automatic transports with orders
--------------------------------

Starting in automatic mode means as well checking for free taskorders.
If there is one, the taskorder is assigned to a workstation, if there is any available.
Each task belonging to that taskorder contains just the name of a Transport Unit.
If that LE is located in a storage area, the task will be started,
which means, the LE receives the target from the corresponding taskorder.

When the LE arrives at the Workstation a new target
can be chosen. If the programm was started from the commandline
with automode, or if 'auto Picking' was chosen from the menu,
target and transport are handled automatically.

When all tasks are picked the taskorder is closed and
the Workstation is ready for another taskorder.