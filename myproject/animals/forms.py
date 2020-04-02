from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField



class AddForm(FlaskForm):

    animalID = IntegerField('ID of Animal:')
    startWeight = FloatField('Start Weight of Animal: ')
    w1 = FloatField('Weight at first weigh in: ')
    w2 = FloatField('Weight at second weigh in: ')
    w3 = FloatField('Weight at third weigh in: ')
    w4 = FloatField('Weight at fourth weigh in: ')
    finalWeight = FloatField('Weight at Final Weigh In')
    motherID = IntegerField('ID of Mother')
    fatherID = IntegerField('ID of Father')
    diet = StringField('Diet Type of Animal')
    ch4_daily_mean = FloatField('Daily Mean of Methane Produced')
    feedEfficiency = FloatField('Feed Efficiancy of Animal')
    waterEfficieny = FloatField('Water Efficiancy of Animal')
    submit = SubmitField('Add Animal')

class DelForm(FlaskForm):

    animalID = IntegerField('Id Number of Animal to Remove:')
    submit = SubmitField('Remove Animal')