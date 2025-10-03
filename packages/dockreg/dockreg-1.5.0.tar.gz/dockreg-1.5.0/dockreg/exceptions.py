"""Dockreg exceptions."""

from __future__ import annotations


class DockregError(Exception):
    """Base class for dockreg errors."""

    pass


class DockregInternalError(DockregError):
    """Internal error."""

    def __str__(self):
        """Get string representation."""

        return f'Internal error: {", ".join(str(s) for s in self.args)}'


class DockregNotFoundError(DockregError):
    """Missing resource of some kind."""

    def __str__(self):
        """Get string representation."""

        return f'{self.args[0]} not found'
