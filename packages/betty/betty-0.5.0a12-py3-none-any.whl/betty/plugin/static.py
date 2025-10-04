"""
Provide static plugin management.
"""

from collections.abc import AsyncIterator
from typing import Generic, TypeVar, final

from typing_extensions import override

from betty.machine_name import MachineName
from betty.plugin import Plugin, PluginNotFound, PluginRepository

_PluginT = TypeVar("_PluginT", bound=Plugin)


@final
class StaticPluginRepository(PluginRepository[_PluginT], Generic[_PluginT]):
    """
    A repository that is given a static collection of plugins, and exposes those.
    """

    def __init__(self, plugin: type[_PluginT], *plugins: type[_PluginT]):
        super().__init__(plugin)
        self._plugins = {plugin.plugin_id(): plugin for plugin in plugins}

    @override
    async def get(self, plugin_id: MachineName) -> type[_PluginT]:
        try:
            return self._plugins[plugin_id]
        except KeyError:
            raise PluginNotFound.new(
                plugin_id, [plugin async for plugin in self]
            ) from None

    @override
    async def __aiter__(self) -> AsyncIterator[type[_PluginT]]:
        for plugin in self._plugins.values():
            yield plugin
