from setuptools import setup, find_packages

setup(
    name="RatingsandReviewLibrary",          # The name of your library
    version="1.0.0",                         # Version of the library
    description="A library for managing ratings and feedback for repair and maintenance instructions.",
    author="GokulGirishKumar",                      # Your name
    author_email="gokulgkumar561@gmail.com",  # Your email (optional)     # URL to your project's repository (optional)
    packages=find_packages(),                # Automatically find all packages
    include_package_data=True,               # Include non-Python files, if any
    python_requires=">=3.6",                 # Minimum Python version
    install_requires=[],                     # Add dependencies if required
)
