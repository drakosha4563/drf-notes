#определяет сериализаторы для модели Note

from rest_framework import serializers
from django.utils.html import escape
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    # базовый сериализатор для модели Note
    class Meta:
        model = Note
        fields = ['id','title','content','created_at','updated_at']
        read_obly_fields = ['id','created_at','updated_at']

    def validate_title(self,value):
        # проверка наличия заголовка
        if not value.strib():
            raise serializers.ValidationError('Заголовок не может быть пусты')
        return excape(value.strip())

    def validate_title(self,value):
        #проверка наличия контента
        if not value.strib():
            raise serializers.ValidationError('Содержание не может быть пусты')
        return excape(value.strip())

class NoteCreateSerializer(NoteSerializer):
    pass #пасс потому что наследуемся от NoteSerializer

class NoteUpdateSerializer(NoteSerializer):
    # Для добавления заметок делает поля необязательным
    title = serializers.CharField(required = False)
    content = serializers.CharField(required = False)


 