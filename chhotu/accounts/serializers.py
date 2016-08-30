from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

from .models import Profile


class AuthMixin(object):
    """
    authenticate user credentials
    """
    messages_text = {
        "invalid": _("The email address and/or password are not correct."),
        "disabled": _("This account is not activated."),
    }

    def user_credentials(self, attrs):
        """
        Provides the credentials required to authenticate the user for login.
        """
        credentials = {}
        credentials["email"] = attrs["email"].lower()
        credentials["password"] = attrs["password"]
        return credentials

    def validate_user_credentials(self, data):
        user = authenticate(**self.user_credentials(data))
        if user:
            if user.is_active:
                self.instance = user
            else:
                raise serializers.ValidationError(
                    self.messages_text["disabled"])
        else:
            raise serializers.ValidationError(self.messages_text["invalid"])
        return user


class RegisterSerializer(serializers.ModelSerializer, AuthMixin):

    """ Profile Serializer for User Signup """

    def validate_email(self, value):
        try:
            Profile.objects.get(email=value.lower())
        except Profile.DoesNotExist:
            return value.lower()
        raise serializers.ValidationError(
            _('User already registered with this Email ID.'))

    def create(self, validated_data):
        """
        Create a new User instance.
        """
        validated_data['username'] = validated_data.get('email')
        self.instance = Profile.objects.create_user(**validated_data)
        return self.validate_user_credentials(validated_data)

    class Meta:
        model = Profile
        fields = (
            'name', 'email', 'contact_no', 'password',
        )


class LoginSerializer(serializers.Serializer, AuthMixin):

    """
    User serializer with custom fields for authentication
    """
    email = serializers.CharField(
        max_length=Profile._meta.get_field('email').max_length)
    password = serializers.CharField(max_length=Profile._meta.get_field('email').max_length)

    def validate(self, data):
        """ validate login credentials """
        self.validate_user_credentials(data)
        return data


class LogOutSerializer(serializers.Serializer):
    pass
