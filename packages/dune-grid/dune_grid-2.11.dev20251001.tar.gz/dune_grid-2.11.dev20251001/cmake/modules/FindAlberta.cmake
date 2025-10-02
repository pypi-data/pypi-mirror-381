# SPDX-FileCopyrightText: Copyright © DUNE Project contributors, see file LICENSE.md in module root
# SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception

#[=======================================================================[.rst:
FindAlberta
-----------

Find Alberta, an Adaptive multiLevel finite element toolbox using Bisectioning
refinement and Error control by Residual Techniques for scientific Applications.
(see https://gitlab.com/alberta-fem/alberta3)

Imported targets
^^^^^^^^^^^^^^^^

This module defines the following :prop_tgt:`IMPORTED` target:

``Alberta::AlbertaGrid_[n]d``
  Dimension dependent library

Result Variables
^^^^^^^^^^^^^^^^

This module defines the following variables:

``Alberta_FOUND``
  The Alberta library with all its dependencies is found

Cache Variables
^^^^^^^^^^^^^^^

The following variables may be set to influence this module's behavior:

``ENV{PKG_CONFIG_PATH}``
  Directory containing the `alberta-grid_[n]d.pc` pkg-config files.
  An environmental variable to influence the search procedure of pkg-config
  for finding Alberta.

``Alberta_ROOT``
  A directory that contains the sub directories `lib/pkgconfig` with
  pkg-config files as above. This directory takes precedence over any system
  path that also contains Alberta pkg-config files.

``Alberta_DEBUG``
  If set to `true` try to find and use the debugging library. This requires
  that a corresponding `alberta-grid_[n]d_debug.pc` file can be found.

``Alberta_FIND_QUIETLY``
  If set to `ON` do not print detailed information during search for
  Alberta using pkg-config. This variable is automatically if `find_package`
  if invoked with flag `QUIET`.

``ALBERTA_MAX_WORLD_DIM``
  Maximal world dimension to check for Alberta library. Default: 3.

#]=======================================================================]

# text for feature summary
include(FeatureSummary)
set_package_properties("Alberta" PROPERTIES
  URL "https://gitlab.com/alberta-fem/alberta3"
  DESCRIPTION "An adaptive hierarchical finite element toolbox and grid manager")

set(ALBERTA_MAX_WORLD_DIM "3" CACHE STRING "Maximal world dimension to check for Alberta library.")

set(ALBERTA_WORLD_DIMS)
set(ALBERTA_GRID_VERSION)
set(ALBERTA_GRID_PREFIX)

# search for Alberta using pkg-config
find_package(PkgConfig)
if(PkgConfig_FOUND)
  set(_old_cmake_prefix_path ${CMAKE_PREFIX_PATH})
  if(Alberta_ROOT)
    list(APPEND CMAKE_PREFIX_PATH ${Alberta_ROOT})
  endif()
  foreach(dim RANGE 1 ${ALBERTA_MAX_WORLD_DIM})
    set(ALBERTA_PKGS "alberta-grid_${dim}d")
    if(Alberta_DEBUG)
      list(INSERT ALBERTA_PKGS 0 "alberta-grid_${dim}d_debug")
    endif()
    foreach(pkg ${ALBERTA_PKGS})
      if(Alberta_FIND_VERSION)
        string(APPEND pkg ">=${Alberta_FIND_VERSION}")
      endif()

      if(Alberta_FIND_QUIETLY)
        pkg_check_modules(Alberta${dim}D QUIET IMPORTED_TARGET GLOBAL ${pkg})
      else()
        pkg_check_modules(Alberta${dim}D IMPORTED_TARGET GLOBAL ${pkg})
      endif()
      if(Alberta${dim}D_FOUND)
        list(APPEND ALBERTA_WORLD_DIMS ${dim})
        set(ALBERTA_GRID_VERSION ${Alberta${dim}D_VERSION})
        set(ALBERTA_GRID_PREFIX ${Alberta${dim}D_PREFIX})
        break()
      endif()
    endforeach(pkg)
  endforeach(dim)
  set(CMAKE_PREFIX_PATH ${_old_cmake_prefix_path})
endif()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args("Alberta"
  REQUIRED_VARS
    ALBERTA_GRID_PREFIX PkgConfig_FOUND
  VERSION_VAR
    ALBERTA_GRID_VERSION
  FAIL_MESSAGE "Could NOT find Alberta (set PKG_CONFIG_PATH to include the location of the alberta-grid_[n]d.pc files)"
)

if(Alberta_FOUND)

  if(ALBERTA_GRID_VERSION VERSION_LESS 3.1.0)
    unset(HAVE_STDBOOL_H_HEADER)
    include(CheckIncludeFileCXX)
    check_include_file_cxx("stdbool.h" HAVE_STDBOOL_H_HEADER)
  endif()

  foreach(dim ${ALBERTA_WORLD_DIMS})
    if(NOT Alberta::AlbertaGrid${dim}D)
      if (${HAVE_STDBOOL_H_HEADER})
         # Tell Alberta(<3.1.0) that we have a stdbool.h header so that it doesn't
         # try to define `bool` itself (which would lead to a `typedef bool bool`
         # and hence a compile error in clang).
         target_compile_definitions(PkgConfig::Alberta${dim}D INTERFACE -DHAVE_STDBOOL_H)
      endif()
      add_library(Alberta::AlbertaGrid${dim}D ALIAS PkgConfig::Alberta${dim}D)
    endif()
  endforeach(dim)
endif()
