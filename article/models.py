from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Muellif")  #eger user silinerse onun butun melumatlari silinsin
    title = models.CharField(max_length=15)
    director = models.CharField(max_length=15)
    description = models.TextField(max_length=100, verbose_name="Tesvir")  #ad vere bilirik alias kimi
    created_date = models.DateTimeField(auto_now_add=True) #yuklendiyi anin zamanini avtomatik qeyd etsin

    def __str__(self):
        return self.title 