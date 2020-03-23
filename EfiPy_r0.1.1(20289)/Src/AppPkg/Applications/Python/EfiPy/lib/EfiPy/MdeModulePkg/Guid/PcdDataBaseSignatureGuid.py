#
# PcdDataBaseSignatureGuid.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# PcdDataBaseSignatureGuid.py is free software: you can redistribute it and/or
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

gPcdDataBaseSignatureGuid         = \
  EFI_GUID (0x3c7d193c, 0x682c, 0x4c14, (0xa6, 0x8f, 0x55, 0x2d, 0xea, 0x4f, 0x43, 0x7e))

SKU_ID  = UINT8
PCD_TYPE_SHIFT        = 28
PCD_TYPE_DATA         = (0x0L << PCD_TYPE_SHIFT)
PCD_TYPE_HII          = (0x8L << PCD_TYPE_SHIFT)
PCD_TYPE_VPD          = (0x4L << PCD_TYPE_SHIFT)
PCD_TYPE_SKU_ENABLED  = (0x2L << PCD_TYPE_SHIFT)
PCD_TYPE_STRING       = (0x1L << PCD_TYPE_SHIFT)

PCD_TYPE_ALL_SET      = (PCD_TYPE_DATA | PCD_TYPE_HII | PCD_TYPE_VPD | PCD_TYPE_SKU_ENABLED | PCD_TYPE_STRING)

PCD_DATUM_TYPE_SHIFT  = 24
PCD_DATUM_TYPE_POINTER  = (0x0L << PCD_DATUM_TYPE_SHIFT)
PCD_DATUM_TYPE_UINT8    = (0x1L << PCD_DATUM_TYPE_SHIFT)
PCD_DATUM_TYPE_UINT16   = (0x2L << PCD_DATUM_TYPE_SHIFT)
PCD_DATUM_TYPE_UINT32   = (0x4L << PCD_DATUM_TYPE_SHIFT)
PCD_DATUM_TYPE_UINT64   = (0x8L << PCD_DATUM_TYPE_SHIFT)

PCD_DATUM_TYPE_ALL_SET =(PCD_DATUM_TYPE_POINTER | \
                         PCD_DATUM_TYPE_UINT8   | \
                         PCD_DATUM_TYPE_UINT16  | \
                         PCD_DATUM_TYPE_UINT32  | \
                         PCD_DATUM_TYPE_UINT64)

PCD_DATUM_TYPE_SHIFT2 = 20

PCD_DATUM_TYPE_UINT8_BOOLEAN = (0x1L << PCD_DATUM_TYPE_SHIFT2)

PCD_DATABASE_OFFSET_MASK = (~(PCD_TYPE_ALL_SET | PCD_DATUM_TYPE_ALL_SET | PCD_DATUM_TYPE_UINT8_BOOLEAN))

class DYNAMICEX_MAPPING (Structure):
  _fields_ = [
  ("ExTokenNumber", UINT32),
  ("TokenNumber",   UINT16),
  ("ExGuidIndex",   UINT16)
  ]

class SKU_HEAD (Structure):
  _fields_ = [
  ("SkuDataStartOffset", UINT32),
  ("SkuIdTableOffset",   UINT32)
  ]

class VARIABLE_HEAD (Structure):
  _fields_ = [
  ("StringIndex",         UINT32),
  ("DefaultValueOffset",  UINT32),
  ("GuidTableIndex",      UINT16),
  ("Offset",              UINT16),
  ("Attributes",          UINT32),
  ("Property",            UINT16),
  ("Reserved",            UINT16)
  ]

class VPD_HEAD (Structure):
  _fields_ = [
  ("Offset",  UINT32)
  ]

STRING_HEAD = UINT32
SIZE_INFO   = UINT16

class PCD_NAME_INDEX (Structure):
  _fields_ = [
  ("TokenSpaceCNameIndex",  UINT32),
  ("PcdCNameIndex",         UINT32)
  ]

TABLE_OFFSET  = UINT32

class PCD_DATABASE_INIT (Structure):
  _fields_ = [
      ("Signature",                     GUID),
      ("BuildVersion",                  UINT32),
      ("Length",                        UINT32),
      ("UninitDataBaseSize",            UINT32),
      ("LocalTokenNumberTableOffset",   TABLE_OFFSET),
      ("ExMapTableOffset",              TABLE_OFFSET),
      ("GuidTableOffset",               TABLE_OFFSET),
      ("StringTableOffset",             TABLE_OFFSET),
      ("SizeTableOffset",               TABLE_OFFSET),
      ("SkuIdTableOffset",              TABLE_OFFSET),
      ("PcdNameTableOffset",            TABLE_OFFSET),
      ("LocalTokenCount",               UINT16),
      ("ExTokenCount",                  UINT16),
      ("GuidTableCount",                UINT16),
      ("SystemSkuId",                   SKU_ID),
      ("Pad",                           UINT8)

#     ("ValueUint64",                   UINT64 * N),
#     ("ValueUint32",                   UINT32 * N),
#     ("VpdHead",                       VPD_HEAD * N),
#     ("ExMapTable",                    DYNAMICEX_MAPPING * N),
#     ("LocalTokenNumberTable",         UINT32 * N),
#     ("GuidTable",                     GUID * N),
#     ("StringHead",                    STRING_HEAD * N),
#     ("PcdNameTable",                  PCD_NAME_INDEX * N),
#     ("VariableHead",                  VARIABLE_HEAD * N),
#     ("SkuHead",                       SKU_HEAD * N),
#     ("StringTable",                   UINT8 * N),
#     ("SizeTable",                     SIZE_INFO * N),
#     ("ValueUint16",                   UINT16 * N),
#     ("ValueUint8",                    UINT8 * N),
#     ("ValueBoolean",                  BOOLEAN * N),
#     ("SkuIdTable",                    UINT8 * N),
#     ("SkuIndexTable",                 UINT8 * N)
  ]

PEI_PCD_DATABASE  = PCD_DATABASE_INIT
DXE_PCD_DATABASE  = PCD_DATABASE_INIT
class PCD_DATABASE (Structure):
  _fields_ = [
  ("PeiDb",  POINTER(PEI_PCD_DATABASE)),
  ("DxeDb",  POINTER(DXE_PCD_DATABASE))
  ]
