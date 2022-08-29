from setuptools import setup

setup(
    name='smpai',
    version='0.1.2a1',    
    description='smpai - A State Machine Framework',
    url='https://github.com/canbatuhan/smpai',
    author='Batuhan Can',
    author_email='batuhanosmancan@gmail.com',
    license='MIT',
    packages=['smpai', 'smpai.builder', 'smpai.components'],
    install_requires=['jsonref', 'PyYAML'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',       
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Typing :: Typed',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'
    ],
)