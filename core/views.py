from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class AbsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @staticmethod
    def __insert_paginator(iterable_object, page, items_for_one_page):
        paginator = Paginator(iterable_object, items_for_one_page)
        try:
            iterable_object_selection = paginator.page(page)
        except PageNotAnInteger:
            iterable_object_selection = paginator.page(1)
        except EmptyPage:
            iterable_object_selection = paginator.page(paginator.num_pages)
        return iterable_object_selection

    def get_paginator(self, iterable_object, items_for_one_page=10):
        page = self.request.GET.get('page')
        return self.__insert_paginator(iterable_object, page, items_for_one_page)


class HomeView(AbsView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
