#
# SerialPortConsoleRedirectionTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SerialPortConsoleRedirectionTable.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.IndustryStandard import *

import Acpi

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_REVISION = 0x01

class EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("InterfaceType",         UINT8),
    ("Reserved1",             UINT8 * 3),
    ("BaseAddress",           Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("InterruptType",         UINT8),
    ("Irq",                   UINT8),
    ("GlobalSystemInterrupt", UINT32),
    ("BaudRate",              UINT8),
    ("Parity",                UINT8),
    ("StopBits",              UINT8),
    ("FlowControl",           UINT8),
    ("TerminalType",          UINT8),
    ("Language",              UINT8),
    ("PciDeviceId",           UINT16),
    ("PciVendorId",           UINT16),
    ("PciBusNumber",          UINT8),
    ("PciDeviceNumber",       UINT8),
    ("PciFunctionNumber",     UINT8),
    ("PciFlags",              UINT32),
    ("PciSegment",            UINT8),
    ("Reserved2",             UINT32)
  ]

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_16550   = 0
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_16450   = 1

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_8259    = 0x1
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_APIC    = 0x2
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_SAPIC   = 0x4

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_9600         = 3
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_19200        = 4
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_57600        = 6
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_115200       = 7

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_PARITY_NO_PARITY       = 0

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_STOP_BITS_1            = 1

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_FLOW_CONTROL_DCD       = 0x1
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_FLOW_CONTROL_RTS_CTS   = 0x2
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_FLOW_CONTROL_XON_XOFF  = 0x4

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_VT100      = 0
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_VT100_PLUS = 1
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_VT_UTF8    = 2
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_ANSI       = 3
