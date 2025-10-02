# setup.py
from setuptools import setup, find_packages

# README.md dosyasındaki uzun açıklamayı okuyun
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # --- TEMEL BİLGİLER ---
    name='viona', # BURASI ÖNEMLİ! Kullanıcılar pip install VIONA diyecek.
    version='0.1.0',
    description='Orvix Games Viona AI modeli için resmi Python API istemcisi.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Orvix Games',
    author_email='destek@orvixgames.com',
    url='https://viona.orvixgames.com', # Projenizin ana sayfası
    
    # --- PAKET İÇERİĞİ ---
    # setuptools'un viona klasöründeki tüm paketleri bulmasını sağlar.
    packages=find_packages(), 
    
    # --- BAĞIMLILIKLAR ---
    # Bu paket için gerekli olan kütüphaneler (requests API bağlantısı için gerekli)
    install_requires=[
        'requests>=2.25.1',
    ],
    
    # --- SINIFLANDIRICILAR (PyPI'da listelenmesi için) ---
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # veya kendi lisansınız
        "Operating System :: OS Independent",
    ],
    
    # Python 3.6 ve üzeri sürümleri destekler
    python_requires='>=3.6',
)