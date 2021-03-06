# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# class Parent(models.Model):
#     name = models.CharField(max_length=40)
#     date = models.DateField(auto_now_add=True)

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    parent = TreeForeignKey('self', related_name='children', blank=True, null=True)

    class Meta:
        verbose_name = u'Категории'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=False)
    description = models.TextField()
    price = models.IntegerField()
    weight = models.IntegerField()
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = u'Продукты'
        verbose_name_plural = u'Продукты'

    def __unicode__(self):
        return self.name

    def url(self):
        return '/product/' + self.slug

    def get_image(self):
        return ProductImage.objects.filter(product=self)[0]


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product")
    product = models.ForeignKey(Product)

    class Meta:
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения продуктов'

    def __unicode__(self):
        return self.product.name + "-" + self.image.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'

    def __unicode__(self):
        return self.name




class ArticleImage(models.Model):
    url = models.ImageField(upload_to="article")
    article = models.ForeignKey(Article)

    class Meta:
        verbose_name = u'Фото статьи'
        verbose_name_plural = u'Фото статьи'

    def __unicode__(self):
        return self.name


class Page(models.Model):
    slug = models.SlugField(max_length=150, unique=False, blank=False)
    name = models.CharField(max_length=2000)
    page = models.TextField()

    class Meta:
        verbose_name = u'Страницы'
        verbose_name_plural = u'Страницы'

    def __unicode__(self):
        return self.name


class PageImage(models.Model):
    url = models.ImageField(upload_to="page")
    page = models.ForeignKey(Page)

    class Meta:
        verbose_name = u'Фото страницы'
        verbose_name_plural = u'Фото страницы'

    def __unicode__(self):
        return self.name

