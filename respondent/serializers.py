from respondent.models import Question, Answer
from rest_framework import serializers

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "text", "created_at"]
        read_only_fields = ['id', 'created_at']

    def validate_text(self, text: str):
        if not text:
            raise serializers.ValidationError("Text can't be empty")
        return text


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question_id", "user_id", "text", "created_at"]
        read_only_fields = ['id', 'created_at']

    def validate_text(self, text: str):
        if not text:
            raise serializers.ValidationError("Text can't be empty")
        return text


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question_id", "user_id", "text", "created_at"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ["id", "text", "created_at", "answers"]
        read_only_fields = fields