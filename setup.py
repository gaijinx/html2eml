from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='html2eml',
    version='0.0.1',
    description='html2eml is a simple package for converting HTML text to EML format (MIME RFC 822)',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    author='Konrad Gadzina',
    author_email='konradgadzina@gmail.com',
    keywords=['EML', 'HTML', 'Email'],
    url='https://github.com/gaijinx/html2eml',
    download_url='https://pypi.org/project/html2eml/'
)


if __name__ == '__main__':
    setup(**setup_args)
