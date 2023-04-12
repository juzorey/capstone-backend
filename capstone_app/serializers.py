from rest_framework import serializers
from .models import User

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    # food = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all()) haveto make it a key in the model for user

    class Meta:
       model = User
       fields = ('id', 'username', 'password', 'email', 'name', 'weight')


class Fooderializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    # performing_at = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('user', 'food_name', 'image_url')

