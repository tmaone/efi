#
# Timer.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Timer.py is free software: you can redistribute it and/or
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

gEfiTimerArchProtocolGuid   = \
  EFI_GUID (0x26baccb3, 0x6f42, 0x11d4, (0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

class EFI_TIMER_ARCH_PROTOCOL (Structure):
  pass

EFI_TIMER_NOTIFY = CFUNCTYPE (
  VOID,
  UINT64  # IN UINT64
  )

EFI_TIMER_REGISTER_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIMER_ARCH_PROTOCOL),   # IN  *This
  EFI_TIMER_NOTIFY                    # IN  NotifyFunction
  )

EFI_TIMER_SET_TIMER_PERIOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIMER_ARCH_PROTOCOL),   # IN  *This
  UINT64                              # IN  TimerPeriod
  )

EFI_TIMER_GET_TIMER_PERIOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIMER_ARCH_PROTOCOL),   # IN  *This
  POINTER(UINT64)                     # OUT *TimerPeriod
  )

EFI_TIMER_GENERATE_SOFT_INTERRUPT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIMER_ARCH_PROTOCOL)    # IN  *This
  )

EFI_TIMER_ARCH_PROTOCOL._fields_ = [
    ("RegisterHandler",       EFI_TIMER_REGISTER_HANDLER),
    ("SetTimerPeriod",        EFI_TIMER_SET_TIMER_PERIOD),
    ("GetTimerPeriod",        EFI_TIMER_GET_TIMER_PERIOD),
    ("GenerateSoftInterrupt", EFI_TIMER_GENERATE_SOFT_INTERRUPT)
  ]
