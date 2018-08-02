from setuptools import setup

with open('README.md') as f:
  readme = f.read()

with open ('LICENSE') as f:
  license = f.read()

setup(
    name='mqtt',
    version='0.0.1',
    description='A quick test on building a Snap with a basic Python MQTT project',
    long_description=readme,
    license=license,
    author='Matti Parkkila',
    author_email="parkkila.matti@gmail.com",
    packages=['mqtt'],
    entry_points={
      'console_scripts': [
        'test-python-ping-mqtt=mqtt.ping:init'
      ]
    },
)
