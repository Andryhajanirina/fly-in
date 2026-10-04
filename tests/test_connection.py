#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test_connection.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/04 11:18:41 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/04 11:33:54 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from fly_in.zone import Zone
from fly_in.connection import Connection


def test_create_connection_with_capacity() -> None:
    zone_a = Zone("A", 0, 0)
    zone_b = Zone("B", 1, 0)
    connection = Connection(
        zone_a=zone_a,
        zone_b=zone_b,
        max_link_capacity=2,
    )

    assert connection.zone_a == zone_a
    assert connection.zone_b == zone_b
    assert connection.max_link_capacity == 2


def test_create_connection_default_capacity() -> None:
    zone_a = Zone("A", 0, 0)
    zone_b = Zone("B", 1, 0)
    connection = Connection(
        zone_a,
        zone_b,
    )

    assert connection.max_link_capacity == 1
