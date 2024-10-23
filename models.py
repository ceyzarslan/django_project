from datetime import datetime

from sqlalchemy import Integer, Column, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

from sqlalchemy import Column, Integer, String, \
    Float  # SQLAlchemy'den veritabanı sütunları için gerekli türleri import ediyoruz (Integer, String, Float).
from sqlalchemy.ext.declarative import \
    declarative_base  # SQLAlchemy'den declarative_base fonksiyonunu import ediyoruz. Bu, veritabanı modellerini oluşturmak için temel bir sınıf sağlar.

Base = declarative_base()  # Base adında bir temel sınıf oluşturuyoruz. Bu sınıf, diğer modellerin (tablo yapılarının) türetileceği bir temel sınıf olarak kullanılır.
class Category(Base):
    __tablename__ = "category"
    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String(25),nullable=False,unique=True)
    products = relationship('Product',back_populates='category')

class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    products = relationship('Product', back_populates='brand')

class Product(
    Base):  # 'Product' adında bir veritabanı modeli (sınıf) oluşturuyoruz. Bu sınıf, veritabanında bir tabloyu temsil edecek.
    __tablename__ = "products"  # Tablonun adı olarak 'products' belirleniyor. Bu tablo, veritabanında "products" adını alacak.

    id = Column(Integer, autoincrement=True, primary_key=True)  # 'id' adında bir sütun tanımlıyoruz. Bu sütun Integer türünde olacak, her yeni ürün eklemede otomatik olarak artacak ve birincil anahtar olacak.
    title = Column(String(160),nullable=False)  # 'title' sütunu String türünde olacak ve en fazla 160 karakter uzunluğunda bir başlık içerecek. Boş bırakılamaz (nullable=False).
    description = Column(String,nullable=True)  # 'description' sütunu String türünde olacak ve ürün açıklaması içerecek. Bu alan boş bırakılabilir (nullable=True).
    price = Column(Float, nullable=False,default=0)  # 'price' sütunu Float türünde olacak ve ürün fiyatını temsil edecek. Boş bırakılamaz ve varsayılan olarak 0 atanır (nullable=False, default=0).
    discountPercentage = Column(Float, nullable=False,default=0)  # 'discountPercentage' sütunu Float türünde olacak, indirim oranını temsil edecek. Varsayılan olarak 0 atanır ve boş bırakılamaz.
    stock = Column(Integer, nullable=False,default=0)  # 'stock' sütunu Integer türünde olacak ve ürün stok miktarını temsil edecek. Varsayılan olarak 0 atanır ve boş bırakılamaz.
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship('Category',back_populates='products')
    brand_id = Column(Integer,ForeignKey('brand.id'))
    brand = relationship('Brand',back_populates='products')
    tags = relationship('Tag',back_populates='product')

class Tag(Base):  # 'Tag' adında bir veritabanı modeli (sınıf) oluşturuyoruz. Bu sınıf, veritabanında bir tabloyu temsil edecek.
    __tablename__ = "tags"  # Bu sınıf, veritabanında "tags" adında bir tabloyu temsil ediyor.

    id = Column(Integer, autoincrement=True, primary_key=True)  # 'id' adında bir sütun tanımlıyoruz. Bu sütun Integer türünde olacak, her yeni etiket eklemede otomatik olarak artacak ve birincil anahtar olacak.
    name = Column(String(25), nullable=False,unique=True)  # 'name' sütunu String türünde olacak ve en fazla 25 karakter uzunluğunda bir isim içerecek. Bu isim boş bırakılamaz (nullable=False) ve benzersiz olmalı (unique=True).
    product_id = Column(Integer,ForeignKey('product.id'))
    product = relationship('Product',back_populates='tags')

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, autoincrement=True, primary_key=True)
    comment = Column(String(25), nullable=False,unique=True)
    rating = Column(Integer,nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    product_id = Column(Integer,ForeignKey('product.id'))
    product = relationship('Product',back_populates='tags')
