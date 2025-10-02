from setuptools import setup, find_packages

setup(
    name='notemate-files',
    version='0.1.0',
    packages=find_packages(),
    author='Abhi', 
    author_email='abhi@notemate.space', 
    description='A CLI tool to upload files and directories to your NoteMate cloud.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aapka-username/notemate-cli', # Agar aapka GitHub repo hai
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0',
        'tqdm>=4.60.0',
    ],
    entry_points={
        'console_scripts': [
            'notemate-files = notemate_files.cli:main',
        ],
    },
)