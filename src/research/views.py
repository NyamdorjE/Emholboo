from django.shortcuts import render
from .models import Research, ResearchCategory, Law, LawCategory
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q

# Create your views here.

class ResearchCategoryView(generic.ListView):
    template_name = 'research/research.html'
    context_object_name = 'ResearchCategory'
    
    def get_queryset(self):
        queryset = super(ResearchCategory, self).get_queryset()
        queryset = ResearchCategory.objects.all()
        return queryset
    
    
class ResearchList(generic.ListView):
    queryset = Research.objects.all().order_by('created_on')
    template_name = 'research/research.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ResearchList, self).get_context_data(**kwargs)
        context['research'] = self.get_queryset()
        context['category_list'] = ResearchCategory.objects.all()
        context['search_text'] = self.request.GET.get('search_text', '')
        return context
    
    def get_queryset(self):
        queryset = super(ResearchList, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(content__icontains=search_text)
            )
        return queryset
    
    
class ResearchDetail(generic.DetailView):
    model = Research
    template_name = "research/research_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(ResearchDetail, self).get_context_data(**kwargs)
        context['research_list'] = Research.objects.all()
        context['category_list'] = ResearchCategory.objects.all()
        return context
    

class LawList(generic.ListView):
    template_name = "research/law.html"
    queryset = Law.objects.all()
    model = Law
    
    def get_context_data(self, **kwargs):
        context = super(LawList, self).get_context_data()
        context['law'] = Law.objects.all()
        return context
