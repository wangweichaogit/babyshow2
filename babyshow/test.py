#! /usr/bin/python
#coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','babyshow.settings')

import django
django.setup()

from app.models import PlayerInfo

#define function
def add_message(name,phone,photo,desc,pi_tickets):
	p = PlayerInfo.objects.get_or_create(pi_name = name,pi_phone = phone,pi_photo = photo,pi_desc = desc,pi_tickets=pi_tickets)
	return p

def populate():
	add_message("小明","13548627845","/media/uploads/baby1.jpg","我是小明，请投我",10)
	add_message("小花","15974128642","/media/uploads/baby2.jpg","我是小花，请投我",20)
	add_message("小芳","18745286425","/media/uploads/baby3.jpg","我是小芳，请投我",30)
	add_message("小王","13548524569","/media/uploads/baby4.jpg","我是小王，请投我",40)
	
if __name__ == '__main__':
	print "start script...."
	populate()
	print "end script...."
