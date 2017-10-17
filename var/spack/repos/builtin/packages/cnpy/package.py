##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Cnpy(CMakePackage):
    """cnpy: library to read/write .npy and .npz files in C/C++."""

    homepage = "https://github.com/rogersce/cnpy"
    url      = "https://github.com/rogersce/cnpy"

    version('master', git='https://github.com/rogersce/cnpy.git', branch="master")
    depends_on('zlib')
    depends_on('zip')
    def configure_args(self):
        args = [
            # not honored, see
            #   https://sourceforge.net/p/libpng/bugs/210/#33f1
            # '--with-zlib=' + self.spec['zlib'].prefix,
            'CFLAGS=-I{0}'.format(self.spec['zlib'].prefix.include, self.spec['zip'].prefix.include),
            'LDFLAGS=-L{0}'.format(self.spec['zlib'].prefix.lib, self.spec['zip'].prefix.lib),
        ]
        configure_args.extend(['CFLAGS=-I{0}'.format(self.spec['zip'].prefix.include)])
        configure_args.extend(['LDFLAGS=-L{0}'.format(self.spec['zip'].prefix.lib)])
        return args
        
