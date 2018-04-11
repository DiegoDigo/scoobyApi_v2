from rest_framework import serializers
from custumer.models import Profile, User, Pet
from validators.validSerializers import RelationModelSerializer


class UserSerializer(RelationModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class CreateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False, is_relation=True)
    pet = PerSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        pets = validated_data.pop('pet')
        instance = Profile.objects.create(**validated_data)
        for pet in pets:
            new_pet, created = Pet.objects.get_or_create(animal=pet['animal'])
            instance.pet.add(new_pet)
        return instance
