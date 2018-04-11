from rest_framework import serializers
from rest_framework.fields import empty


class RelationModelSerializer(serializers.ModelSerializer):
    def __init__(self, instance=None, data=empty, **kwargs):
        self.is_relation = kwargs.pop('is_relation', False)
        super(RelationModelSerializer, self).__init__(instance, data, **kwargs)

    def validate_empty_values(self, data):
        if self.is_relation:
            model = getattr(self.Meta, 'model')
            model_pk = model._meta.pk.name

            if not isinstance(data, dict):
                error_message = self.default_error_messages['invalid'].format(datatype=type(data).__name__)
                raise serializers.ValidationError(error_message)

            if not model_pk in data:
                raise serializers.ValidationError({model_pk: model_pk + ' is required'})

            try:
                instance = model.objects.get(pk=data[model_pk])
                return True, instance
            except:
                raise serializers.ValidationError({model_pk: model_pk + ' is not valid'})

        return super(RelationModelSerializer, self).validate_empty_values(data)
