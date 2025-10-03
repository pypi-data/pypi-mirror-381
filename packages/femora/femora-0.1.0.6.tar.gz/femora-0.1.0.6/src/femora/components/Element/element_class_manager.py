# Provides direct references to element classes for autocompletion and easy access
from .elementsOpenSees import SSPQuadElement, stdBrickElement, PML3DElement
from .elements_opensees_beam import DispBeamColumnElement, ForceBeamColumnElement, ElasticBeamColumnElement


class _BrickElements:
    std = stdBrickElement
    pml3d = PML3DElement

class _QuadElements:
    ssp = SSPQuadElement

class _BeamElements:
    disp = DispBeamColumnElement
    force = ForceBeamColumnElement
    elastic = ElasticBeamColumnElement


