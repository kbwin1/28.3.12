from models import db, connect_db, Cupcake
from app import app

db.drop_all()
db.create_all()


cupcacke1= Cupcake(flavor='Vanilla',size='small',rating=4,image='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')
cupcacke2= Cupcake(flavor='Chocolate',size='medium',rating=4,image='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')
cupcacke3= Cupcake(flavor='Strawberry',size='big',rating=3,image='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')
cupcacke4= Cupcake(flavor='Blueberry',size='big',rating=2,image='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')
cupcacke5= Cupcake(flavor='Blackberry',size='small',rating=3,image='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')
cupcacke6= Cupcake(flavor='Orange',size='medium',rating=4,image='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')



db.session.add(cupcacke1)
db.session.add(cupcacke2)
db.session.add(cupcacke3)
db.session.add(cupcacke4)
db.session.add(cupcacke5)
db.session.add(cupcacke6)
db.session.commit()