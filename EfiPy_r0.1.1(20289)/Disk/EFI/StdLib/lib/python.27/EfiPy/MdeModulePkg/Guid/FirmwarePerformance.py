#
# FirmwarePerformance.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FirmwarePerformance.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
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

from EfiPy  import *
from EfiPy.MdePkg.IndustryStandard.Acpi import *

class FIRMWARE_PERFORMANCE_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",            EFI_ACPI_DESCRIPTION_HEADER),
  ("BootPointerRecord", EFI_ACPI_5_0_FPDT_BOOT_PERFORMANCE_TABLE_POINTER_RECORD),
  ("S3PointerRecord",   EFI_ACPI_5_0_FPDT_S3_PERFORMANCE_TABLE_POINTER_RECORD)
  ]

class S3_PERFORMANCE_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",    EFI_ACPI_5_0_FPDT_PERFORMANCE_TABLE_HEADER),
  ("S3Resume",  EFI_ACPI_5_0_FPDT_S3_RESUME_RECORD),
  ("S3Suspend", EFI_ACPI_5_0_FPDT_S3_SUSPEND_RECORD)
  ]

class BOOT_PERFORMANCE_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",    EFI_ACPI_5_0_FPDT_PERFORMANCE_TABLE_HEADER),
  ("BasicBoot", EFI_ACPI_5_0_FPDT_FIRMWARE_BASIC_BOOT_RECORD)
  ]

class FIRMWARE_PERFORMANCE_RUNTIME_DATA (Structure):
  _pack_   = 1
  _fields_ = [
  ("BootPerformance", BOOT_PERFORMANCE_TABLE),
  ("S3Performance",   S3_PERFORMANCE_TABLE)
  ]

class FIRMWARE_PERFORMANCE_VARIABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("BootPerformanceTablePointer", EFI_PHYSICAL_ADDRESS),
  ("S3PerformanceTablePointer",   EFI_PHYSICAL_ADDRESS)
  ]

class SMM_BOOT_RECORD_COMMUNICATE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Function",        UINTN),
  ("ReturnStatus",    EFI_STATUS),
  ("BootRecordSize",  UINTN),
  ("BootRecordData",  PVOID)
  ]

gEfiFirmwarePerformanceGuid         = \
  EFI_GUID (0xc095791a, 0x3001, 0x47b2, (0x80, 0xc9, 0xea, 0xc7, 0x31, 0x9f, 0x2f, 0xa4))

gEdkiiFaultTolerantWriteGuid         = \
  EFI_GUID (0xdc65adc, 0xa973, 0x4130, (0x8d, 0xf0, 0x2a, 0xdb, 0xeb, 0x9e, 0x4a, 0x31))
