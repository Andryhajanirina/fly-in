#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   graph.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/04 11:41:55 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/04 13:50:05 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .zone import Zone
from .connection import Connection


class ZoneNotFoundError(Exception):
    """Exception raised when a zone is not found in the graph."""
    pass


class Graph:
    """Represent the drone network."""

    def __init__(self) -> None:
        self._zones: dict[str, Zone] = {}
        self._connections: list[Connection] = []
        self._neighbors: dict[str, list[Zone]] = {}

    def add_zone(self, zone: Zone) -> None:
        self._zones[zone.name] = zone
        self._neighbors[zone.name] = []

    def get_zone(self, name: str) -> Zone:
        try:
            return self._zones[name]
        except KeyError as error:
            raise ZoneNotFoundError(
                f"The zone '{name}' is unknown."
            ) from error

    def add_connection(self, connection: Connection) -> None:
        if (connection.zone_a.name not in self._zones):
            raise ZoneNotFoundError(
                f"The zone '{connection.zone_a.name}' is unknown."
            )

        if (connection.zone_b.name not in self._zones):
            raise ZoneNotFoundError(
                f"The zone '{connection.zone_b.name}' is unknown."
            )

        self._connections.append(connection)
        self._neighbors[connection.zone_a.name].append(
            connection.zone_b
        )
        self._neighbors[connection.zone_b.name].append(
            connection.zone_a
        )

    def get_neighbors(self, zone: Zone) -> list[Zone]:
        return self._neighbors[zone.name]
