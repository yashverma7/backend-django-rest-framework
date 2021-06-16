# backend-django-rest-framework

# creating a serializer class

The first thing we need to get started 
on our Web API is to provide a way of s
erializing and deserializing the snippet instances
 into representations such as json. We can do this by declaring 
serializers that work very similar to Django's
 forms. 
Create a file in the snippets directory named 
serializers.py and add the following.

# Using ModelSerializers
Our SnippetSerializer class is replicating a
 lot of information that's also contained
 in the Snippet model. It would be nice if 
we could keep our code a bit more concise.

In the same way that Django provides
 both Form classes and ModelForm classes, 
REST framework includes both Serializer
 classes, and ModelSerializer classes
