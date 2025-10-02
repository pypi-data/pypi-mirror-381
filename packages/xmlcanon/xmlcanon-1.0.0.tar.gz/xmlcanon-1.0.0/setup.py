"""
Установочный скрипт для модуля exc_c14n
"""

from setuptools import setup, find_packages
import os

# Читаем README файл
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Читаем requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="xmlcanon",
    version="1.0.0",
    author="Daniil (imdeniil)",
    author_email="keemor821@gmail.com",
    description="XML Canonicalization для Python",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/imdeniil/xmlcanon",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: XML",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "lxml": ["lxml>=4.0.0"],
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ]
    },
    include_package_data=True,
    package_data={
        "xmlcanon": ["py.typed"],
    },
    entry_points={
        "console_scripts": [
            "xmlcanon=xmlcanon.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/imdeniil/xmlcanon/issues",
        "Source": "https://github.com/imdeniil/xmlcanon",
    },
    keywords="xml canonicalization exc-c14n xmldsig gost signature",
    test_suite="tests",
)