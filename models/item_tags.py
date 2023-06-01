from db import db

class ItemTags(db.Model):
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_ksy=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))