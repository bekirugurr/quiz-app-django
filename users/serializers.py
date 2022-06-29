from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer




class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        # validators=[validate_password],
        style={
            'input_type' :'password'
        }
    )

    #! custom password validation
    def validate_password(self, value):
        num_num = 0
        char_num = 0
        for i in value: 
            if i in '0123456789':
                num_num += 1
            elif i in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                char_num += 1
        if len(value) < 8:
            raise serializers.ValidationError("Password must have at least 8 char") 
        elif value == value.upper():
            raise serializers.ValidationError("Password must have lower char") 
        elif value == value.lower():
            raise serializers.ValidationError("Password must have upper char") 
        elif char_num == 0:
            raise serializers.ValidationError("Password must have number char") 
        elif num_num == 0:
            raise serializers.ValidationError("Password must have special char") 
        return value

    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style={
            'input_type' :'password'
        }
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        )
    
    def validate(self, attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError(
                {'password' : 'Password fileds do not match'}
            )
        return attr

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user



#! login olduğunda token ile birlikte user bilgilerinin dönmesi için aşağıya CustomTokenSerializers yazdım
# TokenSerializers olarak CustomTokenSerializers i kabul etmesi için settings>base.py da REST_AUTH_SERIALIZERS = {} içine 'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer' yazdım

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):  
        fields =(
            'key',
            'user'
        )



