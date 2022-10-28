from django.utils.functional import lazy

from rest_framework import serializers

from baserow.core.auth_provider.models import AuthProviderModel
from baserow.core.registries import auth_provider_type_registry


class CreateAuthProviderSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=lazy(auth_provider_type_registry.get_types, list)(),
        required=True,
    )

    class Meta:
        model = AuthProviderModel
        fields = ("domain", "type")


class UpdateAuthProviderSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=lazy(auth_provider_type_registry.get_types, list)(), required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    class Meta:
        model = AuthProviderModel
        fields = ("domain", "type")
        extra_kwargs = {
            "domain": {"required": False},
        }
