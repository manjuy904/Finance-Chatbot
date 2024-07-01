from setuptools import find_packages, setup

setup(
    name="financebot",
    version='0.0.1',
    author="Dr. Manju",
    author_email="manjuy904@gmail.com",
    packages=find_packages(), #this will help to automatically find the constructor file that is __init__ file
    install_requires = ["langchain", "langchain-openai", "langchain-astradb", "datasets", "pypdf", "python-dotenv", "flask"]    
)