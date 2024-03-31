from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


REPO_NAME = "Movie-Recommendation-System"
AUTHOR_NAME = "Shimul-Baidya"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="1.0.0",
    author=AUTHOR_NAME,
    description="This is a simple Movie Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    author_email="shimul.cse31@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)