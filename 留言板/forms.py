from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class Messageform(FlaskForm):
    user_name = StringField(u'昵称',validators=[DataRequired()])
    content = TextAreaField(u'留言',validators=[DataRequired()])
    submit = SubmitField(u'提交')