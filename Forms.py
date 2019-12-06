from wtforms import Form, StringField, RadioField, validators

class CreateUserForm(Form):
 firstName = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
 lastName = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
 email = StringField("Email", [validators.Length(min=10, max=100), validators.DataRequired()])
 membership = RadioField('Membership', choices=[('M', 'Member'), ('P', 'Premium Member')], default='M')
 password = StringField('Password', [validators.Length(min=5, max=150), validators.DataRequired()])
