from django.contrib.auth.forms import UserCreationForm

class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
