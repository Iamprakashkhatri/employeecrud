from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from . forms import EmployeeForm
from . models import Employee
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    TemplateView
    )

# def emp(request):
#     if request.method=='POST':
#         form=EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect()
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request,"",{'form':form}
class EmployeeView(View):
    template_name="home.html"
    abc=Employee.objects.all()
    # context_object_name='this'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'employee':self.abc})
class EmployeeTemplateView(TemplateView):
    template_name = "home.html"
    model=Employee
    # context_object_name='this'

    def get_context_data(self, **kwargs):
        context=super(EmployeeTemplateView,self).get_context_data(**kwargs)
        context['employee_list'] = Employee.objects.filter()[:1]
        context['employee1_list'] = Employee.objects.filter()[1:1]
        return context

class EmployeeListView(ListView):
    template_name = "list.html"
    queryset = Employee.objects.all()
    def get_context_data(self,**kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['employee_list'] = self.queryset
        return context


class EmployeeDetailView(DetailView):
    template_name = "detail.html"
    queryset = Employee.objects.all()

    def get_object(self):
        pk_=self.kwargs.get("pk")
        return get_object_or_404(Employee,pk=pk_)

class EmployeeCreateView(CreateView):
    template_name="index.html"
    form_class = EmployeeForm
    # queryset=Employee.objects.all()

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

    success_url = reverse_lazy('createcrud:list')

class EmployeeUpdateView(UpdateView):
    template_name="index.html"
    form_class = EmployeeForm
    # queryset=Employee.objects.all()

    def get_object(self):
        pk_=self.kwargs.get("pk")
        return get_object_or_404(Employee,pk=pk_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    success_url = reverse_lazy('createcrud:list')



# class EmployeeDeleteView(DeleteView):
#     template_name = "delete.html"
#     # queryset = Employee.objects.all()
#
#     def get_object(self):
#         id_=self.kwargs.get("id")
#         return get_object_or_404(Employee,id=id_)
#     def get_success_url(self):
#         return reverse('createcrud:list')

class EmployeeDelete(DeleteView):
    template_name = "delete.html"
    model = Employee



    def get_success_url(self):
        return reverse('createcrud:list')
