
from distutils.core import setup
from pathlib import Path

setup(name = 'lemonade',
      version = '1.0b3',
      url = 'https://github.com/leifboo/lemonade',
      description = 'Port of the LEMON Parser Generator',
      long_description = (Path(__file__).parent / 'README.md').read_text(),
      long_description_content_type = 'text/markdown',

      scripts = ['bin/lemonade'],
      packages = ['lemonade'],
      package_data = { 'lemonade': ['lempar.tmpl'] },
      
      classifiers = [
          'License :: Public Domain',
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Code Generators',
          'Topic :: Software Development :: Compilers',
          ],
      
      author = 'Leif Strand',
      author_email = 'leif.c.strand@gmail.com',
      )
