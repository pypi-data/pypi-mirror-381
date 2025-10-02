from setuptools import setup, find_packages


setup(
    name="screenshotbase",
    version="0.1.0",
    description="Python client for screenshotbase.com API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ScreenshotBase",
    author_email="support@screenshotbase.com",
    url="https://screenshotbase.com/docs/",
    packages=find_packages(exclude=("tests", "examples")),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
    ],
    license="MIT",
    license_files=("LICENSE",),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Documentation": "https://screenshotbase.com/docs/",
    },
    include_package_data=True,
)


