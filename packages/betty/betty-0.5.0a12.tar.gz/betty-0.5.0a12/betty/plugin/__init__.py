"""
The Plugin API.

Plugins allow third-party code (e.g. your own Python package) to add functionality
to Betty.

Read more at :doc:`/development/plugin`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import (
    TYPE_CHECKING,
    Generic,
    Self,
    TypeAlias,
    TypeVar,
    final,
)

from typing_extensions import override

from betty.exception import UserFacingException
from betty.json.schema import Enum
from betty.locale.localizable import Join, _, do_you_mean
from betty.locale.localizer import DEFAULT_LOCALIZER
from betty.machine_name import MachineName
from betty.string import kebab_case_to_lower_camel_case

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Iterable, Iterator, Mapping, Sequence
    from graphlib import TopologicalSorter

    from betty.locale.localizable import Localizable

_T = TypeVar("_T")


class PluginError(Exception):
    """
    Any error originating from the Plugin API.
    """


class Plugin(ABC):
    """
    A plugin.

    Plugins are identified by their :py:meth:`IDs <betty.plugin.Plugin.plugin_id>` as well as their types.
    Each must be able to uniquely identify the plugin within a plugin repository.

    To test your own subclasses, use :py:class:`betty.test_utils.plugin.PluginTestBase`.
    """

    @classmethod
    @abstractmethod
    def plugin_type_cls(cls) -> type[Plugin]:
        """
        The base type (class) of all plugins of this type.
        """

    @classmethod
    @abstractmethod
    def plugin_type_id(cls) -> MachineName:
        """
        The plugin type ID.
        """

    @classmethod
    @abstractmethod
    def plugin_type_label(cls) -> Localizable:
        """
        Get the human-readable short plugin type label for the given count.
        """

    @classmethod
    @abstractmethod
    def plugin_id(cls) -> MachineName:
        """
        Get the plugin ID.

        IDs are unique per plugin type:

        - A plugin repository **MUST** at most have a single plugin for any ID.
        - Different plugin repositories **MAY** each have a plugin with the same ID.
        """

    @classmethod
    @abstractmethod
    def plugin_label(cls) -> Localizable:
        """
        Get the human-readable short plugin label.
        """

    @classmethod
    def plugin_description(cls) -> Localizable | None:
        """
        Get the human-readable long plugin description.
        """
        return None


_PluginT = TypeVar("_PluginT", bound=Plugin)
_PluginCoT = TypeVar("_PluginCoT", bound=Plugin, covariant=True)


class OrderedPlugin(Generic[_PluginT], Plugin):
    """
    A plugin that can declare its order with respect to other plugins.
    """

    @classmethod
    def comes_before(cls) -> set[PluginIdentifier[_PluginT & OrderedPlugin[_PluginT]]]:
        """
        Get the plugins that this plugin comes before.

        The returned plugins come after this plugin.
        """
        return set()

    @classmethod
    def comes_after(cls) -> set[PluginIdentifier[_PluginT & OrderedPlugin[_PluginT]]]:
        """
        Get the plugins that this plugin comes after.

        The returned plugins come before this plugin.
        """
        return set()


class DependentPlugin(Generic[_PluginT], OrderedPlugin[_PluginT]):
    """
    A plugin that can declare its dependency on other plugins.
    """

    @classmethod
    def depends_on(cls) -> set[PluginIdentifier[_PluginT & DependentPlugin[_PluginT]]]:
        """
        The plugins this one depends on.

        To declare whether this plugin comes before or after its dependencies, implement
        :py:meth:`betty.plugin.OrderedPlugin.comes_before` and/or :py:meth:`betty.plugin.OrderedPlugin.comes_after`.
        """
        return set()


class ShorthandPluginBase(Plugin):
    """
    Allow shorthand declaration of plugins.
    """

    _plugin_id: MachineName
    _plugin_label: Localizable
    _plugin_description: Localizable | None = None

    @override
    @classmethod
    def plugin_id(cls) -> MachineName:
        return cls._plugin_id

    @override
    @classmethod
    def plugin_label(cls) -> Localizable:
        return cls._plugin_label

    @override
    @classmethod
    def plugin_description(cls) -> Localizable | None:
        return cls._plugin_description


PluginIdentifier: TypeAlias = type[_PluginT] | MachineName


def resolve_identifier(plugin_identifier: PluginIdentifier[Plugin]) -> MachineName:
    """
    Resolve a plugin identifier to a plugin ID.
    """
    if isinstance(plugin_identifier, str):
        return plugin_identifier
    return plugin_identifier.plugin_id()


class PluginNotFound(PluginError, UserFacingException):
    """
    Raised when a plugin cannot be found.
    """

    @classmethod
    def new(
        cls, plugin_id: MachineName, available_plugins: Sequence[type[Plugin]]
    ) -> Self:
        """
        Create a new instance.
        """
        return cls(
            Join(
                " ",
                _('Could not find a plugin "{plugin_id}".').format(plugin_id=plugin_id),
                do_you_mean(
                    *[f'"{plugin.plugin_id()}"' for plugin in available_plugins]
                ),
            )
        )


_PluginMixinOneT = TypeVar("_PluginMixinOneT")
_PluginMixinTwoT = TypeVar("_PluginMixinTwoT")
_PluginMixinThreeT = TypeVar("_PluginMixinThreeT")


class PluginIdToTypeMapping(Generic[_PluginCoT]):
    """
    Map plugin IDs to their types.
    """

    def __init__(self, id_to_type_mapping: Mapping[MachineName, type[_PluginCoT]]):
        self._id_to_type_mapping = id_to_type_mapping

    @classmethod
    async def new(cls, plugins: PluginRepository[_PluginCoT]) -> Self:
        """
        Create a new instance.
        """
        return cls({plugin.plugin_id(): plugin async for plugin in plugins})

    def get(
        self, plugin_identifier: MachineName | type[_PluginCoT]
    ) -> type[_PluginCoT]:
        """
        Get the type for the given plugin identifier.
        """
        if isinstance(plugin_identifier, type):
            return plugin_identifier
        try:
            return self._id_to_type_mapping[plugin_identifier]
        except KeyError:
            raise PluginNotFound.new(
                plugin_identifier, list(self._id_to_type_mapping.values())
            ) from None

    def __getitem__(
        self, plugin_identifier: MachineName | type[_PluginCoT]
    ) -> type[_PluginCoT]:
        return self.get(plugin_identifier)

    def __iter__(self) -> Iterator[MachineName]:
        yield from self._id_to_type_mapping


class PluginRepository(Generic[_PluginT], ABC):
    """
    Discover and manage plugins.
    """

    def __init__(self, plugin: type[_PluginT]):
        self._plugin = plugin
        self._plugin_id_schema: Enum | None = None

    @final
    @property
    def plugin(self) -> type[_PluginT]:
        """
        The plugin this repository manages.
        """
        return self._plugin

    async def resolve_identifier(
        self, plugin_identifier: PluginIdentifier[_PluginT]
    ) -> type[_PluginT]:
        """
        Resolve a plugin identifier to a plugin type.
        """
        if isinstance(plugin_identifier, type):
            return plugin_identifier
        return await self.get(plugin_identifier)

    async def resolve_identifiers(
        self, plugin_identifiers: Iterable[PluginIdentifier[_PluginT]]
    ) -> Sequence[type[_PluginT]]:
        """
        Resolve plugin identifiers to plugin types.
        """
        return [
            await self.resolve_identifier(plugin_identifier)
            for plugin_identifier in plugin_identifiers
        ]

    async def mapping(self) -> PluginIdToTypeMapping[_PluginT]:
        """
        Get the plugin ID to type mapping.
        """
        return await PluginIdToTypeMapping.new(self)

    @abstractmethod
    async def get(self, plugin_id: MachineName) -> type[_PluginT]:
        """
        Get a single plugin by its ID.

        :raises PluginNotFound: if no plugin can be found for the given ID.
        """

    @abstractmethod
    def __aiter__(self) -> AsyncIterator[type[_PluginT]]:
        pass

    @property
    async def plugin_id_schema(self) -> Enum:
        """
        Get the JSON schema for the IDs of the plugins in this repository.
        """
        if self._plugin_id_schema is None:
            label = self.plugin.plugin_type_label().localize(DEFAULT_LOCALIZER)
            self._plugin_id_schema = Enum(
                *[plugin.plugin_id() async for plugin in self],  # noqa A002
                def_name=kebab_case_to_lower_camel_case(self.plugin.plugin_type_id()),
                title=label,
                description=f"A {label} plugin ID",
            )
        return self._plugin_id_schema


class CyclicDependencyError(PluginError):
    """
    Raised when plugins define a cyclic dependency, e.g. two plugins depend on each other.
    """

    def __init__(self, plugin_types: Iterable[type[Plugin]]):
        plugin_names = ", ".join([plugin.plugin_id() for plugin in plugin_types])
        super().__init__(
            f"The following plugins have cyclic dependencies: {plugin_names}"
        )


async def sort_ordered_plugin_graph(
    plugin_repository: PluginRepository[_PluginCoT & OrderedPlugin[_PluginCoT]],
    plugins: Iterable[type[_PluginCoT & OrderedPlugin[_PluginCoT]]],
    sorter: TopologicalSorter[type[_PluginCoT & OrderedPlugin[_PluginCoT]]],
) -> None:
    """
    Build a graph of the given plugins.
    """
    plugins = sorted(plugins, key=lambda plugin: plugin.plugin_id())
    for plugin in plugins:
        sorter.add(plugin)
        for before_identifier in plugin.comes_before():
            before = (
                await plugin_repository.get(before_identifier)
                if isinstance(before_identifier, str)
                else before_identifier
            )
            if before in plugins:
                sorter.add(before, plugin)
        for after_identifier in plugin.comes_after():
            after = (
                await plugin_repository.get(after_identifier)
                if isinstance(after_identifier, str)
                else after_identifier
            )
            if after in plugins:
                sorter.add(plugin, after)


async def expand_plugin_dependencies(
    plugin_repository: PluginRepository[_PluginCoT & DependentPlugin[_PluginCoT]],
    plugins: Iterable[type[_PluginCoT & DependentPlugin[_PluginCoT]]],
) -> set[type[_PluginCoT & DependentPlugin[_PluginCoT]]]:
    """
    Expand a collection of plugins to include their dependencies.
    """
    dependencies = set()
    for plugin in plugins:
        dependencies.add(plugin)
        dependencies.update(
            await expand_plugin_dependencies(
                plugin_repository,
                # We have not quite figured out how to type this correctly, so ignore any errors for now.
                await plugin_repository.resolve_identifiers(plugin.depends_on()),
            )
        )
    return dependencies


async def sort_dependent_plugin_graph(
    plugin_repository: PluginRepository[_PluginCoT & DependentPlugin[_PluginCoT]],
    plugins: Iterable[type[_PluginCoT & DependentPlugin[_PluginCoT]]],
    sorter: TopologicalSorter[type[_PluginCoT & DependentPlugin[_PluginCoT]]],
) -> None:
    """
    Sort a dependent plugin graph.
    """
    await sort_ordered_plugin_graph(
        plugin_repository,  # type: ignore[arg-type]
        await expand_plugin_dependencies(plugin_repository, plugins),
        sorter,  # type: ignore[arg-type]
    )
