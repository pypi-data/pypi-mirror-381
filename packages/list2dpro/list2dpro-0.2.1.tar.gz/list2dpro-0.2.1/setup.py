from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='list2dpro',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[],  # 目前无外部依赖
    author='FriskYan',
    author_email='476227421@qq.com',
    description='A comprehensive 2D list manipulation library for Python with four specialized classes: List2DEdit (basic editing), List2DGame (game development), List2DMath (mathematical operations), and List2DData (data processing).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',  # 无项目链接
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)