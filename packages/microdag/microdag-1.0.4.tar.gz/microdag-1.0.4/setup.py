"""
MicroDAG - Ultra-lightweight DAG blockchain for IoT and micropayments
"""
from setuptools import setup, find_packages
import os

# Read README for long description
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Ultra-lightweight DAG blockchain optimized for IoT devices and micropayments"

setup(
    name="microdag",
    version="1.0.4",
    author="MicroDAG Team", 
    author_email="team@microdag.org",
    description="Ultra-lightweight DAG blockchain optimized for IoT devices and micropayments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microdag/microdag",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Security :: Cryptography",
        "Topic :: Office/Business :: Financial",
    ],
    keywords="blockchain dag iot micropayments lightweight distributed cryptocurrency",
    python_requires=">=3.8",
    install_requires=[
        # Minimal dependencies - use Python built-ins where possible
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0", 
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
        "full": [
            # Optional dependencies for enhanced features
            "aiohttp>=3.8.0",
            "cryptography>=3.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "microdag=microdag:main",
        ],
    },
    include_package_data=True,
    package_data={
        "microdag": ["*.md", "docs/*.html"],
    },
    zip_safe=False,
    project_urls={
        "Bug Reports": "https://github.com/microdag/microdag/issues",
        "Source": "https://github.com/microdag/microdag",
        "Documentation": "https://microdag.org/docs",
        "Homepage": "https://microdag.org",
    },
)
