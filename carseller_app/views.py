from django.shortcuts import render,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import SellFilter
from .models import Sellrequest

# Create your views here.
def page_not_found(request,exception):
    context =None
    if "tried" in str(exception):

        context={"exception":"Page not found"}
    else:
            context = {"exception": exception}
            print(exception)
    return render(request,'carseller_app/404.html',context)


def error403(request, exception):
    context = {"exception": exception}
    return render(request,'carseller_app/404.html', context)


def error500(request):
    context = {}
    return render(request,'carseller_app/500.html', context)

def index(request):
    sells = Sellrequest.objects.all()
    context={"title":"Главная страница с",
             "sells": sells
    }
    return render(request,"carseller_app/index.html",context)



def dabout(request):
    return render(request,"carseller_app/about.html")
def contacts(request):
    return render(request,"carseller_app/contacts.html")
def faq(request):
    return render(request,"carseller_app/faq.html")



class SellDetailView(DetailView):
    model=Sellrequest


# #проверка от класса на залогиненого пользователя
class SellCreateView(LoginRequiredMixin,CreateView):
    model=Sellrequest
    fields=['price','region','inginvolume',"color"]


    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)

class SellUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Sellrequest
    fields=['TyrName','TyrType','TyrPrice','image']

    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        sell=self.get_object()
        return self.request.user==sell.Author
#
class SellDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Sellrequest
    success_url = "/"

    def test_func(self):
        sell=self.get_object()
        return self.request.user==sell.Author


class FilterSellListView(ListView):
    filter_class = None

    def get_queryset(self):
        qs=super().get_queryset()
        req=self.request.GET
        self.filtered=self.filter_class(req,qs)
        return self.filtered.qs.distinct()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["filter"]=self.filtered
        return context

class SellListView(FilterSellListView):

    model=Sellrequest
    filter_class = SellFilter
    template_name = "carseller_app/index.html"
    context_object_name = "sells"
    paginate_by = 5