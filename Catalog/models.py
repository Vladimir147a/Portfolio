from django.db import models
from django.db import models
from django.core.validators import EmailValidator

class UserSubmission(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(
        verbose_name="Почта",
        validators=[EmailValidator(message="Введите корректный email адрес")]
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    data_agreement = models.BooleanField(
        verbose_name="Подтверждаю использование данных",
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"