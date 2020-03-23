#
# MpService.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# MpService.py is free software: you can redistribute it and/or
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

from EfiPy import *

from EfiPy.MdePkg.Pi.PiMultiPhase  import EFI_AP_PROCEDURE

gEfiMpServiceProtocolGuid = \
  EFI_GUID (0x3fdda605, 0xa76e, 0x4f46, (0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x08))

class EFI_MP_SERVICES_PROTOCOL (Structure):
  pass

END_OF_CPU_LIST    = 0xffffffff
PROCESSOR_AS_BSP_BIT         = 0x00000001
PROCESSOR_ENABLED_BIT        = 0x00000002
PROCESSOR_HEALTH_STATUS_BIT  = 0x00000004

class EFI_CPU_PHYSICAL_LOCATION (Structure):
  _fields_ = [
    ("Package", UINT32),
    ("Core",    UINT32),
    ("Thread",  UINT32)
  ]

class EFI_PROCESSOR_INFORMATION (Structure):
  _fields_ = [
    ("ProcessorId", UINT64),
    ("StatusFlag",  UINT32),
    ("Location",    EFI_CPU_PHYSICAL_LOCATION)
  ]

EFI_MP_SERVICES_GET_NUMBER_OF_PROCESSORS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  POINTER(UINTN),                     # OUT *NumberOfProcessors,
  POINTER(UINTN)                      # OUT *NumberOfEnabledProcessors
  )

EFI_MP_SERVICES_GET_PROCESSOR_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  UINTN,                              # IN  ProcessorNumber,
  POINTER(EFI_PROCESSOR_INFORMATION)  # OUT *ProcessorInfoBuffer
  )

EFI_MP_SERVICES_STARTUP_ALL_APS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  EFI_AP_PROCEDURE,                   # IN  Procedure,
  BOOLEAN,                            # IN  SingleThread,
  EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
  UINTN,                              # IN  TimeoutInMicroSeconds,
  PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
  POINTER(POINTER(UINTN))             # OUT **FailedCpuList         OPTIONAL
  )

EFI_MP_SERVICES_STARTUP_THIS_AP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  EFI_AP_PROCEDURE,                   # IN  Procedure,
  UINTN,                              # IN  ProcessorNumber,
  EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
  UINTN,                              # IN  TimeoutInMicroseconds,
  PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
  POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
  )

EFI_MP_SERVICES_SWITCH_BSP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  UINTN,                              # IN  ProcessorNumber,
  BOOLEAN                             # IN  EnableOldBSP
  )

EFI_MP_SERVICES_ENABLEDISABLEAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  UINTN,                              # IN  ProcessorNumber,
  BOOLEAN,                            # IN  EnableAP
  POINTER(UINT32)                     # IN  *HealthFlag OPTIONAL
  )

EFI_MP_SERVICES_WHOAMI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  POINTER(UINTN),                     # OUT *ProcessorNumber
  )

EFI_MP_SERVICES_PROTOCOL._fields_ = [
    ("GetNumberOfProcessors", EFI_MP_SERVICES_GET_NUMBER_OF_PROCESSORS),
    ("GetProcessorInfo",      EFI_MP_SERVICES_GET_PROCESSOR_INFO),
    ("StartupAllAPs",         EFI_MP_SERVICES_STARTUP_ALL_APS),
    ("StartupThisAP",         EFI_MP_SERVICES_STARTUP_THIS_AP),
    ("SwitchBSP",             EFI_MP_SERVICES_SWITCH_BSP),
    ("EnableDisableAP",       EFI_MP_SERVICES_ENABLEDISABLEAP),
    ("WhoAmI",                EFI_MP_SERVICES_WHOAMI)
  ]
