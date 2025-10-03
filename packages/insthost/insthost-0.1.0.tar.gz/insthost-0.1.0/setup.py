from setuptools import setup, find_packages

setup(
    name='insthost',
    version='0.1.0',
    author='sinesurge',
    author_email='sinesurgeproducts@gmail.com',
    description='JUCE-based audio host launcher',
    packages=find_packages(),  # finds the insthost package folder
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'insthost = insthost.__main__:main',  # CLI points to your main()
        ],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
