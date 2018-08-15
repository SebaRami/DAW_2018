from django.shortcuts import render

def cookies_demo(request):
	username = ""
	pwd = ""
	template_name = "manage_cookies/login_cookie.html"
	if request.method == 'POST':
		username = request.POST.get('user')
		pwd = request.POST.get('pwd')
	response = render(request, template_name, {'user':username, 'pwd':pwd})
	response.set_cookie('user', username)
	response.set_cookie('pwd', pwd)
	return response