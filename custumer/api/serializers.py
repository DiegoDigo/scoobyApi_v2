from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.db import IntegrityError, transaction
from custumer.models import Profile, User, Pet
from validators.validSerializers import RelationModelSerializer


class UserSerializer(RelationModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class CreateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False, is_relation=True)
    pet = PetSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        try:
            pets = validated_data.pop('pet')
            instance = Profile.objects.create(**validated_data)
            for pet in pets:
                new_pet, created = Pet.objects.get_or_create(animal=pet['animal'])
                instance.pet.add(new_pet)
            return instance
        except IntegrityError:
            raise APIException(detail='Perfil ja existe para esse usuario !', code=400)
        except Exception:
            raise APIException(detail='outro erro!', code=400)


class UpdateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False, is_relation=True)
    pet = PetSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def update(self, instance, validated_data):
        pet_data = validated_data.pop('pet')
        instance = super(UpdateProfileSerializer, self).update(instance, validated_data)
        for pet in pet_data:
            pet_qs = Pet.objects.filter(animal__iexact=pet['animal'], namepet__iexact=pet['namepet'])
            if pet_qs.exists():
                _pet = pet_qs.first()
            else:
                _pet = Pet.objects.create(**pet_data)
            instance.pet.add(_pet)
        return instance
