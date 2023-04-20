from rest_framework import serializers
from .models import User, Food


class UsersSerializer(serializers.ModelSerializer):
      
    foods = serializers.HyperlinkedRelatedField(
        view_name='food_details',
        many=True,
        read_only=True
      )
      
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password','weight', 'foods']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class FoodSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # user = UsersSerializer()
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     lookup_field='id',
    #     read_only=True
    # )

    class Meta:
        model = Food
        fields = ('id','user','user_id', 'food_name', 'image_url','calories')

