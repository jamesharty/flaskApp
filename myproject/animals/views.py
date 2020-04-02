from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Animal
from myproject.animals.forms import AddForm, DelForm



animals_blueprint = Blueprint('animals', __name__,
                                template_folder='templates/animals')


@animals_blueprint.route('/add',methods =['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        animalID = form.animalID.data
        startWeight = form.startWeight.data
        w1 = form.w1.data
        w2 = form.w2.data
        w3 = form.w3.data
        w4 = form.w4.data
        finalWeight = form.finalWeight.data
        motherID = form.motherID.data
        fatherID = form.fatherID.data
        diet = form.diet.data
        ch4_daily_mean = form.ch4_daily_mean.data
        feedEfficiency = form.feedEfficiency.data
        waterEfficieny = form.waterEfficieny.data



        # Add new Animal to database
        new_animal = Animal(animalID,startWeight,w1,w2,w3,w4,finalWeight,
                        motherID,fatherID,diet,ch4_daily_mean,feedEfficiency,waterEfficieny)
        db.session.add(new_animal)
        db.session.commit()

        return redirect(url_for('animals.list'))

    return render_template('add.html',form=form)


@animals_blueprint.route('/list')
def list():
    # Grab a list of animals from database.
    animals = Animal.query.all()
    return render_template('list.html', animals=animals)

#DELETE ANIMAL FROM DATABASE
@animals_blueprint.route('/delete',methods =['GET','POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        animalID = form.animalID.data
        animal = Animal.query.get(animalID)
        db.session.delete(animal)
        db.session.commit()

        return redirect(url_for('animals.list'))
    return render_template('delete.html',form=form)


@animals_blueprint.route('/graph/<input_data>')
def graph(input_data):
    

    return render_template('graph.html')


    

    

