from setuptools import setup, find_packages

setup(
    name="hogwarts-terminal",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "magic=spells.spell:main"
        ]
    },
    author="Ranjana M Suvarna",
    description="Harry Potter-themed Magical Linux/Windows terminal commands",
    # Safely read README.md; fallback to empty string when missing so 'pip' doesn't fail
    long_description=(open("README.md", encoding="utf-8").read() if __import__('os').path.exists("README.md") else ""),
    long_description_content_type="text/markdown",
)
