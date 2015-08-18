from django.shortcuts import render
from django.http import HttpResponse
from spotlight.models import *

# def index(request):
#   context_dict = {'boldmessage': "I am bold font from the context"}
#   return render(request, 'spotlight/index.html', context_dict)
import json
def search_form(request):
    return render(request, 'spotlight/index.html')


def search(request):
    title_ids=[]
    product_ids =[]
    if 'q' in request.GET:
        q = request.GET['q']
        titles = Source.objects.filter(title__contains =q)
        # print type(titles)
        # for title in titles:
        #   title_ids.append(title.id)
        # # print title_ids
        # for i in title_ids:
        products = Prod.objects.filter(source_id__in=titles)
        # product_ids.append(products)
        # print json.dumps(product_ids)

        return render(request, 'spotlight/search_results.html',
            {'titles': titles, 'query': q,'products':products})
    else:
        return HttpResponse('Please submit a search term.')

def flag(request):
      val = request.GET['test1']
      flag = Flag.objects.filter(product_id=request.GET['id']);
      if not flag:
        flag=Flag()
      flag.product_id = request.GET['id']
      for v in val.split("|"):
        v = v.strip()
        if (v == "Not_Helpful"):

          flag.Not_Helpful = "Not_Helpful"
        if (v == "Inappropriate"):
          flag.Inappropriate = "Inappropriate"
        if (v == "Wrong_Tags"):
          flag.Wrong_Tags = "Wrong_Tags"
        if (v == "Spam"):
          flag.Spam = "Spam"
      flag.save()
      return render(request)


def print_flag(request):
    flagged = Flag.objects.all()
    return render(request, 'spotlight/flag_results.html',
      {'flagged': flagged})


