from setuptools import setup, find_packages

setup(
    name="fabricconnector",
    version="0.0.1",
    author="Davista",
    author_email="support@powerbiconnector.nl",
    description="Python connector library for Microsoft Fabric notebooks (placeholder release)",
    long_description="""# FabricConnector

This is a placeholder release to claim the package name on PyPI.

The full production release is coming soon with:
- Connect to Exact Online, Twinfield and AFAS accounting systems
- Stream large datasets with automatic pagination
- Automatic Lakehouse merge operations
- Incremental refresh support

For more information, visit: https://www.powerbiconnector.nl

## License

Proprietary - Requires paid subscription
""",
    long_description_content_type="text/markdown",
    url="https://www.powerbiconnector.nl",
    license="Proprietary",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
