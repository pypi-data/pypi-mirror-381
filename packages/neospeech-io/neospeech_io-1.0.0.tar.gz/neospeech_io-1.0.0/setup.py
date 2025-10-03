from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="neospeech-io",
    version="1.0.0",
    author="NeoSpeech",
    description="Official Python SDK for the NeoSpeech Text-to-Speech API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neospeech/neospeech-python",
    project_urls={
        "Documentation": "https://docs.neospeech.io",
        "Source": "https://github.com/neospeech/neospeech-python",
        "Bug Reports": "https://github.com/neospeech/neospeech-python/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords="neospeech text-to-speech tts speech-synthesis voice audio ai sdk",
)
