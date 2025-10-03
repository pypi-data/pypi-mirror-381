import os
import sys
import pybind11
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from distutils.unixccompiler import UnixCCompiler

# Register .mm files as valid source files
UnixCCompiler.src_extensions.append('.mm')

JUCE_PATH = '/Volumes/KUSHS DRIVE/SinesurgeHost/JuceLibraryCode'
PLUGIN_HOST_SOURCE = '/Volumes/KUSHS DRIVE/SinesurgeHost/Source/PluginHost.cpp'  # or .cpp if you use .cpp
JUCE_MODULES_DIR = '/Users/sundaychol/Downloads/JUCE/modules'
# Only compile the PluginHost source and rely on JuceHeader.h includes to pull in the modules
sources = [PLUGIN_HOST_SOURCE]

include_dirs = [
    pybind11.get_include(),
    JUCE_PATH,
    JUCE_MODULES_DIR
]

extra_compile_args = [
    '-std=c++17',
    '-stdlib=libc++',
    '-mmacosx-version-min=10.14',
    '-fvisibility=hidden',  # optional but helps with symbol exports
]

extra_link_args = [
    '-framework', 'CoreAudio',
    '-framework', 'CoreMIDI',
    '-framework', 'CoreFoundation',
    '-framework', 'AudioToolbox',
    '-mmacosx-version-min=10.14',
]

ext_modules = [
    Extension(
        'vsthost',
        sources=sources,
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )
]

class BuildExt(build_ext):
    def build_extensions(self):
        # If your source file is .mm, tell compiler to treat as Obj-C++
        for ext in self.extensions:
            ext.extra_compile_args = extra_compile_args
            ext.extra_link_args = extra_link_args
        build_ext.build_extensions(self)

setup(
    name='sinesurge-vst',
    version='0.2',
    author='sinesurge',
    description='Python bindings for c++ VST Instrument Host',
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExt},
    zip_safe=False,
)
