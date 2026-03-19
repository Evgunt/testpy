import datetime
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Record, Category, Subcategory, Type, Status
from . import forms


# Класс для вывода Записей
class RecordList(ListView):
    template_name = 'main/index.html'
    context_object_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передача списков для фильтра в шаблон
        context['status_list'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()

        return context

    def get_queryset(self):
        qs = Record.objects.all()
        # Данные фильтра
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        status = self.request.GET.get('status')
        type_id = self.request.GET.get('type')
        category_id = self.request.GET.get('category')
        subcategory_id = self.request.GET.get('subcategory')
        # Сама фильтрация
        if date_from:
            qs = qs.filter(date__gte=date_from)
        if date_to:
            qs = qs.filter(date__lte=date_to)
        if status and status != '0':
            qs = qs.filter(status=status)
        if type_id and type_id != '0':
            qs = qs.filter(subcategory__parent__type__id=type_id)
        if category_id and category_id != '0':
            qs = qs.filter(subcategory__parent__id=category_id)
        if subcategory_id and subcategory_id != '0':
            qs = qs.filter(subcategory__id=subcategory_id)

        return qs


# Класс для создания Записей
class RecordAdd(CreateView):
    model = Record
    template_name = 'main/add.html'
    form_class = forms.RecordAddForm
    success_url = reverse_lazy('main:index')

    # Автозаполнение даты (сегодня)
    def get_initial(self):
        initial = super().get_initial()
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        initial['date'] = formatted_date
        return initial


# Класс для редактирования Записей
class RecordUpdate(UpdateView):
    model = Record
    template_name = 'main/add.html'
    form_class = forms.RecordAddForm
    success_url = reverse_lazy('main:index')

    def get_initial(self):
        initial = super().get_initial()
        # Заполнение и форматирование даты
        record = self.object
        formatted_date = record.date.strftime("%Y-%m-%d")
        initial['date'] = formatted_date
        # Заполнение select данными из бд
        if record.subcategory and record.subcategory.parent:
            initial['type'] = record.subcategory.parent.type.id
            initial['category'] = record.subcategory.parent.id
        return initial


# Класс для удаления записей.
# Используется в ajax
class RecordDelete(DeleteView):
    model = Record
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:index')


class DirectoryList(TemplateView):
    template_name = 'main/directory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        context['statuses'] = Status.objects.all()
        return context


# Добавление, редактирование и удаление Типов
class CreateType(CreateView):
    model = Type
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class UpdateType(UpdateView):
    model = Type
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class DeleteType(DeleteView):
    model = Type
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:directory')


# Добавление, редактирование и удаление категорий
class CreateCategory(CreateView):
    model = Category
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class UpdateCategory(UpdateView):
    model = Category
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:directory')


# Добавление, редактирование и удаление подкатегорий
class CreateSubcategory(CreateView):
    model = Subcategory
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class UpdateSubcategory(UpdateView):
    model = Subcategory
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class DeleteSubcategory(DeleteView):
    model = Subcategory
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:directory')


# Добавление, редактирование и удаление статусов
class CreateStatus(CreateView):
    model = Status
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class UpdateStatus(UpdateView):
    model = Status
    template_name = 'main/add.html'
    success_url = reverse_lazy('main:directory')
    fields = '__all__'


class DeleteStatus(DeleteView):
    model = Status
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:directory')


# Функция получения категорий.
# Используется в ajax
@require_GET
def get_categories(request):
    category_id = request.GET.get('typeId')
    types = Category.objects.filter(type=category_id).values('id', 'title')
    return JsonResponse(list(types), safe=False)


# Функция получения подкатегорий.
# Используется в ajax
@require_GET
def get_subcategories(request):
    subcategory_id = request.GET.get('categoryId')
    types = Subcategory.objects.filter(parent=subcategory_id).values('id', 'title')
    return JsonResponse(list(types), safe=False)
