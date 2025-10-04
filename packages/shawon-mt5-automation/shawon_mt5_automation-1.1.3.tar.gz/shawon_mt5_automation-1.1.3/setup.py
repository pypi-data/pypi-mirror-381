# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shawon_mt5_automation",
    version="1.1.3",
    author="Mahmudul Haque Shawon", # আপনার নাম
    author_email="haquemahmudul600@gmail.com", # আপনার ইমেইল
    description="A Flask webhook server to automate MetaTrader 5 trading based on TradingView signals with configurable settings and API key authentication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mt5-webhook-trader", # আপনার GitHub রিপোজিটরি URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.7',
    install_requires=[
        "Flask>=2.0.0",
        "MetaTrader5>=5.0.0",
    ],

)