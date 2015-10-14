#coding=utf-8
from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import random
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.

#csrf_exempt关闭csrf验证
@csrf_exempt
def index(request):
	#获取按时间排序的列表
	plist = PlayerInfo.objects.order_by('-pi_time').all()[:4]
	toplist = PlayerInfo.objects.order_by('-pi_tickets').all()[:4]
	#报名数量
	babynum = plist.count()
	#投票数量
	votenum = 0
	for vote in plist:
		votenum +=int(vote.pi_tickets)
	#从baby列表中随机选取三个
	random_list = random.sample(plist,3)
	topics_dict = {'toplist':toplist, 'plist':plist,'votenum':votenum,'babynum':babynum,'random_list':random_list}
	return render(request,'web/index.html',topics_dict)


def details(request):
	num = request.GET['id']
	info_dict ={}
	if num is not None:
		info_list = PlayerInfo.objects.get(id=num)
		info_dict['babyinfo']= info_list
	return render(request,'web/details.html',info_dict)
#选手报名视图函数
def player(request):
	if request.method=='POST':
		player_form = playerInfo()
		username = request.POST['name']
		player_form.pi_name = username
		print player_form.pi_name
		userphone = request.POST['phone']
		player_form.pi_phone = str(userphone)
		print player_form.pi_phone

		if 'photo' in request.FILES:
			image = request.FILES['photo']
			img = Image.open(image)
			#print image
			url='uploads/'+image.name
			#print url
			name=settings.MEDIA_ROOT+'/'+url
			print name
			if os.path.exists(name):   
				file, ext = os.path.splitext(image.name)
				file=file+str(random.randint(1,1000))
				image.name=file+ext
				url='uploads/'+image.name
				name=settings.MEDIA_ROOT+'/'+url
			img.save(name)
			player_form.pi_photo= url
			print player_form.pi_photo
			userdesc = request.POST['desc']
			player_form.pi_desc = userdesc
			print player_form.pi_desc
			player_form.save()
		else:
			image=None
	return render(request,'web/index.html')

def top(request):
	top_list = playerInfo.objects.order_by('-pi_tickets').all()[:100]
	return render(request,'web/top.html',{'top':top_list})

@csrf_exempt
def user_login(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username,password = password)
		if user is not None and user.is_active:
			login(request,user)				
		else:
			return HttpResponse("login fialed")
	return HttpResponseRedirect('/app/')
@csrf_exempt
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/app/')
@csrf_exempt
def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')	
		try:
			User.objects.get(username = username)
			return HttpResponse("username is already registered")
		except User.DoesNotExist:
			user = User.objects.create_user(username,email,password)
			userinfo = Userinfo()
			userinfo.user = user
			if user is not None:
				user.save()
				userinfo.save()
				return HttpResponseRedirect('/app/')
			else:
				return HttpResponse("register failed")
	return HttpResponse("username is already registered")


'''
def check_name(request):  
	if request.method == 'GET':  
		try:  
			user = User.objects.get(username = request.GET['username']);  
			if user is not None:  
				return HttpResponse(json.jumps({'msg':'用户名已存在'}))  
		except:  
            			return HttpResponse(json.jumps({'msg':'用户名no存在'})) '''


@csrf_exempt
def vote(request):
	bid = request.GET['bid']
	info_list = PlayerInfo.objects.get(id = bid)
	if request.user.is_authenticated():
		user_list = Userinfo.objects.get(user = request.user)
		#求出距离上次投票的天数,,USE_TZ = False时，取出的时间不带时区信息
		ifvote = (datetime.now()  - user_list.vote_time).days
		if ifvote >= 1:
			user_list.voteid = 0
		if user_list.voteid == 1:
			return  HttpResponse("You have only once chance to give flower to your lover.  ")
		else:
			user_list.voteid = 1
			user_list.vote_time = datetime.now()
			user_list.save()
			info_list.pi_tickets = info_list.pi_tickets+1
			info_list.save()
		return HttpResponse(str(info_list.pi_tickets))
	else:
		return HttpResponse(str(info_list.pi_tickets))

@csrf_exempt
def search(request):
	search_dict = {}
	str = request.GET['search']
	if str in None:
		result = PlayerInfo.objects.get(id = str)
		return render(request,'web/details.html',search_dict)
	return HttpResponseRedirect('/app/')


