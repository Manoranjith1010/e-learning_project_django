"""
Models for integrity/authenticity verification
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class IntegrityCheck(models.Model):
    """
    Model for integrity and authenticity verification
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='integrity_checks')
    assessment_id = models.IntegerField()
    cheating_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    plagiarism_detected = models.BooleanField(default=False)
    ai_generated_probability = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[('clean', 'Clean'), ('suspicious', 'Suspicious'), ('flagged', 'Flagged')])
    report = models.TextField(blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'integrity_checks'
    
    def __str__(self):
        return f"Integrity Check - {self.student.username}"
