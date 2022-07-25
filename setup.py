from distutils.core import setup

setup(
  name = 'nautapy',        
  packages = ['nautapy'],   
  version = '1.0',      
  license='GNU General Public License v3',      
  description = 'Librería sencilla para acceder al Portal Nauta',   
  author = 'Samuel',                
  author_email = 'samuel.falconpc@gmail.com',      
  url = 'https://github.com/SamuelDev00/nautapy',  
  download_url = 'https://github.com/SamuelDev00/nautapy/archive/refs/tags/v1.0.tar.gz',    
  keywords = ['Portal', 'Nauta', 'Etecsa'],   
  install_requires=[
          'requests~=2.27.1',
          'beautifulsoup4~=4.10.0',
          'lxml==4.7.1',
      ],
  classifiers=[
        "Topic :: Internet",
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Operating System :: Unix"
    ],
)
