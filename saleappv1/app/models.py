from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        #c1 = Category(name='Mobile')
        #c2 = Category(name='Tablet')

        #db.session.add(c1)
        #db.session.add(c2)
        #db.session.commit()

        p1 = Product(name='iPhone 14', price=20000, category_id=1, image=r"C:\Users\admin\Desktop\IT2021-SaleApp01\download.jpg")
        p2 = Product(name='Galaxy S25', price=20000, category_id=1, image=r"C:\Users\admin\Desktop\IT2021-SaleApp01\download.jpg")
        p3 = Product(name='Galaxy Tab S10', price=20000, category_id=2, image=r"C:\Users\admin\Desktop\IT2021-SaleApp01\download.jpg")
        p4 = Product(name='Ipad Pro M2', price=20000, category_id=2, image=r"C:\Users\admin\Desktop\IT2021-SaleApp01\download.jpg")
        p5 = Product(name='Ipad Pro M1', price=20000, category_id=2, image=r"C:\Users\admin\Desktop\IT2021-SaleApp01\download.jpg")
        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()

        #db.create_all()