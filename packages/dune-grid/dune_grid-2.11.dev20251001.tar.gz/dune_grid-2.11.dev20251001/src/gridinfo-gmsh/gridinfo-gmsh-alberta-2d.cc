// SPDX-FileCopyrightText: Copyright © DUNE Project contributors, see file COPYING in module root
// SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception
// -*- tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 2 -*-
// vi: set et ts=4 sw=2 sts=2:

#include <string>

#include <dune/grid/albertagrid.hh>

const std::string programName = "dune-gridinfo-gmsh-alberta-2d";
typedef Dune::AlbertaGrid<2, 2> Grid;

#include <dune/grid/utility/gridinfo-gmsh-main.hh>
