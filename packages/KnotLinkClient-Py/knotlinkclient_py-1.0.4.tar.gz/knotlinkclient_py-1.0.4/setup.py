from setuptools import setup, find_packages

setup(
    name='KnotLinkClient_Py',  # 包名
    version='1.0.4',  # 版本号
    packages=find_packages(),  # 自动发现包和模块
    description='A Py-based client for KnotLink communication',  # 简短描述
    long_description=open('README.md', encoding='utf-8').read(),  # 从 README.md 读取长描述
    long_description_content_type='text/markdown',  # 长描述的格式
    author='HXH',  # 作者
    author_email='1768224274@qq.com',  # 作者邮箱
    install_requires=[  # 依赖包
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)