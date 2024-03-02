from django.forms import ModelForm, CheckboxSelectMultiple, CharField


from .models import (Case, 
                    #  FollowUp, 
                     Comment)


class CaseUpdateForm(ModelForm):
    # cat=CharField(widget=CheckboxSelectMultiple())
    class Meta:
        model = Case
        exclude = ("slug","verified","author")

# class FollowUpForm(ModelForm):
#     class Meta:
#         model = FollowUp
#         fields = ('date',"text",)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)

# class CaseCreateForm(ModelForm):
#     class Meta:
#         model = Case
#         exclude = ("author",)
    