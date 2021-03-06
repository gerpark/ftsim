
Components and Names
====================

The software was written in German, so I'm going
to explain the abbreviations first, because
they are used in the code and database names.

.. _basic_le:

Transport Units
---------------
It's all about  :ref:`Transport Units<cfg_le>`,
called **LE**'s (Ladeeinheiten/Loadunits).
We don't use any inventories, but for picking
you have to imagine there is some inventory on each `LE`.
`Transport Units` move in and between `Areas` depending on their target.

.. _basic_ft:

Areas
-----
The whole site consists of different :ref:`Areas<cfg_ft>`, called **Ft**'s ('FörderTechnik').

The central type of an Area is the conveyor belt (Fördertechnik),
but there are also storage areas and picking areas.

Each Area tries to move its `Transport Units`.
As they do it independently, each `Ft` (Area) runs in it's own thread.

.. _basic_lf:

Locations
---------

Each `Area` consists of a sequence of :ref:`Locations<cfg_lf>`,
called **Lf**'s (Lagerfächer).
Each Location can hold one Transport Unit (LE) and so each `LE` is moving
from one Location to the next one.

Workstation
-----------

The picking area is very similar to a conveyor belt, but it has
one Location of type Workstation (**Ws**). This is the location
where the picking happens. On our visualization a little dialog pops up
or receives the focus as soon as a `LE` arrives.  In a real warehouse the Workstation might be a PC. 
To move the LE further on (after imaginary inventory has been picked)
a dialog has to be used.
Furthermore the Workstation dialog allows to create new `LE's`.

Orders
------

Additionally it is possible to supply :ref:`Orders<cfg_order>`. Each **Order** (Task Order) is dynamically assigned
to one Workstation and consists of one or more **Tasks**. A `Task` basically consists of a `LE`,
which has to be 'picked' at a `Workstation`.
Before a Task can route a `LE` to a Workstation, that LE has to be in a storage area.
The Taskorder itself starts if there is a free workstation and all `LE's` are available.
