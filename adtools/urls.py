from django.urls import path, re_path
from . import views
from django.views.generic.base import TemplateView

appname = "adtools"

urlpatterns = [
	path('', views.index_view, name='index'),
	re_path(r'^url-shortener/?$', views.short_view, name='shortener'),
	re_path(r'^ssl/?$', views.ssl_view, name='ssl'),
	re_path(r'^whois/?$', views.whois_view, name='whois'),
	re_path(r'^hosting/?$', views.hosting_view, name='hosting'),
	re_path(r'^location/?$', views.location_view, name='location'),
	re_path(r'^ip-lookup/?$', views.ip_view, name='ip'),
	re_path(r'^email/?$', views.email_view, name='email'),
	re_path(r'^privacy/?$', views.privacy_view, name='privacy'),
	re_path(r'^terms/?$', views.terms_view, name='terms'),
	re_path(r'^contact/?$', views.contact_view, name='contact'),
	re_path(r'^recent/?$', views.recent_view, name='recent'),
	re_path(r'^about/?$', views.about_view, name='about'),
	path('news/', views.news_view, name='news'),
	path('devices/', views.fcm_view, name='fcm'),
	path('why-custom-domain-important/', TemplateView.as_view(template_name='why-custom-domain-important.html', content_type='text/html'), name='domain-importance'),
	path('why-business-email-important/', TemplateView.as_view(template_name='why-business-email-important.html', content_type='text/html'), name='email-importance'),
	path('domain-location/', TemplateView.as_view(template_name='domain-location.html', content_type='text/html'), name='domain-location'),
	path('reverse-ip-lookup/', TemplateView.as_view(template_name='reverse-ip-lookup.html', content_type='text/html'), name='reverse-ip'),
	path('SSL-certificate/', TemplateView.as_view(template_name='SSL-certificate.html', content_type='text/html'), name='ssl-cert'),
	path('web-hosting-explained/', TemplateView.as_view(template_name='web-hosting-explained.html', content_type='text/html'), name='hosting-explained'),
	path('what-is-URL-shortener/', TemplateView.as_view(template_name='what-is-URL-shortener.html', content_type='text/html'), name='URL-shortener'),
	path('whois-lookup/', TemplateView.as_view(template_name='whois-lookup.html', content_type='text/html'), name='whois-lookup'),
	path('how-to-buy-domain/', TemplateView.as_view(template_name='how-to-buy-domain.html', content_type='text/html'), name='buy-domain'),
	path('how-to-use-URL-shortener/', TemplateView.as_view(template_name='how-to-use-URL-shortener.html', content_type='text/html'), name='usage-shortener'),
	path('how-to-buy-SSL-certificate/', TemplateView.as_view(template_name='how-to-buy-SSL-certificate.html', content_type='text/html'), name='how-to-buy-SSL-certificate'),
	path('how-to-buy-hosting/', TemplateView.as_view(template_name='how-to-buy-hosting.html', content_type='text/html'), name='buy-hosting'),
	path('choose-server-location/', TemplateView.as_view(template_name='choose-server-location.html', content_type='text/html'), name='server-loc'),
	path('how-to-buy-business-email/', TemplateView.as_view(template_name='how-to-buy-business-email.html', content_type='text/html'), name='buy-email'),
	path('how-to-buy-VPN/', TemplateView.as_view(template_name='how-to-buy-VPN.html', content_type='text/html'), name='buy-VPN'),
	path('e-commerce/', TemplateView.as_view(template_name='e-commerce.html', content_type='text/html'), name='ecommerce'),
	path('dropshipping/', TemplateView.as_view(template_name='dropshipping.html', content_type='text/html'), name='dropshipping'),
	path('drop-servicing/', TemplateView.as_view(template_name='drop-servicing.html', content_type='text/html'), name='dropservicing'),
	path('affiliate-marketing/', TemplateView.as_view(template_name='affiliate-marketing.html', content_type='text/html'), name='afmarketing'),
	path('ad-networks/', TemplateView.as_view(template_name='ad-networks.html', content_type='text/html'), name='adnetworks'),
	path('on-page-seo-checklist/', TemplateView.as_view(template_name='on-page-seo-checklist.html', content_type='text/html'), name='on-page-seo-checklist'),
	path('free-tools/', TemplateView.as_view(template_name='free-tools.html', content_type='text/html'), name='free-tools'),
	path('what-is/', TemplateView.as_view(template_name='what-is.html', content_type='text/html'), name='what-is'),
	path('how-to/', TemplateView.as_view(template_name='how-to.html', content_type='text/html'), name='how-to'),
	path('what-is-SSR/', TemplateView.as_view(template_name='what-is-SSR.html', content_type='text/html'), name='what-is-SSR'),
	path('sell-your-own-products/', TemplateView.as_view(template_name='sell-your-own-products.html', content_type='text/html'), name='sell-your-own-products'),
	path('sponsored-product-reviews/', TemplateView.as_view(template_name='sponsored-product-reviews.html', content_type='text/html'), name='sponsored-product-reviews'),
	path('container-technology/', TemplateView.as_view(template_name='container-technology.html', content_type='text/html'), name='container-technology'),
	path('learn-coding/', TemplateView.as_view(template_name='learn-coding.html', content_type='text/html'), name='learn-coding'),
	path('buy-monetized-website/', TemplateView.as_view(template_name='buy-monetized-website.html', content_type='text/html'), name='buy-monetized-website'),
	path('content-delivery-network/', TemplateView.as_view(template_name='content-delivery-network.html', content_type='text/html'), name='content-delivery-network'),
	path('reverse-proxy/', TemplateView.as_view(template_name='reverse-proxy.html', content_type='text/html'), name='reverse-proxy'),
	path('pycharm/', TemplateView.as_view(template_name='pycharm.html', content_type='text/html'), name='pycharm'),
	path('elastic-beanstalk/', TemplateView.as_view(template_name='elastic-beanstalk.html', content_type='text/html'), name='elastic-beanstalk'),
	path('wordpress/', TemplateView.as_view(template_name='wordpress.html', content_type='text/html'), name='wordpress'),
	path('blogger/', TemplateView.as_view(template_name='blogger.html', content_type='text/html'), name='blogger'),
	path('github/', TemplateView.as_view(template_name='github.html', content_type='text/html'), name='github'),
	path('canva/', TemplateView.as_view(template_name='canva.html', content_type='text/html'), name='canva'),
	path('chatgpt/', TemplateView.as_view(template_name='chatgpt.html', content_type='text/html'), name='chatgpt'),
	path('prompt-engineering/', TemplateView.as_view(template_name='prompt-engineering.html', content_type='text/html'), name='prompt-engineering'),
	path('november-2022/', TemplateView.as_view(template_name='november-2022.html', content_type='text/html'), name='november-2022'),
	path('december-2022/', TemplateView.as_view(template_name='december-2022.html', content_type='text/html'), name='december-2022'),
	path('january-2023/', TemplateView.as_view(template_name='january-2023.html', content_type='text/html'), name='january-2023'),
	path('february-2023/', TemplateView.as_view(template_name='february-2023.html', content_type='text/html'), name='february-2023'),
	path('march-2023/', TemplateView.as_view(template_name='march-2023.html', content_type='text/html'), name='march-2023'),
	path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
	path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml'), name='sitemap'),
	path('ads.txt', TemplateView.as_view(template_name='ads.txt', content_type='text/plain'), name='ads'),
	path('firebase-messaging-sw.js', TemplateView.as_view(template_name='firebase-messaging-sw.js', content_type='application/javascript',), name='firebase-messaging-sw'),
	path('opensearchdescription.xml', TemplateView.as_view(template_name='opensearchdescription.xml', content_type='application/xml'), name='opensearchdescription'),
	path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/json'), name='manifest'),
	path('<str:shortened_part>', views.redirect_view, name='redirect'),
]
