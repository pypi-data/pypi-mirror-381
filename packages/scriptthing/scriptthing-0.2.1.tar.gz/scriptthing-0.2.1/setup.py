from setuptools import setup, find_packages

setup(
    name="scriptthing",
    version="0.2.1",
    description="A tool for managing and organizing scripts across multiple repositories with template support",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "click",
        "jinja2",
        "pyyaml",
        "toml",
        "humanfriendly>=10.0",
        "pydantic>=2.0.0"
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0"
        ],
        "mcp": [
            "fastmcp",
            "shellmcp"
        ]
    },
    entry_points={
        "console_scripts": [
            "scriptthing = scriptthing.cli:cli"
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
