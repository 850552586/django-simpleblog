from django.db import models
from django.contrib import  admin
from django.urls import reverse
from django.utils.timezone import now


#---------------------------------用户---------------------------------------
class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 50,default='匿名')
    email = models.EmailField()
    created_time = models.CharField(max_length=50,default=now)
    comment_num = models.PositiveIntegerField(verbose_name='评论数', default=0)   #评论数
    avatar = models.ImageField(upload_to = 'media', default="media/default.png")  #用户头像

    def __str__(self):
        return self.username

    def comment(self):
        self.comment_num += 1
        self.save(update_fields=['comment_num'])

    def comment_del(self):
        self.comment_num -= 1
        self.save(update_fields=['comment_num'])

    class Meta:
        verbose_name = '用户'  # 指定后台显示模型名称
        verbose_name_plural = '用户'  # 指定后台显示模型复数名称
        db_table = "blog_user"  # 数据库表名

#---------------------------------文章评论---------------------------------------
class ArticleComment(models.Model):
    body = models.TextField()
    username = models.CharField(max_length=50)
    userimg = models.CharField(max_length=70)
    nickname = models.CharField(max_length=50,default="匿名")
    createtime = models.DateTimeField(verbose_name='创建时间', default=now)
    article = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    # 使对象在后台显示更友好
    def __str__(self):
        return self.article

    class Meta:
        ordering = ['-createtime']
        verbose_name = '评论'  # 指定后台显示模型名称
        verbose_name_plural = '评论列表'  # 指定后台显示模型复数名称
        db_table = "comment"  # 数据库表名

    list_display = ('article', 'body')

#---------------------------------博客文章标签---------------------------------------
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=64)    
# 使对象在后台显示更友好
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签名称'  # 指定后台显示模型名称
        verbose_name_plural = '标签列表'  # 指定后台显示模型复数名称
        db_table = "tag"  # 数据库表名

#---------------------------------博客文章分类---------------------------------------
class Category(models.Model):
    name = models.CharField(verbose_name='类别名称', max_length=64)

    class Meta:
        ordering = ['name']
        verbose_name = "类别名称"
        verbose_name_plural = '分类列表'
        db_table = "category"  # 数据库表名

    # 使对象在后台显示更友好
    def __str__(self):
        return self.name

#---------------------------------博客文章---------------------------------------
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    article_id = models.CharField(verbose_name='标号', max_length=100)
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', blank=True, null=True)
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    # 使对象在后台显示更友好
    def __str__(self):
        return self.title

    # 更新浏览量
    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 下一篇
    def next_article(self):  # id比当前id大，状态为已发布，发布时间不为空
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False).first()

    # 前一篇
    def prev_article(self):  # id比当前id小，状态为已发布，发布时间不为空
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).first()

    class Meta:
        ordering = ['-created_time']  # 按文章创建日期降序
        verbose_name = '文章'  # 指定后台显示模型名称
        verbose_name_plural = '文章列表'  # 指定后台显示模型复数名称
        db_table = 'article'  # 数据库表名
        get_latest_by = 'created_time'
