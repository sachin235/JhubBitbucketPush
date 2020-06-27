import setuptools

setuptools.setup(
    name="JhubBitbucketPush",
    version='0.1.0',
    url="https://github.com/sachin235/JhubBitbucketPush",
    author="Sachin Singla",
    description="Jupyter extension to enable user push notebooks to a bitbucket repo",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'JhubBitbucketPush': ['static/*']},
)
