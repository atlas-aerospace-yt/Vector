from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '0.0.3'
DESCRIPTION = 'A simple python vector package.'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="vector-ai-ml",
    version=VERSION,
    author="AtlasAerospace (Alexander Armitage)",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    keywords=['python', 'math', 'ai', 'ml', 'artificialintelligence'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)