# Copyright (C) 2022 Rafael Leira, Naudit HPCN S.L.
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
Copyright (C) 2022 Rafael Leira, Naudit HPCN S.L.

This package contains the special objects to handle and store data related to disk interfaces.
This is required as ATA disks and NVMe disks have different attributes and different ways to get them.
"""

from .ata import AtaAttributes
from .common import CommonIface
from .nvme import NvmeAttributes, NvmeError
from .scsi import SCSIAttributes


__all__ = [
    'AtaAttributes',
    'CommonIface',
    'NvmeAttributes',
    'SCSIAttributes',
]
