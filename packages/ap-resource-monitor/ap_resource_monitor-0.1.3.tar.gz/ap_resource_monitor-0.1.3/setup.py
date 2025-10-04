from setuptools import setup, find_packages

setup(
    name="ap_resource_monitor",
    version="0.1.0",
    description="A Python library for analyzing and reporting AP resource monitoring logs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="AirowireAILabs",
    author_email="ailabs@airowire.com",
    url="https://github.com/AirowireAILabs/ap_resource_monitor",
    project_urls={
        "Source": "https://github.com/AirowireAILabs/ap_resource_monitor",
        "Tracker": "https://github.com/AirowireAILabs/ap_resource_monitor/issues",
        "Documentation": "https://github.com/AirowireAILabs/ap_resource_monitor#readme"
    },
    license="MIT",
    packages=find_packages(exclude=["tests", "examples"]),
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Monitoring"
    ],
    keywords="resource monitoring access point system health",
)
