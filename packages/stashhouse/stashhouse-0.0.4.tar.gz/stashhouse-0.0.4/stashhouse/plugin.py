"""
Plugin execution utilities.
"""

import argparse
import logging
import multiprocessing
from importlib.metadata import entry_points
from typing import (
    Protocol,
    runtime_checkable,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from . import server

    # noinspection PyProtectedMember
    from importlib.metadata import EntryPoint, EntryPoints


class PluginOptions(TypedDict, total=False):
    """
    Plugin options.

    This is provided for future expansion, though
    there currently does not exist any mandates
    on the plugin option definitions.
    """


@runtime_checkable
class Plugin(Protocol):
    """
    Defines method headers required for plugins.
    """

    # noinspection PyUnusedLocal
    def __init__(
        self,
        server_options: "server.ServerOptions",
        exited: multiprocessing.Event,
        **kwargs: Unpack[PluginOptions],
    ) -> None:
        """
        Initialize the plugin.

        Args:
            server_options: Globally available server options.
            exited: Whether the plugin should exit.
            **kwargs: Plugin options.
        """
        self.server_options = server_options
        self.exited = exited

    def run(self) -> None:
        """
        Start the plugin.
        """

    @classmethod
    def register_arguments(
        cls, plugin_name: str, parser: argparse.ArgumentParser
    ) -> None:
        """
        Adds arguments to a parser for a plugin.

        Args:
            plugin_name: The plugin name.
            parser: An argument parser.
        """

    @classmethod
    def derive_options(
        cls, plugin_name: str, args: argparse.Namespace
    ) -> PluginOptions:
        """
        Given a namespace, extracts the plugin's options.

        Args:
            plugin_name: The plugin name.
            args: An argument parser.

        Returns:
            A dictionary of values for the plugin.
        """


logger = logging.getLogger(__name__)


def find_plugins() -> "EntryPoints":
    """
    Identifies plugin definitions based on entry points.

    Returns:
        Entry points of plugins.
    """

    return entry_points(group="stashhouse.plugin")


def _run_server_plugin(
    plugin: "EntryPoint", *args, log_level: int = logging.INFO, **kwargs
) -> None:
    """
    Executes a plugin.

    Exists to enable execution with multiprocessing while
    preventing excessive imports into the main process.

    Args:
        plugin: Entry point pointing to a Plugin.
        *args: Arguments to pass to the Plugin initializer.
        log_level: Minimum level to log.
        **kwargs: Keyword arguments to pass to the Plugin initializer.
    """

    logging.basicConfig(level=log_level)
    plugin_instance: Plugin = plugin.load()(*args, **kwargs)

    try:
        plugin_instance.run()
    except KeyboardInterrupt:
        kwargs["exited"].set()
    except:
        logger.exception("Shutting down plugin due to exception: %s", plugin.name)
        raise


def run_server_plugin(*args, **kwargs) -> multiprocessing.Process:
    """
    Creates a multiprocessing process to execute a plugin.

    Args:
        *args: Arguments to pass to _run_server_plugin.
        **kwargs: Keyword arguments to pass to _run_server_plugin.

    Returns:
        A multiprocessing process that when started, executes the plugin.
    """

    return multiprocessing.Process(target=_run_server_plugin, args=args, kwargs=kwargs)


__all__ = ("PluginOptions", "Plugin", "find_plugins", "run_server_plugin")
