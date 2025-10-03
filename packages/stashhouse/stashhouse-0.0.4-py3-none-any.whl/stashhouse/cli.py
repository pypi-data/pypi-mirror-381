"""
Server execution through the command-line.

Accepts arguments from the command-line and start the server.
"""

import argparse
import logging
import pathlib
from typing import TYPE_CHECKING, Sequence

from . import server, plugin

if TYPE_CHECKING:
    # noinspection PyProtectedMember
    from importlib.metadata import EntryPoint, EntryPoints

LOG_LEVELS: dict[str, int] = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "all": logging.NOTSET,
}


def _log_level(log_level_name: str) -> int:  # noqa
    """
    Converts a log level name to its associated integer level

    Args:
        log_level_name: Log level name

    Returns:
        Log level integer associated with the name
    """

    return LOG_LEVELS.get(log_level_name.lower(), logging.INFO)


def _parse_requested_plugins(args: Sequence[str] | None = None) -> Sequence[str]:
    """
    Parses the requested plugins to enable.

    Serves to restrict memory usage by preventing
    the loading of unnecessary plugins entirely.

    Args:
        args: Sequence of arguments to evaluate.

    Returns:
        A sequence of plugin names to enable.
    """

    load_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        exit_on_error=False, add_help=False
    )

    # fmt: off
    load_parser.add_argument(
        "--enable-plugin", "--enable", "-e",
        nargs="*", action="extend", dest="plugins", default=[])

    return tuple(load_parser.parse_known_args(args)[0].plugins)


def _parser(
    plugin_definitions: "EntryPoints",
    desired_plugins: Sequence[str] | None = None,
    **kwargs,
) -> argparse.ArgumentParser:
    """
    Creates an argument parser.

    The argument parser will always consist of server options and
    may include additional options derived from installed plugins.

    Args:
        plugin_definitions: Plugin definitions to register arguments for.
        desired_plugins: Sequence of desired plugin names.
        **kwargs: Keyword arguments to pass for parser initialization.

    Returns:
        An argument parser instance.
    """

    parser = argparse.ArgumentParser(**kwargs)
    # fmt: off
    parser.add_argument("--host", "-H",
                        default="127.0.0.1", help="Address to listen on")
    # fmt: off
    parser.add_argument("--directory", "-d", default="data",
                        type=pathlib.Path, help="Directory to store data in",)
    # fmt: off
    parser.add_argument("--log-level",
                        choices=LOG_LEVELS.keys(), default="info",
                        help="Log level to print to console")

    # Plugin Loading
    plugin_names: list[str] = [
        entry.name
        for entry in plugin_definitions
        if not desired_plugins or entry.name in desired_plugins
    ]

    # fmt: off
    parser.add_argument("--enable-plugin", "--enable", "-e", nargs="+",
                        choices=plugin_names, action="extend", default=[], dest="plugins",
                        help="Plugin names to enable")

    plugin_entry: "EntryPoint"
    for plugin_entry in plugin_definitions:
        if desired_plugins and plugin_entry.name not in desired_plugins:
            continue

        registrar: plugin.Plugin = plugin_entry.load()
        registrar.register_arguments(plugin_entry.name, parser)

    return parser


def _parse_arguments(
    plugin_definitions: "EntryPoints",
    args: Sequence[str] | None = None,
    namespace: argparse.Namespace = None,
    **kwargs,
) -> tuple[server.ServerOptions, dict[str, plugin.PluginOptions]]:
    """
    Parse arguments while leveraging installed plugins.

    Args:
        plugin_definitions: Plugin definitions to handle arguments for.
        args: Sequence of arguments to parse.
        namespace: Namespace of options.
        **kwargs: Keyword arguments to pass for parser initialization.

    Returns:
        A tuple of server options and a dictionary of plugin options.
        The plugin options dictionary consists of string dictionary keys
        representing plugin names and dictionary (str -> Any) values.
    """

    desired_plugins: Sequence[str] = _parse_requested_plugins(args)
    parser: argparse.ArgumentParser = _parser(
        plugin_definitions, desired_plugins, **kwargs
    )
    args: argparse.Namespace = parser.parse_args(args, namespace)

    # Extract our server options
    server_options: server.ServerOptions = server.ServerOptions(
        host=args.host,
        directory=args.directory,
        log_level=_log_level(args.log_level),
        plugins=args.plugins,
    )

    # Configure logging
    logging.basicConfig(level=server_options.log_level)

    plugin_options: dict[str, plugin.PluginOptions] = {}
    plugin_entry: "EntryPoint"
    for plugin_entry in plugin_definitions:
        if desired_plugins and plugin_entry.name not in desired_plugins:
            continue

        parser: plugin.Plugin = plugin_entry.load()
        plugin_options[plugin_entry.name] = parser.derive_options(
            plugin_entry.name, args
        )

    return server_options, plugin_options


def main(
    plugin_definitions: "EntryPoints | None" = None,
    args: Sequence[str] | None = None,
    namespace: argparse.Namespace = None,
    **kwargs,
) -> None:
    """
    Parse arguments and start the server accordingly.

    Args:
        plugin_definitions: Plugin definitions to handle arguments for.
        args: Sequence of arguments to parse.
        namespace: Namespace of options.
        **kwargs: Keyword arguments to pass for parser initialization.
    """
    if plugin_definitions is None:
        plugin_definitions: "EntryPoints" = plugin.find_plugins()

    options, plugin_options = _parse_arguments(
        plugin_definitions, args, namespace, **kwargs
    )
    with server.Server(options, **plugin_options) as stashhouse:
        try:
            stashhouse.join()
        except KeyboardInterrupt:
            stashhouse.stop()
            stashhouse.join()


__all__ = ("main",)
