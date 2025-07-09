from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=200)

    #직종
    JOB_TYPE_CHOICES = [
        ('planning', '기획/전략'),
        ('development', 'IT/개발/데이터'),
        ('manufacturing', '생산/제조'),
        ('contents','콘텐츠/미디어'),
        ('marketing', '마케팅/홍보/MD'),
        ('customer_service', '고객상담/cs'),
        ('construction', '건축/시설관리'),
        ('finance', '금융/보험'),
        ('accounting', '회계/세무/재무'),
        ('logistics', '물류/운송'),
        ('healthcare', '의료/간호'),
        ('public', '공공/복지'),
        ('design', '디자인'),
        ('operation', '운영/서비스업'),
        ('education', '교육/강의'),
        ('hr', '인사/사무/총무'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    
    #지역
    REGION_CHOICES = [
        ('seoul', '서울'),
        ('gyeonggi', '경기/인천'),
        ('busan', '부산/울산/경남'),
        ('daegu', '대구/경북'),
        ('gwangju', '광주/전남/전북'),
        ('daejeon', '대전/충남/충북'),
        ('gangwon', '강원'),
        ('jeju', '제주'),
    ]
    region = models.CharField(max_length=20, choices=REGION_CHOICES)


    #재택가능 여부
    remote_available = models.BooleanField(default=False)

    #경력
    CAREER_TYPE_CHOICES = [
        ('new', '신입'),
        ('none', '없음'),
        ('exp', '경력'),
    ]

    career = models.CharField(max_length=10, choices=CAREER_TYPE_CHOICES)
    career_years = models.IntegerField(null=True, blank=True)

    #학력
    EDUCATION_CHOICES = [
        ('high_school', '고등학교 졸업'),
        ('associate_degree', '전문대학 졸업'),
        ('bachelor_degree', '학사 학위'),
        ('master_degree', '석사 학위'),
        ('doctorate', '박사 학위'),
    ]
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)

    #기업 규모
    COMPANY_SIZE_CHOICES = [
        ('small', '소기업'),
        ('medium', '중기업'),
        ('large', '대기업'),
        ('startup', '스타트업'),
        ('public', '공공기관'),
    ]
    company_size = models.CharField(max_length=20, choices=COMPANY_SIZE_CHOICES)

    company_logo = models.ImageField(verbose_name = "company_logo", null=True, blank=True)

    link = models.URLField(blank=True, null=True)
    
    company = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        from django.core.exceptions import ValidationError
        # 경력이 'exp'일 때만 career_years 입력 가능
        if self.career == 'exp':
            if self.career_years is None:
                raise ValidationError({'career_years': '경력이 있을 경우 경력 연차를 입력해야 합니다.'})
        else:
            if self.career_years not in (None, 0):
                raise ValidationError({'career_years': '경력이 없거나 신입일 경우 경력 연차를 입력할 수 없습니다.'})

