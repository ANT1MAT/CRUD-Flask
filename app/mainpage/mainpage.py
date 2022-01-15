from flask import Blueprint, render_template, request, redirect, url_for

from models.wishlist import Wishlist, db


mainpage_blueprint = Blueprint('mainpage', __name__,
                           template_folder='templates/html')


@mainpage_blueprint.route('/', methods=['get'])
def mainpage():
    return render_template('mainpage.html')


@mainpage_blueprint.route('/', methods=['post'])
def additem():
    try:
        add = Wishlist(name=request.form['name'], price=request.form['price'],
                       url=request.form['url'], disc=request.form['disc'])
        db.session.add(add)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return render_template('mainpage.html')



@mainpage_blueprint.route('/mylist', methods=['get'])
def mywishlist():
    list=Wishlist.query.all()
    return render_template('wishlist.html', list=list)


@mainpage_blueprint.route('/mylist', methods=['post'])
def deleteitem():
    id_item = request.form['item']
    db.engine.execute("delete from list where id={}".format(id_item))
    return redirect(url_for('mainpage.mywishlist'))

