
Components and Names
====================

The software was written in german, so I'm going
to explain the abbreviations first, because
they are used in the code and database names.

.. _basic_le:

Transport Units
---------------
It's all about  :ref:`Transport Units<cfg_le>`,
called **LE**'s (Ladeeinheiten/Loadunits)

We don't use any inventories, but for picking
You can imagine, there is some inventory on each LE.

.. _basic_ft:

Areas
-----
The whole site consists of different :ref:`Areas<cfg_ft>`, called **Ft**'s ('FörderTechnik').

The central type of an Area is the conveyor belt (Fördertechnik),
but there are also storage areas and picking areas.

Each Area tries to move its transport Units.
As they do it independently, each `Ft` (Area) runs in it's own thread.

.. _basic_lf:

Locations
---------

Each Area consists of a sequence of :ref:`Locations<cfg_lf>`,
called **Lf**'s (Lagerfächer).
Each Location can have a Transport Unit (LE) and so each `LE` is moving
from one `location` to the next one.

Workstation
-----------

The picking area is very similar to a conveyor belt, but it has
one Location of type Workstation (**Ws**). This is the location
where the picking happens. On our visualization a little dialog pops up
as soon as a LE arrives.  In a real warehouse the Workstation might be a PC. 
To move the LE further on (after imaginary inventory has been picked)
the dialog has to be used.
Furthermore the Workstation dialog allows to create new LE's.

Orders
------

Additionally it is possible to supply orders. Each order (Task Order) is dynamically assigned
to one Workstation and consists of one or more tasks. A Task simply consists a LE name.
