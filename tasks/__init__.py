"""Invoke tasks."""

from invoke import Collection

from . import format, test

ns = Collection()
ns.add_collection(format)
ns.add_collection(test)