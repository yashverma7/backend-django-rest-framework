#to start with the web api, proceed with a way of serializing
#and deserializing the snippet instances into
#representations like json 
#by declaring the serializers similar to django forms

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



#Our SnippetSerializer class is replicating a lot of information that's also contained 
# in the Snippet model. It would be nice if we could keep our code a bit more concise.

#In the same way that Django provides both Form classes and ModelForm classes, 
# REST framework includes both Serializer classes, and ModelSerializer classes.

#Let's look at refactoring our serializer using the ModelSerializer class. Open the 
# file snippets/serializers.py again, and replace the SnippetSerializer class with the 
# following.


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

#ModelSerializer classes don't do anything particularly magical,
 #they are simply a shortcut for creating serializer classes:

#An automatically determined set of fields.
#Simple default implementations for the create() and update() methods.



#defines the fields that get serialized/deserialised
'''class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')'''
#create and update methods define how the fully fledged instances are created and modified 
#serilaizer class is similar to django form class including 



'''def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
    return Snippet.objects.create(**validated_data)

def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
    instance.title = validated_data.get('title', instance.title)
    instance.code = validated_data.get('code', instance.code)
    instance.linenos = validated_data.get('linenos', instance.linenos)
    instance.language = validated_data.get('language', instance.language)
    instance.style = validated_data.get('style', instance.style)
    instance.save()
    return instance
'''

#The field flags can also control how the serializer
#should be displayed in certain circumstances, such as when rendering to HTML. 
# The {'base_template': 'textarea.html'} flag above is equivalent to using 
# widget=widgets.Textarea on a Django Form class. This is particularly useful 
# for controlling how the browsable API should be displayed, We can actually 
# also save ourselves some time by using the ModelSerializer class, 
