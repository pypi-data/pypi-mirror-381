# SPDX-FileCopyrightInfo: Copyright © DUNE Project contributors, see file LICENSE.md in module root
# SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception

file(
  WRITE ${metadatafile}
  "DEPBUILDDIRS=${DEPBUILDDIRS}\nDEPS=${DEPS}\nMODULENAME=${MODULENAME}\nINSTALL_PREFIX=${INSTALL_PREFIX}\nCMAKE_FLAGS=${CMAKE_FLAGS}"
)
