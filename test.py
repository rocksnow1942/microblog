########
# SET UP YOUR FLASK APP HERE
########

from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory

class Family(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(500), info={'label': 'Familyname', 'validators': DataRequired()})

class Member(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(500), info={'label': 'Member', 'validators': DataRequired()})


BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class MemberForm(ModelForm):

    class Meta:
        model = Machine


class MemberEditForm(MemberForm):
    pass

class MainForm(ModelForm):

    add_member = SubmitField('+ Member')
    members = ModelFieldList(FormField(MemberForm))
    class Meta:
        model = Family



@app.route('/form')
def main_form():

    family = Family()
    form = MainForm(obj=family)

    if form.add_member.data:
        getattr(form,'members').append_entry()
        return render_template('form.html', form=form)

    if form.validate_on_submit():
        form.populate_obj(family)
        db.session.add(order)
        db.session.commit()

    return render_template('form.html', form=form)


@app.route('/process_add_member', methods=['POST'])
def add_member():
    form = MainForm()

    getattr(form,'members').append_entry()

    return render_template('members.html', form=form)
