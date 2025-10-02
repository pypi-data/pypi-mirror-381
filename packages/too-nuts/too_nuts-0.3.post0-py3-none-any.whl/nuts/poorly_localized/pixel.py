"""Define pixel class for GW module.

File defines pixel class which stores relevant
information from the skymap for poorly localized module

original author: Luke Kupari (luke-kupari@uiowa.edu)

.. autoclass:: source_pixel
    :noindex:
    :members:
    :undoc-members:
"""

from dataclasses import dataclass


@dataclass
class source_pixel:
    """Class to store relevant information for GW skymap pixels."""

    probability: float = 0
    ra: float = 0
    dec: float = 0
    pixel: int = 0

    def save_dict(self) -> dict:
        parameters = {}

        parameters["probability"] = self.probability
        parameters["ra"] = self.ra
        parameters["dec"] = self.dec
        parameters["pixel"] = self.pixel

        return parameters
