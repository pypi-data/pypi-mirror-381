from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_latest_version():
    try:
        with open("CHANGELOG.md", "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("## ["):
                    return line.split("[")[1].split("]")[0]
    except FileNotFoundError:
        return "0.0.1"  # fallback version
    return "0.0.1"  # fallback if no version found

try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    requirements = []

setup(
    name="thetemani-common-utils",
    version=get_latest_version(),
    author="Omer Hadad",
    description="A collection of common utility functions and scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['common_utils', 'common_utils.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    project_urls={
        "Homepage": "https://github.com/Omer-hadad-s-Projects/common",
        "Bug Reports": "https://github.com/Omer-hadad-s-Projects/common/issues",
        "Source": "https://github.com/Omer-hadad-s-Projects/common",
    },
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "common_utils": ["shell_scripts/*.sh"],
    },
)