import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_desciption = f.read()

setuptools.setup(
    name="bot_daddy_bot",
    version="2.0.1",
    author="drforse",
    author_email="george.lifeslice@gmail.com",
    description="Telegram bot with many functions",
    long_description=long_desciption,
    long_description_content_type="text/markdown",
    url="https://github.com/drforse/BotDaddy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)