"""
Setup script for Nexus - Intelligent Agentic File Assistant
"""

from setuptools import setup
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="nexus-ai-agent",
    version="1.0.1",
    author="Chiheb Nabil",
    author_email="hi@remoteskills.io",
    description="Intelligent Agentic File Assistant powered by Claude",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Remote-Skills/nexus",
    py_modules=["agent", "cli", "tools", "tool_functions", "__main__"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "anthropic>=0.25.0",
        "python-dotenv>=1.0.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nexus=cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", ".env.example"],
    },
    keywords="ai agent claude anthropic file-operations automation agentic planning",
    project_urls={
        "Bug Reports": "https://github.com/Remote-Skills/nexus/issues",
        "Source": "https://github.com/Remote-Skills/nexus",
        "Documentation": "https://github.com/Remote-Skills/nexus#readme",
    },
)
