import setuptools

PACKAGES = []

setuptools.setup(
   name='fetch_coins_list',
   version='1.0',
   url='aqsone.com',
   author='Theo Freville',
   author_email='theo.freville@aqsone.com',
   setup_requires=PACKAGES,
   install_requires=PACKAGES,
   packages=setuptools.find_packages(),
   include_package_data=True
)