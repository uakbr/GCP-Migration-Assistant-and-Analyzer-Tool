from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='gcp-migration-assistant-analyzer-tool',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to assist organizations in migrating to Google Cloud Platform',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your-github-username/gcp-migration-assistant-analyzer-tool',
    project_urls={
        'Bug Tracker': 'https://github.com/your-github-username/gcp-migration-assistant-analyzer-tool/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.8',
    install_requires=[
        'google-cloud-storage==1.42.0',
        'google-cloud-bigquery==2.30.1',
        'google-cloud-compute==0.4.0',
        'google-cloud-container==2.7.1',
        'google-cloud-database-migration==1.1.1',
        'google-resumable-media==1.3.3',
        'docker==5.0.0',
        'kubernetes==18.20.0',
        'google-auth==2.3.3',
        'requests==2.26.0',
        'numpy==1.21.4',
        'pandas==1.3.4',
        'prometheus-client==0.11.0',
        'tenacity==8.0.1',
        'mkdocs==1.2.3',
        'click==8.0.3',
        'PyYAML==6.0',
        'Flask==2.0.2',
        'Jinja2==3.0.3',
    ],
    entry_points={
        'console_scripts': [
            'gcp-migration-assistant = main:main',
        ],
    },
    include_package_data=True,
    keywords='gcp migration, cloud migration, google cloud platform, migration tool',
    license='MIT',
    zip_safe=False
)
