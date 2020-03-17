from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings

def json_response(status, data=None, error=None, pages=None, hasNextPage=None):
	return JsonResponse(
		{
			"status": status, 
			"data": data,
			"pages": pages,
			"hasNextPage": hasNextPage,
			"error": error
		}
	)

def to_camel_case(string):
	if '_' not in string:
		return string
	while True:
		pos = string.find('_')
		after = pos + 1
		string = string[0:pos+1] + string[after].upper() + string[after+1:]  # make the char after the underscore uppercase
		string = string[0:pos] + string[after:]  # cut the underscore out of the string
		if '_' not in string:
			return string
	
def update_obj(obj, dictionary):
	for key, value in dictionary.items():
		setattr(obj, key, value)

def paginate(querySet, page, itemsPerPage=settings.ITEMS_PER_PAGE):
	paginator = Paginator(querySet, itemsPerPage)
	numberOfPages = paginator.num_pages
	pageN = paginator.get_page(page) if page in paginator.page_range else paginator.get_page(numberOfPages)
	hasNextPage = pageN.has_next() 
	objectList = pageN.object_list
	return objectList, hasNextPage, numberOfPages

