from setuptools import setup
import django_mqtt

setup(name='django-mqtt',
      description='Send data to mqtt server as publisher.',
      version='.'.join(map(str, django_mqtt.__version__)),
      author=django_mqtt.__author__,
      author_email=django_mqtt.__contact__,
      url=django_mqtt.__homepage__,
      license=django_mqtt.__license__,
      keywords='django mqtt',
      classifiers=[
          "Framework :: Django",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
      ],
      packages=[
          'django_mqtt',
          'django_mqtt.mosquitto',
          'django_mqtt.mosquitto.auth_plugin',
          'django_mqtt.publisher',
          'django_mqtt.publisher.management',
          'django_mqtt.publisher.management.commands'
      ])
