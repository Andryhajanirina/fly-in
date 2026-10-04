#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test_graph.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/04 11:47:16 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/04 13:59:29 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from fly_in.zone import Zone
from fly_in.connection import Connection
from fly_in.graph import Graph, ZoneNotFoundError
import pytest


def test_add_zone_start_and_goal() -> None:
    graph = Graph()
    start = Zone("A", 0, 0)
    goal = Zone("B", 1, 0)
    graph.add_zone(start)
    graph.add_zone(goal)

    assert graph._zones["A"] == start
    assert graph._zones["B"] == goal


def test_get_known_zone() -> None:
    graph = Graph()
    start = Zone("start", 0, 0)
    junction = Zone("junction", 1, 0)
    graph.add_zone(start)
    graph.add_zone(junction)
    assert graph.get_zone("start") == start
    assert graph.get_zone("junction") == junction


def test_get_unknown_zone() -> None:
    graph = Graph()
    start = Zone("start", 0, 0)
    junction = Zone("junction", 1, 0)
    graph.add_zone(start)
    graph.add_zone(junction)
    assert graph.get_zone("start") == start
    assert graph.get_zone("junction") == junction
    with pytest.raises(ZoneNotFoundError):
        graph.get_zone("Unknown")


def test_add_connection_and_get_neighbors() -> None:
    graph = Graph()

    zone_a = Zone("A", 0, 0)
    zone_b = Zone("B", 1, 0)

    graph.add_zone(zone_a)
    graph.add_zone(zone_b)

    connection = Connection(zone_a, zone_b)
    graph.add_connection(connection)

    assert graph.get_neighbors(zone_a) == [zone_b]
    assert graph.get_neighbors(zone_b) == [zone_a]


def test_add_connection_with_existent_zone_and_inexistent_zone() -> None:
    graph = Graph()

    zone_a = Zone("A", 0, 0)
    zone_b = Zone("B", 1, 0)

    graph.add_zone(zone_a)
    with pytest.raises(ZoneNotFoundError):
        connection = Connection(zone_a, zone_b)
        graph.add_connection(connection)
