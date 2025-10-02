from setuptools import setup, find_packages

setup(
    name="python_snake_game",
    version="0.10.1",
    description="A Windows snake game project.It is a private project but you can use it if you trust me.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ramimK0bir",
    author_email="kobirbiddut81@gmail.com" ,  
    packages=find_packages() ,
    python_requires='>=3.7',

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
)
