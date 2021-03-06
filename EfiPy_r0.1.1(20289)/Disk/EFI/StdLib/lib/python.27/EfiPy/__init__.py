#!/usr/bin/python

#
# __init__.py
#
# Copyright (C) 2015-2016 efipy.core@gmail.com All rights reserved.
#
# __init__.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import _EfiPy
from ctypes   import *
from ctypes   import _SimpleCData

from EfiPy.MdePkg.Uefi.UefiBaseType import *
from EfiPy.MdePkg.Uefi.UefiSpec     import *

from _EfiPy import EFIPY_MDE_CPU_IA32
from _EfiPy import EFIPY_MDE_CPU_IPF
from _EfiPy import EFIPY_MDE_CPU_X64
from _EfiPy import EFIPY_MDE_CPU_ARM
from _EfiPy import EFIPY_MDE_CPU_AARCH64
from _EfiPy import EFIPY_MDE_CPU_EBC

from _EfiPy import EFIPY_MDE_CPU_TYPE

#
# UEFI basic tables gST, gRT, gBS
#

gRT = EFI_RUNTIME_SERVICES.from_address (_EfiPy.EfiPygRtAddr)
gST = EFI_SYSTEM_TABLE.from_address     (_EfiPy.EfiPygStAddr)
gBS = EFI_BOOT_SERVICES.from_address    (_EfiPy.EfiPygBsAddr)

#
# EDK basic image handle
#

gImageHandle = EFI_HANDLE.from_address( _EfiPy.gImageHandle)
pImageHandle = EFI_HANDLE.from_address( _EfiPy.pImageHandle)