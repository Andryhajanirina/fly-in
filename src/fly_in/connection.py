#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   connection.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/04 11:14:11 by andry-ha            #+#    #+#            #
#   Updated: 2026/10/04 11:16:08 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from dataclasses import dataclass
from .zone import Zone


@dataclass
class Connection:
    """Represent a bidirectional connection between two zones."""
    zone_a: Zone
    zone_b: Zone
    max_link_capacity: int = 1
