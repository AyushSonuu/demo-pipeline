from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author= "ayush",
      author_email="sonuayush55@gmail.com",
      packages=find_packages(),
      install_require = ["numpy","pandas" ,"matplotlib","flask"]
      )