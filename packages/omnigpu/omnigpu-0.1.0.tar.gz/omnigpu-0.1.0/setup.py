from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="omnigpu",
    version="0.1.0",
    author="Badel L. Mbanga",
    author_email="badel@klogW.ai",
    description="Run PyTorch CUDA code on Apple Silicon GPUs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/badelmbanga/omnigpu",
    project_urls={
        "Bug Tracker": "https://github.com/badelmbanga/omnigpu/issues",
        "Documentation": "https://omnigpu.readthedocs.io",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS :: MacOS X",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
        ],
    },
)