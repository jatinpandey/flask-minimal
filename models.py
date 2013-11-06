
from mongoengine import *

connect('tumblelog') #Database

class User(Document):
    email = StringField(required=True)
    last_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    password = StringField(max_length=100) 

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=100)

class Post(Document):
    title = StringField(max_length=100, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

class TextPost(Post):
    content = StringField()

class ImagePost():
    image_path = StringField()

class LinkPost():
    link_url = StringField()

