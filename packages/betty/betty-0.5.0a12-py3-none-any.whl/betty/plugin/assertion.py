"""
Provide plugin assertions.
"""

from typing import Any, TypeVar

from betty.assertion import AssertionChain, assert_str
from betty.exception import UserFacingException
from betty.locale.localizable import Join, _, do_you_mean
from betty.plugin import Plugin, PluginIdToTypeMapping, PluginNotFound

_PluginT = TypeVar("_PluginT", bound=Plugin)


def assert_plugin(
    plugin_id_to_type_mapping: PluginIdToTypeMapping[_PluginT],
) -> AssertionChain[Any, type[_PluginT]]:
    """
    Assert that a value is a plugin ID.
    """

    def _assert(
        value: Any,
    ) -> type[_PluginT]:
        plugin_id = assert_str()(value)
        try:
            return plugin_id_to_type_mapping[plugin_id]
        except PluginNotFound:
            raise UserFacingException(
                Join(
                    " ",
                    _(
                        'Cannot find and import "{plugin_id}".',
                    ).format(plugin_id=plugin_id),
                    do_you_mean(
                        *(f'"{plugin_id}"' for plugin_id in plugin_id_to_type_mapping)
                    ),
                )
            ) from None

    return AssertionChain(_assert)
