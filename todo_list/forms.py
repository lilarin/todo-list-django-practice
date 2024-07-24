from django import forms
from django.contrib.auth import get_user_model
from todo_list.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        ),
        required=True,
    )

    class Meta:
        model = Task
        fields = [
            "description",
            "deadline",
            "tags",
        ]
