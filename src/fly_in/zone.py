#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   zone.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/02 12:46:30 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/02 12:46:41 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from dataclasses import dataclass


@dataclass
class Zone:
    name: str
    x: int
    y: int
    zone_type: str = "normal"
    color: str = "none"
    max_drones: int = 1
