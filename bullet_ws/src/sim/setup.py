from setuptools import setup
import os
from glob import glob

package_name = 'sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'models'), glob('models/*.pt')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.stl')),
        (os.path.join('share', package_name, 'imgs'), glob('imgs/*.png')),
        (os.path.join('share', package_name, 'imgs'), glob('imgs/*.npy')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TODO',
    maintainer_email='TODO',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sim = sim.sim:main',
            'vision = sim.vision:main',
            'strat = sim.strat:main',
            'comms = sim.comms:main',
            'gui = sim.gui:main',
            'tests = sim.tests:main',
            'stratmax = sim.stratMax:main',
        ],
    },
)