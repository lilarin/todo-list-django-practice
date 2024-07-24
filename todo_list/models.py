from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    description = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag, blank=True
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return (
            f"{self.description} (completed: {self.is_completed})"
            f"Created at: {self.description}"
            f"Deadline: {self.deadline}"
        )
