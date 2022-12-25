from setuptools import setup

package_name = 'test_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='c-gayan',
    maintainer_email='cgayan10@gmail.com',
    description='Testing ros pub sub with python',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = test_pubsub.publisher:main',
            'listner = test_pubsub.subscriber:main',
        ],
    },
)
