from django.forms import ModelForm
from .models import Question, Choice

class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]
        
        
class CreateChoice(ModelForm):
    class Meta:
        model = Choice
        fields = ["question", "choice_text"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["question"].queryset = Question.objects.all()