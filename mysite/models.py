# -- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

Fields = (
    ('Металл, металлоизделия ', u'Металл, металлоизделия '),
    ('Оборудование, приборы, инструменты, комплектующие ', u'Оборудование, приборы, инструменты, комплектующие '),
    ('Транспорт, запчасти, аксессуары ', u'Транспорт, запчасти, аксессуары '),
    ('Электротехническое оборудование ', u'Электротехническое оборудование '),
    ('Одежда, обувь, текстиль, галантерея, кожа ', u'Одежда, обувь, текстиль, галантерея, кожа '),
    ('Прочее', u'Прочее'),
)
# Create your models here.

class Client(models.Model):
	user = models.OneToOneField(User, null=True, blank=True)
	organization = models.CharField(verbose_name=u'Организация', max_length=50, null=True)
	position = models.CharField(blank=True, verbose_name=u'Должность', max_length=50, null=True)
	phone_number = models.CharField(blank=True, verbose_name=u'Номер телефона', max_length=50, null=True)
	address = models.CharField(blank=True, verbose_name=u'Адрес', max_length=150, null=True)

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

class Category(models.Model):
	name = models.CharField(verbose_name=u'Наименование', max_length=50)
	description = models.TextField(verbose_name=u'Описание')

	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(verbose_name=u'Наименование', max_length=50)
	slug = models.SlugField(max_length=50, null=True)
	description = models.TextField(verbose_name=u'Описание')
	price = models.CharField(verbose_name=u'Диапозон стоимости', max_length=50)
	icon = models.ImageField()
	category = models.ForeignKey(Category, null=True, blank=True, verbose_name=u'Категория', related_name='category')
	def __unicode__(self):
		return self.name


class Order(models.Model):
	client = models.ForeignKey(Client, null=True, blank=True, verbose_name=u'Покупатель', related_name='client')
	is_temporary = models.NullBooleanField(verbose_name='Является корзиной', blank=True)

	def __unicode__(self):
		return self.client.user.first_name + ' ' + self.client.user.last_name 

class Order_product(models.Model):
	order = models.ForeignKey(Order, null=True, blank=True, verbose_name=u'Заказ', related_name='order')
	product = models.ForeignKey(Product, null=True, blank=True, verbose_name=u'Товар', related_name='product')
	quantity = models.IntegerField(null=True, blank=True, verbose_name=u'Количество')

	def __unicode__(self):
		return self.order.client.user.last_name + ' ' + self.product.name
