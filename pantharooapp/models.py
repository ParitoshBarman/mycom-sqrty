from django.db import models

# Create your models here.
class AllowDevice(models.Model):
    slNo = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=122)
    ApplicationName = models.CharField(max_length=122, null=True)
    EmployeeID = models.IntegerField()
    Email = models.CharField(max_length=122)
    DesktopID = models.CharField(max_length=122)
    IP_Address = models.CharField(max_length=100) 
    MainDateTime = models.DateField(auto_now=True)
    def __str__(self):
        return self.FullName

class FileHistory(models.Model):
    slNo = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=122)
    ApplicationName = models.CharField(max_length=122, null=True)
    EmployeeID = models.IntegerField()
    Email = models.CharField(max_length=122)
    DesktopID = models.CharField(max_length=122)
    IP_Address = models.CharField(max_length=100) 
    fileNameData = models.CharField(max_length=300)
    MainDateTime = models.DateField(auto_now=True)
    def __str__(self):
        return self.FullName

class AvailableFiles(models.Model):
    slNo = models.AutoField(primary_key=True)
    FileCreaterFullName = models.CharField(max_length=122)
    FileCreaterApplicationName = models.CharField(max_length=122, null=True)
    FileCreaterEmployeeID = models.IntegerField()
    FileCreaterEmail = models.CharField(max_length=122)
    FileCreaterDesktopID = models.CharField(max_length=122)
    FileCreaterIP_Address = models.CharField(max_length=100) 
    fileNameData = models.CharField(max_length=300)
    MainDateTime = models.DateField(auto_now=True)
    def __str__(self):
        return self.FullName

class History(models.Model):
    slNo = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=122)
    ApplicationName = models.CharField(max_length=122, null=True)
    EmployeeID = models.IntegerField()
    Email = models.CharField(max_length=122)
    DesktopID = models.CharField(max_length=122)
    IP_Address = models.CharField(max_length=100) 
    UserDateTime = models.CharField(max_length=100)
    ServerDateTime = models.CharField(max_length=50)
    MainDateTime = models.DateField(auto_now=True)
    def __str__(self):
        return self.FullName
    

class NotAllow(models.Model):
    slNo = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=122)
    ApplicationName = models.CharField(max_length=122, null=True)
    EmployeeID = models.IntegerField()
    Email = models.CharField(max_length=122)
    DesktopID = models.CharField(max_length=122)
    IP_Address = models.CharField(max_length=100) 
    UserDateTime = models.CharField(max_length=100)
    ServerDateTime = models.CharField(max_length=50)
    MainDateTime = models.DateField(auto_now=True)
    def __str__(self):
        return self.FullName
    


class FileHistoryNotAllowSPAM(models.Model):
    slNo = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=122)
    ApplicationName = models.CharField(max_length=122, null=True)
    EmployeeID = models.IntegerField()
    Email = models.CharField(max_length=122)
    DesktopID = models.CharField(max_length=122)
    IP_Address = models.CharField(max_length=100) 
    fileNameData = models.CharField(max_length=300)
    MainDateTime = models.DateField(auto_now=True)
    def __str__(self):
        return self.FullName
