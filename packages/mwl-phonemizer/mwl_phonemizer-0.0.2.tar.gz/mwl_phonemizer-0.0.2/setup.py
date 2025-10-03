import os

from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


def get_version():
    """ Find the version of the package"""
    version_file = os.path.join(BASEDIR, 'mwl_phonemizer', 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if alpha and int(alpha) > 0:
        version += f"a{alpha}"
    return version


extra_files = package_files('mwl_phonemizer')


setup(
    name='mwl_phonemizer',
    version=get_version(),
    packages=['mwl_phonemizer'],
    include_package_data=True,
    package_data={'': extra_files},
    url='https://github.com/TigreGoticomwl_phonemizer',
    license='',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    description=''
)
