/*
 * This file is part of UEFI GPT fdisk.
 *
 * UEFI GPT fdisk is a port of GPT fdisk to UEFI/BIOS.
 * UEFI GPT fdisk est un portage de GPT fdisk vers UEFI/BIOS.
 * Ce fichier a été initié par Bernard Burette en janvier 2014.
 * Ce fichier est récupéré soit de "GNU libc" soit de "dietlibc"
 * soit encore il a été créé de toutes pièces.
 *
 * All this work is copyleft Bernard Burette.
 * Gauche d'auteur Bernard Burette.
 *
 * This program is distributed under the terms of the GNU GPL version 2.
 * La diffusion de ce code est faite selon les termes de la GPL GNU version 2.
 */

#include "libmy.h"
/* Definition for thread-local data handling.  Generic version.
   Copyright (C) 2002-2013 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>.  */

/* An architecture-specific version of this file has to defined a
   number of symbols:

     TLS_TCB_AT_TP  or  TLS_DTV_AT_TP

     The presence of one of these symbols signals which variant of
     the TLS ABI is used.  There are in the moment two variants
     available:

     * the thread pointer points to a thread control block

     * the thread pointer points to the dynamic thread vector


     TLS_TCB_SIZE

     This is the size of the thread control block structure.  How
     this is actually defined depends on the ABI.  The thread control
     block could be internal descriptor of the thread library or
     just a data structure which allows finding the DTV.

     TLS_INIT_TCB_SIZE

     Similarly, but this value is only used at startup and in the
     dynamic linker itself.  There are no threads in use at that time.


     TLS_TCB_ALIGN

     Alignment requirements for the TCB structure.

     TLS_INIT_TCB_ALIGN

     Similarly, but for the structure used at startup time.


     INSTALL_DTV(tcb, init_dtv)

     This macro must install the given initial DTV into the thread control
     block TCB.  The normal runtime functionality must then be able to
     use the value.


     TLS_INIT_TP(tcb, firstcall)

     This macro must initialize the thread pointer to enable normal TLS
     operation.  The first parameter is a pointer to the thread control
     block.  The second parameter specifies whether this is the first
     call for the TCB.  ld.so calls this macro more than once.


     THREAD_DTV()

     This macro returns the address of the DTV of the current thread.
     This normally is done using the thread register which points
     to the dtv or the TCB (from which the DTV can found).
  */
