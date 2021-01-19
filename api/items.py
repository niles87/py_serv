from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from api.auth import login_required
from api.db import get_db

bp = Blueprint('items', __name__)


@bp.route('/')
def index():
    db = get_db()
    items = db.execute(
        'SELECT id, name, price, description, stock'
        ' FROM item'
    ).fetchall()
    return render_template('items/index.html', items=items)


def get_item(id):
    item = get_db().execute(
        'SELECT id, name, price, description, stock'
        ' FROM item WHERE id = ?',
        (id,)
    ).fetchone()

    if item is None:
        abort(404, f"Item id {id} doesn't exist")
    return item


@bp.route('/<int:id>/item', methods=('GET', 'POST'))
def update(id):
    item = get_item(id)

    if request.method == 'POST':
        stock = request.form['stock']
        amount = request.form['amount']
        error = None
        if amount == 0:
            error = 'Amount is needed'

        if error is not None:
            flash(error)
        else:
            remaining_stock = stock - amount
            db = get_db()
            db.execute(
                'UPDATE item SET stock = ?'
                ' WHERE id = ?',
                (remaining_stock, id)
            )
            db.commit()
            return redirect(url_for('items.index'))

    return render_template('items/item.html', item=item)
