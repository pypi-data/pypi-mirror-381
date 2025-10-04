#!/usr/bin/env python
from setuptools import setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dbt-model-erd",
    version="0.1.0",
    author="Entechlog",
    description="Generate entity-relationship diagrams for dbt models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/entechlog/dbt-model-erd",
    py_modules=[
        "__init__",
        "config",
        "dbt_erd",
        "mermaid_generator",
        "mermaid_renderer",
        "model_analyzer",
        "utils",
        "yaml_manager",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=5.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "ruff>=0.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dbt-model-erd=dbt_erd:main",
        ],
    },
    include_package_data=True,
)
