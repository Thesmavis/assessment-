from django.db import models

# Create your models here.
class Eventdetails(models.Model):
    Event=models.CharField(max_length=50, blank=True, null=True) 
class Jobrequisition(models.Model):
    Jobreq=models.CharField(max_length=50, blank=True, null=True) 
class Persona(models.Model):
    Personal=models.CharField(max_length=50, blank=True, null=True) 
class Screeningmode(models.Model):
    Screeningmod=models.CharField(max_length=50, blank=True, null=True) 
class Gender(models.Model):
    Gender=models.CharField(max_length=50, blank=True, null=True) 
class Maritalstatus(models.Model):
    Maritalstatu=models.CharField(max_length=50, blank=True, null=True) 
class Employeedirectory(models.Model):
    Employeedirector=models.CharField(max_length=50, blank=True, null=True) 
class City(models.Model):
    city=models.CharField(max_length=50, blank=True, null=True) 
class Experiencelevel(models.Model):
    Experienceleve=models.CharField(max_length=50, blank=True, null=True) 
class Educationlevel(models.Model):
    Educationlevel=models.CharField(max_length=50, blank=True, null=True) 
class Educationqualification(models.Model):
    Educationqualification=models.CharField(max_length=50, blank=True, null=True) 
class Educationspecialization(models.Model):
    Educationspecialization=models.CharField(max_length=50, blank=True, null=True) 
class Sourcetype(models.Model):
    Sourcetype=models.CharField(max_length=50, blank=True, null=True) 
class Source(models.Model):
    Source=models.CharField(max_length=50, blank=True, null=True) 
class Reasonforchange(models.Model):
    Reasonforchange=models.CharField(max_length=50, blank=True, null=True)    

class Candidatedirectory(models.Model):
     event = models.ForeignKey( Eventdetails, on_delete=models.DO_NOTHING, db_column="event", blank=True, null=True )
     job_position = models.ForeignKey( Jobrequisition, on_delete=models.DO_NOTHING, db_column="job_position", blank=True, null=True, ) 
     recruiter_alert = models.CharField(max_length=50, blank=True, null=True) 
     first_name = models.CharField(max_length=255, blank=True, null=True) 
     last_name = models.CharField(max_length=255, blank=True, null=True) 
     email = models.CharField(max_length=50, blank=True, null=True) 
     persona = models.ForeignKey( Persona, on_delete=models.DO_NOTHING, db_column="persona", blank=True, null=True, default=1, )
     role = models.IntegerField(blank=True, null=True) 
     screening_mode = models.ForeignKey( Screeningmode, on_delete=models.DO_NOTHING, db_column="screening_mode", blank=True, null=True, )
     dob = models.DateField(blank=True, null=True) 
     gender = models.ForeignKey( Gender, on_delete=models.DO_NOTHING, db_column="gender", blank=True, null=True ) 
     marital_status = models.ForeignKey( Maritalstatus, on_delete=models.DO_NOTHING, db_column="marital_status", blank=True, null=True, ) 
     contact_no_primary = models.DecimalField( max_digits=10, decimal_places=0, blank=True, null=True ) 
     contact_no_alternate = models.DecimalField( max_digits=10, decimal_places=0, blank=True, null=True ) 
     referred_by = models.ForeignKey( Employeedirectory, on_delete=models.DO_NOTHING, db_column="referred_by", blank=True, null=True, ) 
     referred_by_other = models.CharField(max_length=250, blank=True, null=True) 
     address_line = models.CharField(max_length=255, blank=True, null=True) 
     city = models.ForeignKey( City, on_delete=models.DO_NOTHING, db_column="city", blank=True, null=True ) 
     pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True) 
     experience_level = models.ForeignKey( Experiencelevel, on_delete=models.DO_NOTHING, db_column="experience_level", blank=True, null=True, ) 
     education_level = models.ForeignKey( Educationlevel, on_delete=models.DO_NOTHING, db_column="education_level", blank=True, null=True, ) 
     education_qualification = models.ForeignKey( Educationqualification,on_delete=models.DO_NOTHING, db_column="education_qualification", blank=True, null=True, ) 
     education_specialization = models.ForeignKey( Educationspecialization, on_delete=models.DO_NOTHING, db_column="education_specialization", blank=True, null=True, ) 
     education_specialization_other = models.TextField( blank=True, null=True ) # This field type is a guess. 
     education_institution = models.ForeignKey( Source, on_delete=models.DO_NOTHING, db_column="education_institution", blank=True, null=True, ) 
     education_institution_other = models.TextField( blank=True, null=True ) # This field type is a guess. 
     source = models.ForeignKey( Source, on_delete=models.DO_NOTHING, db_column="source", blank=True, null=True, related_name="source_for_candidate_details", ) 
     source_type = models.ForeignKey( Sourcetype, on_delete=models.DO_NOTHING, db_column="source_type", blank=True, null=True ) 
     years_of_experience = models.DecimalField( max_digits=4, decimal_places=2, blank=True, null=True ) 
     current_employer = models.CharField(max_length=100, blank=True, null=True) 
     current_designation = models.TextField( blank=True, null=True ) # This field type is a guess. 
     current_monthly_salary = models.IntegerField( blank=True, null=True ) 
     expected_monthly_salary = models.IntegerField( blank=True, null=True ) 
     notice_period = models.CharField(max_length=50, blank=True, null=True) 
     reason_for_change = models.ForeignKey( "Reasonforchange", on_delete=models.DO_NOTHING, db_column="reason_for_change",blank=True, null=True, ) 
     photo_path = models.TextField(blank=True, null=True) # This field type is a guess. 
     resume_path = models.TextField(blank=True, null=True) # This field type is a guess. 
     login_time = models.DateTimeField(blank=True, null=True) 
     logout_time = models.DateTimeField(blank=True, null=True) 
     ip_address = models.CharField(max_length=15, blank=True, null=True) 
     geo_location = models.CharField(max_length=50, blank=True, null=True) 
     created_date = models.DateTimeField(blank=True, null=True) 
     created_by = models.IntegerField(blank=True, null=True) 
     modified_date = models.DateTimeField(blank=True, null=True)
     modified_by = models.IntegerField(blank=True, null=True) 
     status = models.IntegerField(default=1) 
     class Meta:
        managed = False 
        db_table = "CandidateDirectory" 
        constraints = [ models.UniqueConstraint(fields=['first_name', 'last_name'], name='full_name') ]
