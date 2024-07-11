from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Rittik Raj',
    author_email='rittikrajchauhan123@gmail.com',
    install_requires=["google-generativeai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)