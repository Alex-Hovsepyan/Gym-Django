from django.db import models
import uuid
# Create your models here.

class Header(models.Model):

    img = models.ImageField('Logo', upload_to='images')
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)
    path5 = models.CharField('Path 5', max_length=50)
    path6 = models.CharField('Path 6', max_length=50)
    sub_path1 = models.CharField('Sub Path 1', max_length=50)
    sub_path2 = models.CharField('Sub Path 2', max_length=50)
    sub_path3 = models.CharField('Sub Path 3', max_length=50)
    social1 = models.CharField('Social 1', max_length=50)
    social2 = models.CharField('Social 2', max_length=50)
    social3 = models.CharField('Social 3', max_length=50)
    social4 = models.CharField('Social 4', max_length=50)
    social_link1 = models.URLField('Social Link 1')
    social_link2 = models.URLField('Social Link 2')
    social_link3 = models.URLField('Social Link 3')
    social_link4 = models.URLField('Social Link 4')

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class FooterContent(models.Model):

    icon = models.CharField('Icon', max_length=50)
    info = models.CharField('Info', max_length=200)

    class Meta:

        verbose_name = 'Footer Content'
        verbose_name_plural = 'Footer Content'

    def __str__(self) -> str:
        return self.info
    
class Footer(models.Model):

    text = models.TextField('Text')
    social1 = models.CharField('Social 1', max_length=50)
    social2 = models.CharField('Social 2', max_length=50)
    social3 = models.CharField('Social 3', max_length=50)
    social4 = models.CharField('Social 4', max_length=50)
    social5 = models.CharField('Social 5', max_length=50)
    social_link1 = models.URLField('Social Link 1')
    social_link2 = models.URLField('Social Link 2')
    social_link3 = models.URLField('Social Link 3')
    social_link4 = models.URLField('Social Link 4')
    social_link5 = models.URLField('Social Link 5')
    title1 = models.CharField('Title 1', max_length=40)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    subtitle3 = models.CharField('Subtitle 3', max_length=50)
    subtitle4 = models.CharField('Subtitle 4', max_length=50)
    title2 = models.CharField('Title 2', max_length=40)
    subtitle5 = models.CharField('Subtitle 5', max_length=50)
    subtitle6 = models.CharField('Subtitle 6', max_length=50)
    subtitle7 = models.CharField('Subtitle 7', max_length=50)
    subtitle8 = models.CharField('Subtitle 8', max_length=50)
    title3 = models.CharField('Title 3', max_length=40)
    info1 = models.TextField('Info 1')
    info2 = models.TextField('Info 2')
    copyright_text = models.TextField('Copyright')
        
    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class Homepage(models.Model):

    background = models.ImageField('Background', upload_to='images')
    subtitle = models.CharField('Subtitle', max_length=50)
    title1 = models.CharField('Title 1', max_length=50)
    colored_title = models.CharField('Colored Title', max_length=50)
    title2 = models.CharField('Title 2', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)

    class Meta:

        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepage'

    def __str__(self) -> str:
        return f'{self.title1} {self.colored_title} {self.title2}'
    
class Title(models.Model):

    colored_title1 = models.CharField('Colored Title 1', max_length=50)
    title1 = models.CharField('Title 1', max_length=50)
    colored_title2 = models.CharField('Colored Title 2', max_length=50)
    title2 = models.CharField('Title 2', max_length=50)
    colored_title3 = models.CharField('Colored Title 3', max_length=50)
    title3 = models.CharField('Title 3', max_length=50)
    colored_title4 = models.CharField('Colored Title 4', max_length=50)
    title4 = models.CharField('Title 4', max_length=50)
    colored_title5 = models.CharField('Colored Title 5', max_length=50)
    title5 = models.CharField('Title 5', max_length=50)
    colored_title6 = models.CharField('Colored Title 6', max_length=50)
    title6 = models.CharField('Title 6', max_length=50)
    colored_title7 = models.CharField('Colored Title 7', max_length=50)
    title7 = models.CharField('Title 7', max_length=50)
    colored_title8 = models.CharField('Colored Title 8', max_length=50)
    title8 = models.CharField('Title 8', max_length=50)
    colored_title9 = models.CharField('Colored Title 9', max_length=50)
    title9 = models.CharField('Title 9', max_length=50)

class Reason(models.Model):

    icon = models.CharField('Icon', max_length=50)
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title
    
class Offer(models.Model):

    img = models.ImageField('Image', upload_to='images')
    colored_title = models.CharField('Colored Title', max_length=50)
    title = models.CharField('Title', max_length=50)
    icon = models.CharField('Icon', max_length=50)

    def __str__(self) -> str:
        return self.title

class Appointment(models.Model):

    background = models.ImageField('Background', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    btn_name = models.CharField('Button Name', max_length=40)
    
    class Meta:

        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointment'

class Pricing(models.Model):

    title = models.CharField('Title', max_length=50)
    price = models.CharField('Price', max_length=20)
    subtitle = models.CharField('Subtitle', max_length=50)
    offer1 = models.CharField('Offer 1', max_length=50, blank=True)
    offer2 = models.CharField('Offer 2', max_length=50, blank=True)
    offer3 = models.CharField('Offer 3', max_length=50, blank=True)
    offer4 = models.CharField('Offer 4', max_length=50, blank=True)
    offer5 = models.CharField('Offer 5', max_length=50, blank=True)
    offer6 = models.CharField('Offer 6', max_length=50, blank=True)
    btn_name = models.CharField('Button Name', max_length=40)

    def __str__(self) -> str:
        return self.title
    
class HomeGallery(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    img1 = models.ImageField('Image 1', upload_to='images')
    title1 = models.CharField('Title 1', max_length=50)
    img2 = models.ImageField('Image 2', upload_to='images')
    title2 = models.CharField('Title 2', max_length=50)
    img3 = models.ImageField('Image 3', upload_to='images')
    title3 = models.CharField('Title 3', max_length=50)
    img4 = models.ImageField('Image 4', upload_to='images')
    title4 = models.CharField('Title 4', max_length=50)
    img5 = models.ImageField('Image 5', upload_to='images')
    title5 = models.CharField('Title 5', max_length=50)
    img6 = models.ImageField('Image 6', upload_to='images')
    title6 = models.CharField('Title 6', max_length=50)

    class Meta:

        verbose_name = 'Home Gallery'
        verbose_name_plural = 'Home Gallery'

class Aboutpage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)

    class Meta:

        verbose_name = 'Aboutpage'
        verbose_name_plural = 'Aboutpage'

class About(models.Model):

    img = models.ImageField('Image', upload_to='images')
    video_link = models.URLField('Video')
    text = models.TextField('Text')

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutFill(models.Model):

    title = models.CharField('Title', max_length=50)
    percent = models.IntegerField('Percent')

    class Meta:

        verbose_name = 'About Fill'
        verbose_name_plural = 'About Fill'

    def __str__(self) -> str:
        return self.title
    
class Testimonial(models.Model):

    img = models.ImageField('Image', upload_to='images')
    text = models.TextField('Text')
    name = models.CharField('Name', max_length=50)
    icon = models.TextField('Icon')

    def __str__(self) -> str:
        return self.name
    
class Servicespage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    
    class Meta:

        verbose_name = 'Servicespage'
        verbose_name_plural = 'Servicespage'
    
class Services(models.Model):

    trainer = models.ForeignKey('Team', on_delete=models.CASCADE)
    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)
    to_check = models.BooleanField('Check Position', blank=True)
    text2 = models.TextField('Text 2')
    slug = models.SlugField('Slug', unique=True, blank=True)

    class Meta:

        verbose_name = 'Services'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return self.title
    
class Teampage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    
    class Meta:

        verbose_name = 'Teampage'
        verbose_name_plural = 'Teampage'

class Team(models.Model):

    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=50)
    profession = models.CharField('Profession', max_length=50)
    social1 = models.CharField('Social 1', max_length=50)
    social2 = models.CharField('Social 2', max_length=50)
    social3 = models.CharField('Social 3', max_length=50)
    social4 = models.CharField('Social 4', max_length=50)
    social5 = models.CharField('Social 5', max_length=50)
    social_link1 = models.URLField('Social Link 1')
    social_link2 = models.URLField('Social Link 2')
    social_link3 = models.URLField('Social Link 3')
    social_link4 = models.URLField('Social Link 4')
    social_link5 = models.URLField('Social Link 5')
    age = models.CharField('Age', max_length=10)
    weight = models.CharField('Weight', max_length=20)
    height = models.CharField('Height', max_length=20)
    occupation = models.CharField('Occupation', max_length=50)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')

    class Meta:

        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self) -> str:
        return self.name
    
class Contactpage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    
    class Meta:

        verbose_name = 'Contactpage'
        verbose_name_plural = 'Contactpage'
    
class Contact(models.Model):

    placeholder1 = models.CharField('Input Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Input Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Input Placeholder 3', max_length=50)
    placeholder4 = models.CharField('Input Placeholder 4', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
    google_map = models.TextField('Google Map Link')
    
    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class ContactPost(models.Model):

    user_name = models.CharField('Name', max_length=50)
    user_email = models.EmailField('Email')
    user_phone = models.CharField('Phone Number', max_length=30)
    user_message = models.TextField('Message')

    class Meta:

        verbose_name = 'Contact Post'
        verbose_name_plural = 'Contact Post'

    def __str__(self) -> str:
        return f'{self.user_name} --------------------------------------------- {self.user_email} --------------------------------------------- {self.user_phone}'
    
class Calculatorpage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    path3 = models.CharField('Path 3', max_length=30)
    
    class Meta:

        verbose_name = 'Calculatorpage'
        verbose_name_plural = 'Calculatorpage'

class CalculatorBMI(models.Model):

    title1 = models.CharField('Title 1', max_length=50)
    title2 = models.CharField('Title 2', max_length=50)
    text = models.TextField('Text')
    placeholder1 = models.CharField('Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Placeholder 2', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)

    class Meta:

        verbose_name = 'CalculatorBMI'
        verbose_name_plural = 'CalculatorBMI'

class BMI_STATUS(models.Model):

    bmi = models.CharField('Bmi', max_length=30)
    status = models.CharField('Status', max_length=50)
    
    class Meta:

        verbose_name = 'BMI_STATUS'
        verbose_name_plural = 'BMI_STATUS'

    def __str__(self) -> str:
        return f'{self.bmi} ================== {self.status}'
    
class Gallerypage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    path3 = models.CharField('Path 3', max_length=30)
    
    class Meta:

        verbose_name = 'Gallerypage'
        verbose_name_plural = 'Gallerypage'

class Gallery(models.Model):

    img1 = models.ImageField('Image 1', upload_to='images')
    title1 = models.CharField('Title 1', max_length=50)
    img2 = models.ImageField('Image 2', upload_to='images')
    title2 = models.CharField('Title 2', max_length=50)
    img3 = models.ImageField('Image 3', upload_to='images')
    title3 = models.CharField('Title 3', max_length=50)
    img4 = models.ImageField('Image 4', upload_to='images')
    title4 = models.CharField('Title 4', max_length=50)
    img5 = models.ImageField('Image 5', upload_to='images')
    title5 = models.CharField('Title 5', max_length=50)
    img6 = models.ImageField('Image 6', upload_to='images')
    title6 = models.CharField('Title 6', max_length=50)
    img7 = models.ImageField('Image 7', upload_to='images')
    title7 = models.CharField('Title 7', max_length=50)
    img8 = models.ImageField('Image 8', upload_to='images')
    title8 = models.CharField('Title 8', max_length=50)
    img9 = models.ImageField('Image 9', upload_to='images')
    title9 = models.CharField('Title 9', max_length=50)
        
    class Meta:

        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

class Classespage(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    background = models.ImageField('Backgorund', upload_to='images')
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    path3 = models.CharField('Path 3', max_length=30)
    title2 = models.CharField('Title 2', max_length=50)
    info1 = models.CharField('Info 1', max_length=25)
    info2 = models.CharField('Info 2', max_length=25)
    info3 = models.CharField('Info 3', max_length=25)
    info4 = models.CharField('Info 4', max_length=25)

    class Meta:

        verbose_name = 'Classespage'
        verbose_name_plural = 'Classespage'