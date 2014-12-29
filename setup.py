#!/usr/bin/env python
# Copyright 2011 The hop Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=C0103

"""Setup script for hop."""

import os.path
from os import makedirs
import sys

from setuptools import setup
from distutils.command import install_data



class hop_install(install_data.install_data):
  """Handle installing data for hop."""

  def run(self):
    """Install commands and dotfiles."""
    install_data.install_data.run(self)
    return True


setup(name='Hop',
      version='1.0',
      description='Easily jump to your favorite directories',
      license='Apache',
      author='Greplin',
      author_email='robbyw@greplin.com',
      url='https://www.github.com/Cue/hop',
      packages=['hop'],
      data_files=[('hop', ['hop/hop.bash', 'hop/hop.sh', 'hop/hop.lua', 'hop/json.lua'])],
      entry_points = {
        'console_scripts': [
          'hop-python-script = hop.hop:main'
        ],
      },
      cmdclass=dict(install_data=hop_install)
     )
