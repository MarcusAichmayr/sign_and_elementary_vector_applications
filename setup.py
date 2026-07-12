from setuptools import setup


# Get information from separate files (README)
def readfile(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


setup(
    name="sign_and_elementary_vector_applications",
    version="1.1",
    description="Applications of sign vectors and elementary vectors",
    long_description=readfile("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/MarcusAichmayr/sign_and_elementary_vector_applications",
    author="Marcus S. Aichmayr",
    author_email="aichmayr@mathematik.uni-kassel.de",
    license="GPL-3.0-or-later",
    packages=[
        "applications",
    ],
    install_requires=["elementary_vectors>=2.4", "sign_vectors>=1.4", "certlin>=1.4", "signcrn>=2.5"],
)
