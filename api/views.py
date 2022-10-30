from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET",])
def slack_info_api(request, *args, **kwargs):
	data = {
		'slackUsername': 'UkemeB',
		'backend': True,
		'age': 'number',
		'bio': 'I am a Django Developer',
	}
	return JsonResponse(data)