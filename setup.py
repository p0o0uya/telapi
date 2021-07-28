import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='telegapi',
    version='0.0',
    author='Pouya Jamali',
    author_email='pouyajamali@gmail.com',
    description='A wrapper for telegram bot API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/p0o0uya/telapi',
    project_urls = {
        "Bug Tracker": "https://github.com/p0o0uya/telapi/issues"
    },
    license='MIT',
    packages=['telapi'],
    install_requires=['requests', 'pandas'],
)
