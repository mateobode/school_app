# class Submission(models.Model):
#     grade = models.PositiveIntegerField(validators=[MinValueValidator(4), MaxValueValidator(10)])
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     feedback = models.CharField(max_length=250)
#     deadline_date = models.DateField()
