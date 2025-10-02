// SPDX-FileCopyrightText: Copyright © DUNE Project contributors, see file LICENSE.md in module root
// SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception

#include <dune/grid/yaspgrid.hh>
#include <dune/grid/io/file/dgfparser.hh>
#include "../dgfyasp.hh"
#include "checkdgf.hh"

using namespace Dune;

int main(int argc, char ** argv)
try {
#ifdef TESTCOORDINATES
  using Grid=YaspGrid<2,EquidistantOffsetCoordinates<double,2>>;
#else
  using Grid=YaspGrid<3>;
#endif
  runDGFTest<Grid>(argc,argv);
  return 0;
}
catch( const Dune::Exception &e )
{
  std::cerr << e << std::endl;
  return 1;
}
catch (...)
{
  std::cerr << "Generic exception!" << std::endl;
  return 1;
}
