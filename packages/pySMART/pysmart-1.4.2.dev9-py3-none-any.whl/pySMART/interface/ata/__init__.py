# Copyright (C) 2023 Rafael Leira, Naudit HPCN S.L.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.
#
################################################################
"""
This module contains the definition of the `ATA` device interface type.
"""

from enum import Enum
import re
from typing import Optional, Iterator, Union, List

from ..common import CommonIface
from .attribute import Attribute


class AtaAttributes(CommonIface):

    """Class to store the ATA attributes
    """

    @staticmethod
    def has_compatible_data(data: Iterator[str]) -> bool:
        """Checks if the data is compatible with this class

        Args:
            data (Iterator[str]): Iterator of the lines of the output of the command nvme smart-log

        Returns:
            bool: True if compatible, False otherwise
        """

        for line in data:
            if 'Specific SMART Attributes' in line:
                return True

        return False

    def __init__(self, data: Optional[Iterator[str]] = None):
        """Initializes the attributes

        Args:
            data (Iterator[str], optional): Iterator of the lines of the output of the command nvme smart-log. Defaults to None.

        """

        self.legacyAttributes: List[Optional[Attribute]] = [None] * 256
        """
        **(List[Optional[Attribute]]):** List of the ATA attributes. The index is the attribute ID.
        This is the legacy attribute list for ATA devices. It is strongly recommended to other properties when possible.
        """

        self._logical_sector_size: Optional[int] = None
        """
        **(int):** The logical sector size of the device (or LBA).
        """
        self._physical_sector_size: Optional[int] = None
        """
        **(int):** The physical sector size of the device.
        """

        if data is not None:
            self.parse(data)

    def parse(self, data: Iterator[str]) -> None:
        """Parses the attributes from the raw data
        """

        # Advance data until required things are found
        for line in data:
            # SMART Attribute table parsing
            if 'Specific SMART Attributes' in line:
                attribute_re = re.compile(
                    r'^\s*(?P<id>\d+)\s+(?P<name>\S+)\s+(?P<flag>\S+)\s+(?P<value>\d+)\s+(?P<worst>\d+)\s+(?P<thresh>\S+)\s+(?P<type>\S+)\s+(?P<updated>\S+)\s+(?P<whenfailed>\S+)\s+(?P<raw>.+)$')

                # loop until we reach the end of the table (empty line)
                while True:
                    line = next(data).strip()
                    if line == '':
                        break

                    # Parse the line
                    m = attribute_re.match(line)
                    if m is not None:
                        tmp = m.groupdict()
                        self.legacyAttributes[int(tmp['id'])] = Attribute(
                            int(tmp['id']), tmp['name'], int(tmp['flag'], base=16), tmp['value'], tmp['worst'], tmp['thresh'], tmp['type'], tmp['updated'], tmp['whenfailed'], tmp['raw'])

            # Sector sizes
            if 'Sector Sizes' in line:  # ATA
                m = re.match(
                    r'.* (\d+) bytes logical,\s*(\d+) bytes physical', line)
                if m:
                    self._logical_sector_size = int(m.group(1))
                    self._physical_sector_size = int(m.group(2))

                else:
                    m = re.match(r'.* (\d+) bytes logical/physical', line)
                    if m:
                        self._logical_sector_size = int(m.group(1))
                        self._physical_sector_size = int(m.group(1))

                continue

    def __getstate__(self):
        """
        Allows us to send a pySMART diagnostics object over a serializable
        medium which uses json (or the likes of json) payloads
        """
        import copy
        ret = copy.copy(vars(self))

        # for each attribute, get the state. If None, set to None
        ret['legacyAttributes'] = [e.__getstate__()
                                   if e is not None else None
                                   for e in ret['legacyAttributes']]

        return ret

    def __setstate__(self, state):
        self.__dict__.update(state)

    @property
    def temperature(self) -> Optional[int]:
        if self.legacyAttributes[190] is not None or self.legacyAttributes[194] is not None:
            temp_attr = self.legacyAttributes[190] or self.legacyAttributes[194]
            if temp_attr is not None and temp_attr.raw_int is not None:
                return temp_attr.raw_int

        return None

    @property
    def physical_sector_size(self) -> int:
        if self._physical_sector_size is not None:
            return self._physical_sector_size
        elif self._logical_sector_size is not None:
            return self._logical_sector_size
        else:
            return 512

    @property
    def logical_sector_size(self) -> int:
        return self._logical_sector_size if self._logical_sector_size is not None else self.physical_sector_size
