from flask import Flask, render_template
from flask import redirect
from flask import url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from setting3 import Config
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# 实例化管理器对象（）

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    name2 = db.Column(db.String(64), unique=True)
    at_book = db.relationship('Book',backref='author')

    # def __repr__(self):
    #     return "Author:%s" % self.name


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # at_book = db.Column(db.Integer,db.ForeignKey=('author.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    # def __repr__(self):
    #     return "Book: %s" % self.name
# class Form(FlaskForm):
#     ator = StringField(validators=[DataRequired()])
#     book = StringField(validators=[DataRequired()])
#     submit = SubmitField("保存")
# @app.route('/',methods=['POST','GET'])
# def hello_world():
#     form = Form()
#     if form.validate_on_submit():
#         at = form.ator.data
#         bk = form.book.data
#         ators=Author(name=at)
#         db.session.add(ators)
#         db.session.commit()
#         books=Author(name=bk)
#         db.session.add(books)
#         db.session.commit()
#     ator = Author.query.all()
#     book = Book.query.all()
#     return render_template('flask_529.html', ator= ator, book=book,form=form)
#
# @app.route('/detele_author<int:id>')
# def del_author(id):
#     # print(id)
#     foo = Author.query.filter_by(id=id).first()
#     # book = Book.query.get()
#     # print(foo)
#     db.session.delete(foo)
#     db.session.commit()
#     return redirect(url_for('hello_world'))
# @app.route('/detele_book<int:id>')
# def del_book(id):
#     # print(id)
#     bok = Book.query.get(id)
#     print(bok)
#     # book = Book.query.get()
#     # print(foo)
#     db.session.delete(bok)
#     db.session.commit()
#     return redirect(url_for('hello_world'))

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au1 = Author(name='老王')
    # au2 = Author(name='老尹')
    # au3 = Author(name='老刘')
    # # 把数据提交给用户会话
    # db.session.add_all([au1, au2, au3])
    # # 提交会话
    # db.session.commit()
    # bk1 = Book(name='老王回忆录', author_id=au1.id)
    # bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    # bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    # bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    # bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # # 把数据提交给用户会话
    # db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # # 提交会话
    # db.session.commit()
    # app.run(port=9999)
    # migrate.run()
    manager.run()
