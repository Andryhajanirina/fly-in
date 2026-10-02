#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test_zone.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/02 12:48:17 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/02 12:48:22 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from fly_in.zone import Zone


def test_create_zone() -> None:
    zone = Zone(
        name="corridorA",
        x=4,
        y=3,
        zone_type="priority",
        color="green",
        max_drones=2,
    )

    assert zone.name == "corridorA"
    assert zone.x == 4
    assert zone.y == 3
    assert zone.zone_type == "priority"
    assert zone.color == "green"
    assert zone.max_drones == 2
