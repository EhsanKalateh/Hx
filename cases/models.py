from django.conf import settings
from django.db import models
from django.urls import reverse


class Case(models.Model):
    verified=models.BooleanField(default=False, )
    slug = models.SlugField(
        ("Link"),
        max_length=40,
        null=False,
        blank=False,
        unique=True,
        help_text="لینک مورد علاقه برای کیس خود را وارد کنید. تلاش کنید لینکتان گویا و دقیق باشد، پس از این توانایی تغییر آن را نخواهید داشت.",
    )

    rts={"ریه":"ریه",
         "هماتولوژی و انکولوژی":"هماتولوژی و انکولوژی",
         "روماتولوژی":"روماتولوژی",
         "غدد":"غدد",
         "گوارش":"گوارش",
         "نفرولوژی":"نفرولوژی",
         "جنرال":"جنرال",
         "قلب":"قلب",
         "پوست":"پوست",
         "اطفال":"اطفال",
         "زنان":"زنان",
         "اعصاب":"اعصاب",
         "روان":"روان",
         "ENT":"ENT",
         "عفونی":"عفونی",
         "چشم":"چشم",
         "مسمومین":"مسمومین",}
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    cat=models.CharField(
        ("دسته:"),
        max_length=100,
        choices=rts,
        null=True,
        blank=True,

    )


    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="خلاصه‌ای برای نشان دادن در صفحۀ اصلی که می‌تواند از عنوان طولانی‌تر باشد (تا دویست حرف)."
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    pretext = models.TextField(null=True, blank=True,help_text="اگر خواستید، می‌توانید مقدمه‌ای دربارۀ شرح‌حال خود بنویسید.")

    gender = models.CharField(
        max_length=5,
        choices={"آقا": "Male", "خانم": "Female", "دیگر": "Other"},
        null=False,
        blank=False,
        default="O",
    )
    location = models.CharField(
        max_length=10,
        choices={
            "مطب": "مطب",
            "درمانگاه": "درمانگاه",
            "اورژانس": "اورژانس",
            "بخش": "بخش",
        },
        null=False,
        blank=False,
        default="ROT",
    )
    job = models.CharField(max_length=20, null=True, blank=True)
    dwelling = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=False, blank=False, default=40)
    marriage = models.CharField(
        max_length=15,
        choices={
            "متاهل": "متاهل",
            "مجرد": "مجرد",
            "همسر فوت شده": "همسر فوت شده",
            "جداشده": "جداشده",
        },
        null=True,
        blank=True,
    )
    # date_of_admission=models.DateField(null=True, blank=True)
    doctor = models.CharField(max_length=20, null=True, blank=True)
    source = models.CharField(max_length=10, null=True, blank=True)
    reliability = models.CharField(
        max_length=1,
        choices={
            "5": "5/5",
            "4": "4/5",
            "3": "3/5",
            "2": "2/5",
            "1": "1/5",
        },
        null=True,
        blank=True,
    )
    setting = models.CharField(max_length=30, null=True, blank=True)

    PR = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True, default=70
    )
    BP_S = models.DecimalField(
        ("Systolic BP"),
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        default=120,
    )
    BP_D = models.DecimalField(
        ("Diastolic BP"),
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        default=80,
    )
    RR = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True, default=18
    )
    SPO2_O = models.DecimalField(
        ("SPO2 With Oxygen"),
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
    )
    SPO2_N = models.DecimalField(
        ("SPO2 Without Oxygen"),
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
    )
    Temp = models.DecimalField(
        ("Temperature"),
        max_digits=2,
        decimal_places=0,
        null=True,
        blank=True,
        default=37,
    )

    cc = models.CharField(
        ("Cheif Complaint"), max_length=100, null=False, blank=False, default=""
    )
    pi = models.TextField(("Present Illness"), null=False, blank=False, default="")
    pmh = models.TextField(
        ("Past Medical History"),
        null=True,
        blank=True,
    )
    drg = models.TextField(
        ("Drugs and Addictions"),
        null=True,
        blank=True,
    )
    sh = models.TextField(
        ("Social History"),
        null=True,
        blank=True,
    )
    fh = models.TextField(
        ("Family History"),
        null=True,
        blank=True,
    )
    alg = models.CharField(
        ("Allergies"),
        max_length=100,
        null=True,
        blank=True,
    )
    phe = models.TextField(
        ("Physical Examinations and Review of Systems"),
        null=True,
        blank=True,
    )
    dat = models.TextField(
        ("Paraclinic Data"),
        null=True,
        blank=True,
        help_text=("Including Previous Lab Data and Images and ECGs."),
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
    pdx = models.CharField(
        ("Primary Dx"),
        max_length=100,
        null=True,
        blank=True,
    )
    act = models.TextField(
        ("Actions"),
        null=True,
        blank=True,
    )



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("case_detail", args=[str(self.slug)])


class FollowUp(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    date = models.DecimalField(
        ("Days After Admission:"),
        max_digits=2,
        decimal_places=0,
        null=False,
        blank=False,
        default=0,
    )
    text = models.TextField(("Note"), null=False, blank=False, help_text="توجه کنید که نت‌ها در حال حاضر، قابل تغییر یا پاکسازی نیستند.")
    
    def get_absolute_url(self):
        return reverse("cases_list",kwargs={"slug": self.slug})
    
    def __str__(self):
        return (str(self.date)+" "+self.text[:32])

class Comment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    verified=models.BooleanField(default=True)
    comment = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment[:32]

