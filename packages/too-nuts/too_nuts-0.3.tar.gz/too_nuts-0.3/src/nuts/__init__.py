r"""Target of Opportunity Source Scheduler

***************
ToO
***************

.. autosummary::
   :toctree:
   :nosignatures:

   nuts.too_observation
   nuts.too_event
   nuts.prioritization

*************
I/O functions
*************

.. autosummary::
   :toctree:
   :nosignatures:

   nuts.IO_funcs

*************
Configuration
*************

.. autosummary::
   :toctree:
   :nosignatures:

   nuts.config

***********
Visualizing
***********

.. autosummary::
   :toctree:
   :nosignatures:

   nuts.visualization

**********
Listeners
**********
.. autosummary::
   :toctree:
   :nosignatures:

   nuts.alert_listeners

**********
Utilities
**********

.. autosummary::
   :toctree:
   :nosignatures:

   nuts.detector_motion
   nuts.observation_period
   nuts.alert_listeners
   nuts.scheduling
   nuts.apps

"""

__all__ = [
    "apps",
    "Catalogs",
    "detector_motion",
    "config",
    "IO_funcs",
    "observation_period",
    "alert_listeners",
    "prioritization",
    "scheduling",
    "visualization",
    "poorly_localized",
]


# Do not import the `UI` package at module import time because it imports
# Streamlit and related UI libraries. Import UI lazily (e.g. `import nuts.UI`)
# when the GUI is actually needed to avoid printing Streamlit warnings during
# CLI-only operations (like `nuts --help`).
from . import (
    Catalogs,
    IO_funcs,
    alert_listeners,
    apps,
    config,
    detector_motion,
    observation_period,
    poorly_localized,
    prioritization,
    scheduling,
    visualization,
)
