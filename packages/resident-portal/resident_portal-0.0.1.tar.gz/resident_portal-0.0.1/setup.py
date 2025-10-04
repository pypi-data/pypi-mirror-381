from setuptools import find_packages, setup  # noqa: D100

with open("README.md", encoding="utf8") as fh:
    long_desc = fh.read()

setup(
    name="resident_portal",
    version="0.0.1",
    description="API wrapper for ResidentPortal",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Gavyn Stanley",
    packages=find_packages(where="."),
    license="MIT",
    install_requires=["aiohttp", "loguru", "pyjwt"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
