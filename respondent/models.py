from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"Question id {self.pk}: {self.text[:10]}"


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user_id = models.CharField(max_length=64)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['created_at']

    def __str__(self) -> str:
        return f"Answer id {self.pk}: {self.text[:10]}"