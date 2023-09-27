from flask import Blueprint, render_template, request, redirect, url_for
from . import models


bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')

    results = models.Fact.query.all()

    return render_template('facts/index.html', facts=results)


@bp.route('/new')
def new():
    return render_template('facts/new.html')


# bp = Blueprint('fact', __name__, url_prefix="/facts")

# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         submitter = request.form['submitter']
#         fact_text = request.form['fact']

#         new_fact = models.Fact(submitter=submitter, fact=fact_text)

#         models.db.session.add(new_fact)
#         models.db.session.commit()

#         return redirect(url_for('fact.index'))

#     results = models.Fact.query.all()


# @bp.route('/new')
# def new():
#     return render_template('facts/index.html')
