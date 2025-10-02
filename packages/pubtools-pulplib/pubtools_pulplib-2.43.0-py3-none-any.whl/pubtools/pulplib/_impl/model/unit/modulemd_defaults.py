from .base import Unit, unit_type

from ..attr import pulp_attrib
from ... import compat_attr as attr
from frozendict.core import frozendict  # pylint: disable=no-name-in-module
from ..convert import frozenlist_or_none_sorted_converter, frozendict_or_none_converter
from ..validate import optional_frozendict


@unit_type("modulemd_defaults")
@attr.s(kw_only=True, frozen=True)
class ModulemdDefaultsUnit(Unit):
    """A :class:`~pubtools.pulplib.Unit` representing a modulemd_defaults document.

    .. versionadded:: 2.4.0
    """

    name = pulp_attrib(type=str, pulp_field="name", unit_key=True)
    """The name of this modulemd defaults unit"""

    repo_id = pulp_attrib(type=str, pulp_field="repo_id", unit_key=True)
    """The repository ID bound to this modulemd defaults unit"""

    stream = pulp_attrib(type=str, pulp_field="stream", default=None)
    """The stream of this modulemd defaults unit"""

    profiles = pulp_attrib(
        type=frozendict,
        pulp_field="profiles",
        default=None,
        validator=optional_frozendict,
        converter=frozendict_or_none_converter,
    )
    """The profiles of this modulemd defaults unit."""

    content_type_id = pulp_attrib(
        default="modulemd_defaults", type=str, pulp_field="_content_type_id"
    )

    repository_memberships = pulp_attrib(
        default=None,
        type=list,
        converter=frozenlist_or_none_sorted_converter,
        pulp_field="repository_memberships",
    )
    """IDs of repositories containing the unit, or ``None`` if this information is unavailable.

    .. versionadded:: 2.6.0
    """

    unit_id = pulp_attrib(type=str, pulp_field="_id", default=None)
    """The unique ID of this unit, if known.

    .. versionadded:: 2.20.0
    """
