from django import forms
from .models import Property,Feedback

class add_prop_form(forms.ModelForm):        
    price=forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'type':"number",'class':"form-control",'id':"price",'placeholder':"Price in Lakhs"}))
    class Meta:
        postedbychoice=(
            ('Owner','Owner'),
            ('Builder','Builder'),
            ('Dealer','Dealer')
        )
        roomchoice=(
            ('BHK','BHK'),
            ('RK','RK')
        )
        model=Property
        fields=('posted_by','under_construction','rera','rooms','room_type','area','ready_to_move','resale','location','loc_long','loc_lat','price')
        widgets={
            'posted_by':forms.Select(attrs={'type':"text",'class':"form-control",'id':"pby",'placeholder':"Posted By"},choices=postedbychoice),
            'rooms':forms.NumberInput(attrs={'type':"number",'class':"form-control",'id':"rm",'placeholder':"Number of Rooms"}),
            'room_type':forms.Select(attrs={'type':"text",'class':"form-control",'id':"rmtype",'placeholder':"Type of Room Layout"},choices=roomchoice),
            'area':forms.NumberInput(attrs={'type':"number",'class':"form-control",'id':"area",'placeholder':"Area in Sqft"}),
            'location':forms.TextInput(attrs={'type':"text",'class':"form-control",'id':"loc",'placeholder':"Location"}),
            'loc_long':forms.NumberInput(attrs={'type':"number",'class':"form-control",'id':"loclong",'placeholder':"Longitude"}),
            'loc_lat':forms.NumberInput(attrs={'type':"number",'class':"form-control",'id':"loclat",'placeholder':"Latitude"})
        }

class feedbackform(forms.ModelForm):
    date=forms.CharField(required=False)
    class Meta:
        model=Feedback
        fields=('name','email','subject','message','date')
        widgets={
            'name':forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Name",'aria-label':"Name",'aria-describedby':"name"}),
            'email':forms.EmailInput(attrs={'type':"email",'class':"form-control",'placeholder':"ABC@example.com",'aria-label':"Subject",'aria-describedby':"email"}),
            'subject':forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Subject",'aria-label':"Subject",'aria-describedby':"subject"}),
            'message':forms.Textarea(attrs={'class':"form-control",'aria-label':"With textarea"}),
        }