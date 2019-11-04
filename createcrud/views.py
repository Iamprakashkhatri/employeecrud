from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from . forms import EmployeeForm
from . models import Employee
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    DeleteView
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
class EmployeeListView(ListView):
    template_name = "list.html"
    queryset = Employee.objects.all()

class EmployeeDetailView(DeleteView):
    template_name = "detail.html"
    queryset = Employee.objects.all()

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Employee,id=id_)

class EmployeeCreateView(CreateView):
    template_name="index.html"
    form_class = EmployeeForm
    queryset=Employee.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
class EmployeeUpdateView(UpdateView):
    template_name="index.html"
    form_class = EmployeeForm
    # queryset=Employee.objects.all()

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Employee,id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



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
