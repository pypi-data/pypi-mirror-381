from setuptools import setup, find_packages

setup(
    name="scriptthing",
    version="0.1.0",
    description="A tool for managing scripts in various languages with powerful output formatting capabilities",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "click",
        "jinja2",
        "pyyaml",
        "humanfriendly>=10.0"
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0"
        ],
        "mcp": [
            "fastmcp"
        ]
    },
    entry_points={
        "console_scripts": [
            "scriptthing = scriptthing.cli:cli",
            "scriptthing-run = scriptthing.runtime:main"
        ]
    },
    package_data={
        "scriptthing": [
            "templates/*.py",
            "templates/*.sh", 
            "templates/*.js",
            "templates/*.jinja2",
            "config/*.toml",
            "resources/*.sh",
            "resources/*.js",
            "resources/internal_repo/**/*",
            "resources/starter_repo/**/*",
            "output/*.py"
        ]
    },
    include_package_data=True,
    zip_safe=False
)
