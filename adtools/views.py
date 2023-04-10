from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
import whois
from .models import Short, Dom, News, FCMDevice
import re
from adtools.tasks import dom_aval
from celery import group

from .forms import DomainForm, ShortForm, HostingForm, IpForm, EmailForm, SSLForm

def fcm_view(request):
	if request.method == 'POST':
		registration_id = request.POST.get('registration_id')
		num_results = FCMDevice.objects.filter(registration_id=registration_id).count()
		if num_results > 0:
			return HttpResponse('The user is already in the database!')
		fcm = FCMDevice()
		fcm.registration_id = registration_id
		fcm.save()
	return HttpResponse('Done!')

def news_view(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		news = News()
		news.email = email
		news.save()
	return redirect(request.META.get('HTTP_REFERER'))

def email_view(request):
	context = {}
	context['form'] = EmailForm()
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			size = form.cleaned_data.get('size')
			a = form.cleaned_data.get('num')
			num = int(a)
			link = 'https://namecheap.pxf.io/e4YGZz'
			context['link'] = link
			if size == '5':
				best = 'Starter Business Email'
				context['best'] = best
			elif size == '30':
				if num < 5 or num > 7:
					best = 'Pro Business Email'
					context['best'] = best
				else:
					best = 'Ultimate Business Email'
					context['best'] = best
			elif size == '75':
				best = 'Ultimate Business Email'
				context['best'] = best

	return render(request, 'email.html', context)

def ip_view(request):
	context = {}
	context['form'] = IpForm()
	if request.method == 'GET':
		return render(request, 'ip.html', context)

	elif request.method == 'POST':
		form = IpForm(request.POST)
		if form.is_valid():
			domain = form.cleaned_data.get('domain')
			if '.' not in domain:
				domain = domain + '.com'
			context['domain'] = domain
			try:
				w = whois.whois(domain)
				context['w'] = w
				a = w.text
				b = re.sub(".*#.*\n?","",a)
				c = b.splitlines()
				context['c'] = c
			except:
				err = 1
				context['err'] = err
	return render(request, 'ip.html', context)

def location_view(request):
	context = {}
	context['form'] = DomainForm()
	if request.method == 'GET':
		return render(request, 'location.html', context)
	elif request.method == 'POST':
		form = DomainForm(request.POST)
		if form.is_valid():
			domain = form.cleaned_data.get('domain')
			if '.' not in domain:
				domain = domain + '.com'
			context['domain'] = domain
			form.save()
			rets = Dom.objects.all().values_list()
			recen = []
			for a in rets:
				recen.append(a[1])
			recent = recen[::-1]
			recents = recent[0:10]
			context['recents'] = recents
			try:
				w = whois.whois(domain)
				context['w'] = w

				if 'registrant_street' in w:
					ordered = {"Domain Name: ": w["domain_name"], "Address: ": w["registrant_street"][0], "City: ": w["registrant_city"][0], "State: ": w["registrant_state_province"],
								"Postcode: ": w["registrant_postal_code"][0], "Country: ": w["registrant_country"]}
				elif 'address' in w:
					ordered = {"Domain Name: ": w["domain_name"], "Address: ": w["address"], "City: ": w["city"], "State: ": w["state"],
								"Postcode: ": w["registrant_postal_code"], "Country: ": w["country"]}
				info = []
				for x in ordered:
					a = str(x) + str(ordered[x])
					info.append(a)
				context['info'] = info
			except:
				err = 1
				context['err'] = err
	return render(request, 'location.html', context)

def hosting_view(request):
	context = {}
	context['form'] = HostingForm()
	if request.method == 'GET':
		feedback = 1
		context['feedback'] = feedback
		return render(request, 'hosting.html', context)

	elif request.method == 'POST':
		form = HostingForm(request.POST)
		if form.is_valid():
			site = form.cleaned_data.get('site')
			serv = form.cleaned_data.get('serv')
			visitor = form.cleaned_data.get('visitor')
			content = form.cleaned_data.get('content')
			num = int(site) + int(visitor) + int(content)

			if serv == 'min' or serv == 'unsure':
				if num == 0:
					best = 'Stellar Shared Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/624623/5618'
					context['link'] = link
					context['best'] = best
				elif num == 1:
					best = 'Stellar Business Shared Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/624623/5618'
					context['link'] = link
					context['best'] = best
				elif num == 2:
					best = 'Stellar Plus Shared Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/624623/5618'
					context['link'] = link
					context['best'] = best
				elif num == 3:
					best = 'EasyWP Starter WordPress Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/1417922/5618'
					context['link'] = link
					context['best'] = best
				elif num == 4 or num == 5:
					best = 'EasyWP Turbo WordPress Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/1417922/5618'
					context['link'] = link
					context['best'] = best
				elif num > 5:
					best = 'EasyWP Supersonic WordPress Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/1417922/5618'
					context['link'] = link
					context['best'] = best
			elif serv == 'wp':
				if num >= 0 and num <= 2:
					best = 'EasyWP Starter WordPress Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/1417922/5618'
					context['link'] = link
					context['best'] = best
				elif num > 2 and num <= 5:
					best = 'EasyWP Turbo WordPress Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/1417922/5618'
					context['link'] = link
					context['best'] = best
				elif num > 5 and num <= 8:
					best = 'EasyWP Supersonic WordPress Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/1417922/5618'
					context['link'] = link
					context['best'] = best
			elif serv == 'self':
				if num >= 0 and num <= 2:
					best = 'Pulsar VPS Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/624643/5618'
					context['link'] = link
					context['best'] = best
				elif num > 2 and num <= 5:
					best = 'Quasar VPS Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/624643/5618'
					context['link'] = link
					context['best'] = best
				elif num > 5 and num <= 8:
					best = 'Magnetar VPS Hosting'
					link = 'https://namecheap.pxf.io/c/3692161/624643/5618'
					context['link'] = link
					context['best'] = best
			elif serv == 'dedicated':
				best = 'Dedicated Server Hosting'
				link = 'https://namecheap.pxf.io/c/3692161/408749/5618'
				context['link'] = link
				context['best'] = best
	return render(request, 'hosting.html', context)

def whois_view(request):
	context = {}
	context['form'] = DomainForm()
	if request.method == 'GET':
		form = DomainForm(request.GET)
		if form.is_valid():
			domain = form.cleaned_data.get('domain')
			if '.' not in domain:
				domain = domain + '.com'
			context['domain'] = domain
			rets = Dom.objects.all().values_list()
			recen = []
			for a in rets:
				recen.append(a[1])
			recent = recen[::-1]
			recents = recent[0:10]
			context['recents'] = recents
			try:
				w = whois.whois(domain)
				a = w.text
				if "Domain not found" in a or "DOMAIN NOT FOUND" in a or "Not Found" in a or "No match" in a or "No Data Found" in a or "Status: AVAILABLE" in a:
					err = 1
					context['err'] = err
				d = a.splitlines()
				context['w'] = w
				context['d'] = d
			except:
				err = 1
				context['err'] = err
	return render(request, 'whois.html', context)

def ssl_view(request):
	context = {}
	context['form'] = SSLForm()
	if request.method == 'POST':
		form = SSLForm(request.POST)
		if form.is_valid():
			site = form.cleaned_data.get('site')
			serv = form.cleaned_data.get('serv')
			num = form.cleaned_data.get('num')
			link = 'https://namecheap.pxf.io/P079kj'
			context['link'] = link
			
			if num == '1':
				if serv == '0':
					if site == '1':
						best = 'PositiveSSL Certificate'
						context['best'] = best
					elif site == '2':
						best = 'InstantSSL Certificate'
						context['best'] = best
					elif site == '3':
						best = 'EV SSL Certificate'
						context['best'] = best
				elif serv == '1':
					if site == '1':
						best = 'PositiveSSL Wildcard Certificate'
						context['best'] = best
					elif site == '2':
						best = 'EssentialSSL Wildcard Certificate'
						context['best'] = best
					elif site == '3':
						best = 'PremiumSSL Wildcard Certificate'
						context['best'] = best
			elif num == '2':
				if site == '1':
					best = 'PositiveSSL Multi-Domain Certificate'
					context['best'] = best
				elif site == '2':
					best = 'Unified Communications SSL Certificate'
					context['best'] = best
				elif site == '3':
					best = 'EV Multi-Domain SSL Certificate'
					context['best'] = best
	return render(request, 'ssl.html', context)

def index_view(request):
	context = {}
	context['form'] = DomainForm()
	separator = "."
	if request.method == 'POST':
		form = DomainForm(request.POST)
		if form.is_valid():
			domain = form.cleaned_data.get('domain')
			if domain.startswith("www."):
				domain = domain.replace("www.", "")
			if domain.startswith("WWW."):
				domain = domain.replace("WWW.", "")
			if '.' not in domain:
				domain = domain + '.com'
			context['domain'] = domain
			form.save()

			dom = domain.split(separator, 1)[0]
			doms = ['.com', '.org', '.net', '.xyz', '.biz', '.app', '.online', '.io', '.me', '.us', '.uk', '.ca', '.eu', '.de', '.in', '.mobi', '.cc', '.co', '.info', '.ru']
			lastly = []
			for i in doms:
				lastly.append(dom+i)

			lastly.append(domain)

			context['domcom'] = lastly[0]
			context['domorg'] = lastly[1]
			context['domnet'] = lastly[2]
			context['domxyz'] = lastly[3]
			context['dombiz'] = lastly[4]
			context['domapp'] = lastly[5]
			context['domonline'] = lastly[6]
			context['domio'] = lastly[7]
			context['domme'] = lastly[8]
			context['domus'] = lastly[9]
			context['domuk'] = lastly[10]
			context['domca'] = lastly[11]
			context['domeu'] = lastly[12]
			context['domde'] = lastly[13]
			context['domin'] = lastly[14]
			context['dommobi'] = lastly[15]
			context['domcc'] = lastly[16]
			context['domco'] = lastly[17]
			context['dominfo'] = lastly[18]
			context['domru'] = lastly[19]

			g = group(dom_aval.s(i) for i in lastly)
			r = g()
			res = r.get()

			com, org, net, xyz, biz, app, online, io, me, us, uk, ca, eu, de, hin, mobi, cc, co, info, ru, main = res
			context['com'] = com
			context['org'] = org
			context['net'] = net
			context['xyz'] = xyz
			context['biz'] = biz
			context['app'] = app
			context['online'] = online
			context['io'] = io
			context['me'] = me
			context['us'] = us
			context['uk'] = uk
			context['ca'] = ca
			context['eu'] = eu
			context['de'] = de
			context['hin'] = hin
			context['mobi'] = mobi
			context['cc'] = cc
			context['co'] = co
			context['info'] = info
			context['ru'] = ru
			context['main'] = main

	else:
		form = DomainForm()
	return render(request, 'index.html', context)

def short_view(request):
    context = {}
    context['form'] = ShortForm()

    if request.method == 'GET':
        return render(request, 'shortener.html', context)

    elif request.method == 'POST':

        form = ShortForm(request.POST)

        if form.is_valid():
            shortened_object = form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url

            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, 'shortener.html', context)

        else:

            context['errors'] = form.errors

            return render(request, 'shortener.html', context)

def privacy_view(request):
	return render(request, 'privacy.html')

def terms_view(request):
	return render(request, 'terms.html')

def contact_view(request):
	return render(request, 'contact.html')

def about_view(request):
	return render(request, 'about.html')

def recent_view(request):
	context = {}
	rets = Dom.objects.all().values_list()
	recen = []
	for a in rets:
		recen.append(a[1])
	recents = recen[::-1]
	paginator = Paginator(recents, 30)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context['page_obj'] = page_obj
	return render(request, 'recent.html', context)

def redirect_view(request, shortened_part):
	try:
		shortener = Short.objects.get(short_url=shortened_part)

		shortener.times_followed += 1

		shortener.save()

		return HttpResponseRedirect(shortener.long_url)

	except:
		raise Http404('Sorry this link is broken :(')