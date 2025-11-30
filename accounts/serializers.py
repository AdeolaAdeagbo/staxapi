from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label='Confirm Password'
    )
    
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'password', 'password2', 
                  'university', 'course_of_study', 'phone_number']
        extra_kwargs = {
            'username': {'required': True},
            'full_name': {'required': True},
        }
    
    def validate(self, attrs):
        """Check that passwords match"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs
    
    def validate_email(self, value):
        """Check if email already exists"""
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value.lower()
    
    def validate_username(self, value):
        """Check if username already exists"""
        if User.objects.filter(username=value.lower()).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value.lower()
    
    def create(self, validated_data):
        """Create new user"""
        # Remove password2 as it's not needed for user creation
        validated_data.pop('password2')
        
        # Create user
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            university=validated_data.get('university', ''),
            course_of_study=validated_data.get('course_of_study', ''),
            phone_number=validated_data.get('phone_number', '')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user details"""
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'full_name', 'university', 
                  'course_of_study', 'profile_image', 'points', 'role', 
                  'bio', 'phone_number', 'is_verified', 'created_at']
        read_only_fields = ['id', 'email', 'points', 'role', 'is_verified', 'created_at']


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user profile"""
    
    class Meta:
        model = User
        fields = ['full_name', 'university', 'course_of_study', 'bio', 
                  'phone_number', 'profile_image']
    
    def validate_profile_image(self, value):
        """Validate image file size (max 5MB)"""
        if value and value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Image file size cannot exceed 5MB.")
        return value


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for password change"""
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    new_password2 = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        """Check that new passwords match"""
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({
                "new_password": "New password fields didn't match."
            })
        return attrs
    
    def validate_old_password(self, value):
        """Check that old password is correct"""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value
    
    def save(self, **kwargs):
        """Set new password"""
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user