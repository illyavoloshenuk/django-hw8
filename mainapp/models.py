
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "Новое"),
        ("in_progress", "В процессе"),
        ("waiting", "Ожидание"),
        ("blocked", "Заблокировано"),
        ("done", "Готово"),
    ]

    title = models.CharField(max_length=255, unique=True, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание задачи")
    categories = models.ManyToManyField(
        Category,
        related_name="tasks",
        blank=True,
        verbose_name="Категории",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус",
    )
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Крайний срок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class SubTask(models.Model):
    STATUS_CHOICES = [
        ("new", "Новое"),
        ("in_progress", "В процессе"),
        ("waiting", "Ожидание"),
        ("blocked", "Заблокировано"),
        ("done", "Готово"),
    ]

    title = models.CharField(max_length=255, verbose_name="Название подзадачи")
    description = models.TextField(blank=True, verbose_name="Описание подзадачи")
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="subtasks",
        verbose_name="Основная задача",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус",
    )
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Крайний срок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        verbose_name = "Подзадача"
        verbose_name_plural = "Подзадачи"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title