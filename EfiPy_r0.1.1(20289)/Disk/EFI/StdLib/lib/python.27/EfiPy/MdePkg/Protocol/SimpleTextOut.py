#
# SimpleTextOut.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SimpleTextOut.py is free software: you can redistribute it and/or
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

gEfiSimpleTextOutProtocolGuid = EFI_GUID( 0x387477c2, 0x69c7, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b))

class EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL (Structure):
  pass

BOXDRAW_HORIZONTAL                  = 0x2500
BOXDRAW_VERTICAL                    = 0x2502
BOXDRAW_DOWN_RIGHT                  = 0x250c
BOXDRAW_DOWN_LEFT                   = 0x2510
BOXDRAW_UP_RIGHT                    = 0x2514
BOXDRAW_UP_LEFT                     = 0x2518
BOXDRAW_VERTICAL_RIGHT              = 0x251c
BOXDRAW_VERTICAL_LEFT               = 0x2524
BOXDRAW_DOWN_HORIZONTAL             = 0x252c
BOXDRAW_UP_HORIZONTAL               = 0x2534
BOXDRAW_VERTICAL_HORIZONTAL         = 0x253c
BOXDRAW_DOUBLE_HORIZONTAL           = 0x2550
BOXDRAW_DOUBLE_VERTICAL             = 0x2551
BOXDRAW_DOWN_RIGHT_DOUBLE           = 0x2552
BOXDRAW_DOWN_DOUBLE_RIGHT           = 0x2553
BOXDRAW_DOUBLE_DOWN_RIGHT           = 0x2554
BOXDRAW_DOWN_LEFT_DOUBLE            = 0x2555
BOXDRAW_DOWN_DOUBLE_LEFT            = 0x2556
BOXDRAW_DOUBLE_DOWN_LEFT            = 0x2557
BOXDRAW_UP_RIGHT_DOUBLE             = 0x2558
BOXDRAW_UP_DOUBLE_RIGHT             = 0x2559
BOXDRAW_DOUBLE_UP_RIGHT             = 0x255a
BOXDRAW_UP_LEFT_DOUBLE              = 0x255b
BOXDRAW_UP_DOUBLE_LEFT              = 0x255c
BOXDRAW_DOUBLE_UP_LEFT              = 0x255d
BOXDRAW_VERTICAL_RIGHT_DOUBLE       = 0x255e
BOXDRAW_VERTICAL_DOUBLE_RIGHT       = 0x255f
BOXDRAW_DOUBLE_VERTICAL_RIGHT       = 0x2560
BOXDRAW_VERTICAL_LEFT_DOUBLE        = 0x2561
BOXDRAW_VERTICAL_DOUBLE_LEFT        = 0x2562
BOXDRAW_DOUBLE_VERTICAL_LEFT        = 0x2563
BOXDRAW_DOWN_HORIZONTAL_DOUBLE      = 0x2564
BOXDRAW_DOWN_DOUBLE_HORIZONTAL      = 0x2565
BOXDRAW_DOUBLE_DOWN_HORIZONTAL      = 0x2566
BOXDRAW_UP_HORIZONTAL_DOUBLE        = 0x2567
BOXDRAW_UP_DOUBLE_HORIZONTAL        = 0x2568
BOXDRAW_DOUBLE_UP_HORIZONTAL        = 0x2569
BOXDRAW_VERTICAL_HORIZONTAL_DOUBLE  = 0x256a
BOXDRAW_VERTICAL_DOUBLE_HORIZONTAL  = 0x256b
BOXDRAW_DOUBLE_VERTICAL_HORIZONTAL  = 0x256c

BLOCKELEMENT_FULL_BLOCK   = 0x2588
BLOCKELEMENT_LIGHT_SHADE  = 0x2591

GEOMETRICSHAPE_UP_TRIANGLE    = 0x25b2
GEOMETRICSHAPE_RIGHT_TRIANGLE = 0x25ba
GEOMETRICSHAPE_DOWN_TRIANGLE  = 0x25bc
GEOMETRICSHAPE_LEFT_TRIANGLE  = 0x25c4

ARROW_LEFT  = 0x2190
ARROW_UP    = 0x2191
ARROW_RIGHT = 0x2192
ARROW_DOWN  = 0x2193

EFI_BLACK                 = 0x00
EFI_BLUE                  = 0x01
EFI_GREEN                 = 0x02
EFI_CYAN                  = EFI_BLUE | EFI_GREEN
EFI_RED                   = 0x04
EFI_MAGENTA               = EFI_BLUE | EFI_RED
EFI_BROWN                 = EFI_GREEN | EFI_RED
EFI_LIGHTGRAY             = EFI_BLUE | EFI_GREEN | EFI_RED
EFI_BRIGHT                = 0x08
EFI_DARKGRAY              = EFI_BLACK | EFI_BRIGHT
EFI_LIGHTBLUE             = EFI_BLUE | EFI_BRIGHT
EFI_LIGHTGREEN            = EFI_GREEN | EFI_BRIGHT
EFI_LIGHTCYAN             = EFI_CYAN | EFI_BRIGHT
EFI_LIGHTRED              = EFI_RED | EFI_BRIGHT
EFI_LIGHTMAGENTA          = EFI_MAGENTA | EFI_BRIGHT
EFI_YELLOW                = EFI_BROWN | EFI_BRIGHT
EFI_WHITE                 = EFI_BLUE | EFI_GREEN | EFI_RED | EFI_BRIGHT

def EFI_TEXT_ATTR(Foreground, Background):

  return Foreground | (Background << 4)

EFI_BACKGROUND_BLACK      = 0x00
EFI_BACKGROUND_BLUE       = 0x10
EFI_BACKGROUND_GREEN      = 0x20
EFI_BACKGROUND_CYAN       = EFI_BACKGROUND_BLUE | EFI_BACKGROUND_GREEN
EFI_BACKGROUND_RED        = 0x40
EFI_BACKGROUND_MAGENTA    = EFI_BACKGROUND_BLUE | EFI_BACKGROUND_RED
EFI_BACKGROUND_BROWN      = EFI_BACKGROUND_GREEN | EFI_BACKGROUND_RED
EFI_BACKGROUND_LIGHTGRAY  = EFI_BACKGROUND_BLUE | EFI_BACKGROUND_GREEN | EFI_BACKGROUND_RED

EFI_WIDE_ATTRIBUTE  = 0x80

EFI_TEXT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  BOOLEAN                                   # IN ExtendedVerification
  )

EFI_TEXT_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  PCHAR16                                   # IN *String
  )

EFI_TEXT_TEST_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  PCHAR16                                   # IN *String
  )

EFI_TEXT_QUERY_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN  *This
  UINTN,                                    # IN  ModeNumber
  POINTER(UINTN),                           # OUT *Columns
  POINTER(UINTN)                            # OUT *Rows
  )

EFI_TEXT_SET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  UINTN                                     # IN ModeNumber
  )

EFI_TEXT_SET_ATTRIBUTE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  UINTN                                     # IN Attribute
  )

EFI_TEXT_CLEAR_SCREEN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)  # IN *This
  )

EFI_TEXT_SET_CURSOR_POSITION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  UINTN,                                    # IN Column
  UINTN                                     # IN Row
  )

EFI_TEXT_ENABLE_CURSOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL), # IN *This
  BOOLEAN                                   # IN Visible
  )

class EFI_SIMPLE_TEXT_OUTPUT_MODE (Structure):
  _fields_ = [
    ("MaxMode",       INT32),
    ("Mode",          INT32),
    ("Attribute",     INT32),
    ("CursorColumn",  INT32),
    ("CursorRow",     INT32),
    ("CursorVisible", BOOLEAN)
    ]

EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL._fields_ = [
  ("Reset",             EFI_TEXT_RESET),
  ("OutputString",      EFI_TEXT_STRING),
  ("TestString",        EFI_TEXT_TEST_STRING),
  ("QueryMode",         EFI_TEXT_QUERY_MODE),
  ("SetMode",           EFI_TEXT_SET_MODE),
  ("SetAttribute",      EFI_TEXT_SET_ATTRIBUTE),
  ("ClearScreen",       EFI_TEXT_CLEAR_SCREEN),
  ("SetCursorPosition", EFI_TEXT_SET_CURSOR_POSITION),
  ("EnableCursor",      EFI_TEXT_ENABLE_CURSOR),
  ("Mode",              POINTER(EFI_SIMPLE_TEXT_OUTPUT_MODE))
  ]
