#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   zone.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/02 12:46:30 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/02 14:44:49 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from dataclasses import dataclass


@dataclass
class Zone:
    """Represent a zone in the drone network."""
    name: str
    x: int
    y: int
    zone_type: str = "normal"
    color: str = "none"
    max_drones: int = 1
