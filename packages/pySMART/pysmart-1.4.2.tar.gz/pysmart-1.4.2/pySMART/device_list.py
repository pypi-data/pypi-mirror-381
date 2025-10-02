# Copyright (C) 2014 Marc Herndon
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
This module contains the definition of the `DeviceList` class, used to
represent all physical storage devices connected to the system.
Once initialized, the sole member `devices` will contain a list of `Device`
objects.

This class has no public methods.  All interaction should be through the
`Device` class API.
"""
# Python built-ins
import re

# pySMART module imports
from .device import Device
from .smartctl import Smartctl, SMARTCTL
from typing import List


class DeviceList(object):
    """
    Represents a list of all the storage devices connected to this computer.
    """

    def __init__(self, init: bool = True, smartctl=SMARTCTL, catch_errors: bool = False):
        """Instantiates and optionally initializes the `DeviceList`.

        Args:
            init (bool, optional): By default, `pySMART.device_list.DeviceList.devices`
                is populated with `Device` objects during instantiation. Setting init
                to False will skip initialization and create an empty
                `pySMART.device_list.DeviceList` object instead. Defaults to True.
            smartctl ([type], optional): This stablish the smartctl wrapper.
                Defaults the global `SMARTCTL` object and should be only
                overwritten on tests.
            catch_errors (bool, optional): If True, individual device-parsing errors will be caught
        """

        self.devices: List[Device] = []
        """
        **(list of `Device`):** Contains all storage devices detected during
        instantiation, as `Device` objects.
        """
        self.smartctl: Smartctl = smartctl
        """The smartctl wrapper
        """
        if init:
            self.initialize(catch_errors)

    def __repr__(self):
        """Define a basic representation of the class object."""
        rep = "<DeviceList contents:\n"
        for device in self.devices:
            rep += str(device) + '\n'
        return rep + '>'
        # return "<DeviceList contents:%r>" % (self.devices)

    def _cleanup(self):
        """
        Removes duplicate ATA devices that correspond to an existing CSMI
        device. Also removes any device with no capacity value, as this
        indicates removable storage, ie: CD/DVD-ROM, ZIP, etc.
        """
        # We can't operate directly on the list while we're iterating
        # over it, so we collect indeces to delete and remove them later
        to_delete = []
        # Enumerate the list to get tuples containing indeces and values
        for index, device in enumerate(self.devices):
            # Allow well-known devices
            if device.interface in ['nvme']:
                continue
            
            # Check for duplicate ATA devices with CSMI devices
            if device.interface == 'csmi':
                for otherindex, otherdevice in enumerate(self.devices):
                    if (otherdevice.interface == 'ata' or
                            otherdevice.interface == 'sata'):
                        if device.serial == otherdevice.serial:
                            to_delete.append(otherindex)
                            device._sd_name = otherdevice.name
            if device.capacity is None and index not in to_delete:
                to_delete.append(index)
        # Recreate the self.devices list without the marked indeces
        self.devices[:] = [v for i, v in enumerate(self.devices)
                           if i not in to_delete]

    def initialize(self, catch_errors: bool = False):
        """
        Scans system busses for attached devices and add them to the
        `DeviceList` as `Device` objects.
        If device list is already populated, it will be cleared first.

        Args:
            catch_errors (bool, optional): If True, individual device-parsing errors will be caught
        """

        # Clear the list if it's already populated
        if len(self.devices):
            self.devices = []

        # Scan for devices
        for line in self.smartctl.scan():
            if not ('failed:' in line or line == ''):
                groups = re.compile(
                    r'^(\S+)\s+-d\s+(\S+)').match(line).groups()
                name = groups[0]
                interface = groups[1]

                try:
                    # Add the device to the list
                    self.devices.append(
                        Device(name, interface=interface, smartctl=self.smartctl))

                except Exception as e:
                    if catch_errors:
                        # Print the exception
                        import logging

                        logging.exception(f"Error parsing device {name}")

                    else:
                        # Reraise the exception
                        raise e

        # Remove duplicates and unwanted devices (optical, etc.) from the list
        self._cleanup()
        # Sort the list alphabetically by device name
        self.devices.sort(key=lambda device: device.name)

    def __getitem__(self, index: int) -> Device:
        """Returns an element from self.devices

        Args:
            index (int): An index of self.devices

        Returns:
            Device: Returns a Device that is located on the asked index
        """
        return self.devices[index]


__all__ = ['DeviceList']
