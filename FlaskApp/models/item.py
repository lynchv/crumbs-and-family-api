from FlaskApp import db

class Item(db.Model):
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), default='', nullable=False)
    category = db.Column(db.String(50), default='', nullable=False)
    description = db.Column(db.String(2048), default='', nullable=False)
    image = db.Column(db.Text, nullable=True)
    price = db.Column(db.Integer,default=0, nullable=False)


    def __repr__(self):
        return '<Item {} - {}>'.format(self.item_id, self.name)

    
    def to_json(self):
        json = {}
        json["item_id"] = self.item_id
        json["name"] = self.name
        json["category"] = self.category
        json["description"] = self.description
        json["price"] = self.price

        if isinstance(self.image, bytes):
            json["image"] = self.image.decode('utf-8')
        elif isinstance(self.image, str):
            json["image"] = self.image
        else:
            json["image"] = ""
            
        return json