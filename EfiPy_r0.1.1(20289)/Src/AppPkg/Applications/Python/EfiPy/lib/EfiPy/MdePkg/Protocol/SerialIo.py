#
# SerialIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SerialIo.py is free software: you can redistribute it and/or
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

gEfiSerialIoProtocolGuid  = \
  EFI_GUID (0xBB25CF6F, 0xF1D4, 0x11D2, (0x9A, 0x0C, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0xFD ))

class EFI_SERIAL_IO_PROTOCOL (Structure):
  pass

DefaultParity   = 0
NoParity        = 1
EvenParity      = 2
OddParity       = 3
MarkParity      = 4
SpaceParity     = 5
EFI_PARITY_TYPE = ENUM

DefaultStopBits     = 0
OneStopBit          = 1
OneFiveStopBits     = 2
TwoStopBits         = 3
EFI_STOP_BITS_TYPE  = ENUM

EFI_SERIAL_CLEAR_TO_SEND        = 0x00000010
EFI_SERIAL_DATA_SET_READY       = 0x00000020
EFI_SERIAL_RING_INDICATE        = 0x00000040
EFI_SERIAL_CARRIER_DETECT       = 0x00000080
EFI_SERIAL_INPUT_BUFFER_EMPTY   = 0x00000100
EFI_SERIAL_OUTPUT_BUFFER_EMPTY  = 0x00000200

EFI_SERIAL_REQUEST_TO_SEND      = 0x00000002
EFI_SERIAL_DATA_TERMINAL_READY  = 0x00000001

EFI_SERIAL_HARDWARE_LOOPBACK_ENABLE     = 0x00001000
EFI_SERIAL_SOFTWARE_LOOPBACK_ENABLE     = 0x00002000
EFI_SERIAL_HARDWARE_FLOW_CONTROL_ENABLE = 0x00004000

EFI_SERIAL_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERIAL_IO_PROTOCOL) # IN      *This
  )

EFI_SERIAL_SET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERIAL_IO_PROTOCOL),# IN *This
  UINT64,                         # IN BaudRate,
  UINT32,                         # IN ReceiveFifoDepth,
  UINT32,                         # IN Timeout,
  EFI_PARITY_TYPE,                # IN Parity,
  UINT8,                          # IN DataBits,
  EFI_STOP_BITS_TYPE              # IN StopBits
  )

EFI_SERIAL_SET_CONTROL_BITS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERIAL_IO_PROTOCOL),# IN *This
  UINT32                          # IN Control
  )

EFI_SERIAL_GET_CONTROL_BITS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERIAL_IO_PROTOCOL),# IN      *This
  POINTER(UINT32)                 #     OUT *Control
  )

EFI_SERIAL_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERIAL_IO_PROTOCOL),# IN     *This
  POINTER(UINTN),                 # IN OUT *BufferSize,
  PVOID                           # IN     *Buffer
  )

EFI_SERIAL_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERIAL_IO_PROTOCOL),# IN     *This
  POINTER(UINTN),                 # IN OUT *BufferSize,
  PVOID                           #    OUT *Buffer
  )

class EFI_SERIAL_IO_MODE (Structure):
  _fields_ = [
    ("ControlMask",       UINT32),
    ("Timeout",           UINT32),
    ("BaudRate",          UINT64),
    ("ReceiveFifoDepth",  UINT32),
    ("DataBits",          UINT32),
    ("Parity",            UINT32),
    ("StopBits",          UINT32)
  ]

EFI_SERIAL_IO_PROTOCOL_REVISION    = 0x00010000
SERIAL_IO_INTERFACE_REVISION  = EFI_SERIAL_IO_PROTOCOL_REVISION
EFI_SERIAL_IO_PROTOCOL._fields_ = [
    ("Revision",      UINT32),
    ("Reset",         EFI_SERIAL_RESET),
    ("SetAttributes", EFI_SERIAL_SET_ATTRIBUTES),
    ("SetControl",    EFI_SERIAL_SET_CONTROL_BITS),
    ("GetControl",    EFI_SERIAL_GET_CONTROL_BITS),
    ("Write",         EFI_SERIAL_WRITE),
    ("Read",          EFI_SERIAL_READ),
    ("Mode",          POINTER(EFI_SERIAL_IO_MODE))
  ]

