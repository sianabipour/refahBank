from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _
from django.conf import settings




class Company(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='companies')
    name = models.CharField(max_length=150, verbose_name="نام سازمان")
    subs = models.ManyToManyField("main.Company", blank=True, verbose_name="زیر مجموعه ها")
    description = models.TextField(verbose_name="توضیحات")
    content = HTMLField(null=True, blank=True)
    image = models.ImageField(verbose_name="تصویر", upload_to='company')
    founder = models.CharField(verbose_name="مدیر عامل", max_length=150, null=True, blank=True)
    phone = models.CharField(verbose_name="شماره تماس", max_length=150, null=True, blank=True)
    link = models.URLField(_("لینک سایت"), max_length=200,null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "سازمان"
        verbose_name_plural = 'سازمان ها'

class HomePage(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    footer_text = models.TextField(verbose_name="متن فوتر")
    logo = models.ImageField(upload_to='homepage', verbose_name="تصویر")
    phone = models.CharField(verbose_name="شماره تماس", max_length=50)
    address = models.TextField(verbose_name="آدرس")
    email = models.EmailField(verbose_name="ایمیل", max_length=254)
    twitter = models.URLField(verbose_name="توییتر", max_length=200)
    instagram = models.URLField(verbose_name="اینستاگرام", max_length=200)
    linkedin = models.URLField(verbose_name="لینکدین", max_length=200)
    google_map = models.TextField(verbose_name="گوگل مپ",null=True)
    home_content = HTMLField(verbose_name="محتوای صفحه اصلی",null=True)

    class Meta:
        verbose_name = "صفحه اصلی"
        verbose_name_plural = "صفحه اصلی"

    def save(self, *args, **kwargs):
        if not self.pk and HomePage.objects.exists():
            raise ValueError("فقط یک صفحه متوانید بسازید.")
        super(HomePage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    start_date = models.CharField(verbose_name="تاریخ تاسیس", max_length=50)
    image = models.ImageField(upload_to='aboutpage', verbose_name="تصویر")
    content = HTMLField(verbose_name="محتوای صفحه ",null=True)
    founder = models.CharField(verbose_name="مدیر عامل", max_length=150, null=True, blank=True)
    phone = models.CharField(verbose_name="شماره تماس", max_length=150, null=True, blank=True)
    link = models.URLField(_("لینک سایت"), max_length=200,null=True, blank=True)

    class Meta:
        verbose_name = "صفحه درباره‌ما"
        verbose_name_plural = "صفحه درباره‌ما"

    def save(self, *args, **kwargs):
        if not self.pk and AboutPage.objects.exists():
            raise ValueError("فقط یک صفحه متوانید بسازید.")
        super(AboutPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Slider(models.Model):
    name = models.CharField(verbose_name="متن", max_length=150)
    subtext = HTMLField(_("سابتکست"))
    image = models.ImageField(verbose_name="عکس", upload_to="slider")
    link = models.URLField(verbose_name='لینک', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنر‌ها"


class Message(models.Model):
    name = models.CharField(verbose_name='نام', max_length=150)
    subject = models.CharField(verbose_name='موضوع', max_length=150)
    email =  models.EmailField(verbose_name='ایمیل', max_length=254)
    message =  models.TextField(verbose_name='پیام')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"
        
class Report(models.Model):
    
    company = models.ForeignKey("Company", verbose_name=_("شرکت"), on_delete=models.CASCADE,related_name='subcompany')
    annual_profit = models.CharField(_("سود سالیانه"), max_length=50)
    budget = models.CharField(_("بودجه اولیه"), max_length=50)
    staff_number = models.CharField(_("تعداد پرسنل"), max_length=50)
    current_expense = models.CharField(_("هزینه جاری"), max_length=50)
    year_analysis = models.TextField(_("عملکرد امسال"))
    expected_budget = models.CharField(_("پیش بینی بودجه"), max_length=50)
    

    class Meta:
        verbose_name = _("گزارش")
        verbose_name_plural = _("گزارشها")

    def __str__(self):
        return self.company.name