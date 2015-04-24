#*-* encoding: utf-8 *-*

from flask_wtf import Form
from flask_wtf.html5 import (
	IntegerField,
	TelField,
	EmailField,
	DateField
)
from wtforms import (
	TextField,
	TextAreaField,
	SelectMultipleField
)

from wtforms.validators import Required, Length  

class SlamForm(Form):
	name = TextField("Dame tu Nombre", validators=[Required()])
	edad = IntegerField("Cuantos agnos tienes?")
	fecha = DateField("Que dia es hoy?")
	email = EmailField("Cual es tu email")
	historia = TextAreaField("Cuentame algo")


class SlamForm2(SlamForm):
	likes = SelectMultipleField(
		'Dime que te gusta',
		choices=[
			('skeletor', 'Skeletor'),
			('man_at_arms', 'Man at Arms'),
			('she_ra', 'She-ra'),
			('orko', 'Orko')
		]
	)
