# -*- coding: utf-8 -*-
# Copyright (C) European Gravitational Observatory (EGO) (2022) and
# Laser Interferometer Gravitational-Wave Observatory (LIGO) (2022)
#
# Author list: Rhys Poulton <poulton@ego-gw.it>
#              Brockill <brockill@uwm.edu>
#              Patrick Godwin <patrick.godwin@ligo.org>
#
# This file is part of igwn-lldd-common.
#
# igwn-lldd-common is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# igwn-lldd-common is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with igwn-lldd-common.  If not, see <http://www.gnu.org/licenses/>.

import logging

try:
    import framel
except ImportError:
    can_check_crc = False
else:
    can_check_crc = True


logger = logging.getLogger()


def check_crc(frame_buffer):
    if frame_buffer[39] != 1:
        logger.warn('No file CRC check present')
        return 1

    # Do a check of the buffer before reading
    nframes = framel.FrameBufCheck(frame_buffer, len(frame_buffer), True)

    # Check if buffer check failed
    if nframes < 0:
        if nframes == -3:
            logger.warn('Unable to allocate memory for the file')
        elif nframes == -4:
            logger.warn('Unable to open the file')
        elif nframes == -5:
            logger.warn(
                'nBytes reported in the file is not the same as'
                'its actual buffer size'
            )
        elif nframes == -6:
            logger.warn('Header checksum failed')
        elif nframes == -7:
            logger.warn('File checksum failed')
        else:
            logger.warn(
                'An unknown error occured when checking' 'the frame buffer'
            )
        return 2

    return 0
