import subprocess
import os

try:
    import rdkit
except ImportError:
    print('rdkit not installed...', file=sys.stderr)
    print('build rdkit...', file=sys.stderr)
    subprocess.call(['git', 'clone', 'https://github.com/rdkit/conda-rdkit.git'])
    os.chdir('conda-rdkit')
    subprocess.call(['conda', 'build', 'boost'])
    subprocess.call(['conda', 'build', 'rdkit'])
