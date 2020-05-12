import csv
import zipfile

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from .models import Session, Experiment
from zipfile import ZipFile
from django.utils import timezone

# Create your views here.
class SessionCreateView(generic.edit.CreateView):
    model = Session
    fields = ['filename']
    template_name_suffix = '_create'
    def clean_filename(self):
        return self.cleaned_data['filename'] or None
    def form_valid(self,form):
        if form.instance.filename is None:
            form.instance.filename = timezone.now().strftime("%d%m%Y_%H%M%S")
        return super(SessionCreateView, self).form_valid(form)
    #def get_success_url(self):
    #    return HttpResponseRedirect(reverse('runexp:session', args=(self.object.filename,)))

class ExperimentCreateView(generic.edit.CreateView):
    model = Experiment
    fields = ['concentration']
    template_name_suffix = '_create'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = 0.00
        return context
    def form_valid(self, form):
        form.instance.session = get_object_or_404(Session, filename=self.kwargs.get('filename'))
        form.instance.result = 5
        return super(ExperimentCreateView, self).form_valid(form)

class ExperimentView(generic.DetailView):
    model = Experiment
    template_name = 'runexp/experiment.html'

class SessionListView(generic.ListView): #index
    model = Session
    template_name = 'runexp/session_list.html'
    def get_queryset(self):
        return Session.objects.all()

class SessionDetails(generic.DetailView):
    model = Session
    template_name = 'runexp/session_details.html'
    def get_object(self):
        return get_object_or_404(Session, filename=self.kwargs.get('filename'))
    def get_queryset(self):
        return Session.objects.all()

class ExperimentEditView(generic.edit.UpdateView):
    model = Experiment
    template_name_suffix = '_edit'
    fields = ['concentration','result']
    def get_object(self):
        return get_object_or_404(Experiment, pk=self.kwargs.get('eid'))
    def get_initial(self):
        return { 'concentration': self.get_object().concentration, 'result': self.get_object().result }
    def get_success_url(self):
        return reverse('runexp:session_details', kwargs={'filename':self.get_object().session.filename})
    
def delete_experiment(request,filename):
    session = get_object_or_404(Session, filename=filename)
    pk_list = request.POST.getlist('experiment')
    for i in pk_list:
        session.experiment_set.get(pk=i).delete()
    return HttpResponseRedirect(reverse('runexp:session_details', kwargs={'filename':filename}))
    
def delete_sessions(request):
    if 'delete' in request.POST: 
        name_list = request.POST.getlist('session')
        for i in name_list:
            Session.objects.get(filename=i).delete()
        return HttpResponseRedirect(reverse('runexp:index'))

def download_sessions(request):
    if 'download' in request.POST:
        response = HttpResponse(content_type='application/zip')
        zf = zipfile.ZipFile(response, 'w')

        name_list = request.POST.getlist('session')

        if name_list == []:
            return render(request, 'runexp/session_list.html', { #redisplay question
                'session_list': Session.objects.all(),
                'error_message': "You didn't select any sessions to download.",
            })

        csvs = []
        filenames = []
        for i in name_list:
            session = Session.objects.get(filename=i)
            filenames += [str(i) +'.csv']
            table_data = 'Concentration,Result\n'
            for experiment in session.experiment_set.all():
                table_data += str(experiment.concentration) + ',' + str(experiment.result) + '\n'
            csvs += [table_data]

        # create the zipfile in memory using writestr
        for i in range(0,len(csvs),1):
            zf.writestr(filenames[i],csvs[i])

        # return as zipfile
        response['Content-Disposition'] = 'attachment; filename="sessions_tables.zip"'
        return response

def delete_current_session(request,filename):
    session = get_object_or_404(Session,filename=filename)
    if 'delete' in request.POST: 
        session.delete()
    return HttpResponseRedirect(reverse('runexp:index'))

def download_current_session(request,filename):
    session = get_object_or_404(Session,filename=filename)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + str(filename) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Concentration', 'Result'])
    for experiment in session.experiment_set.all():
        writer.writerow([experiment.concentration,experiment.result])

    return response

def run_experiment(request,filename):
    if request.GET.get('run'):
        time = run(request)
    return HttpResponseRedirect(reverse('runexp:session', kwargs={'filename':filename}))
    return render(request, 'runexp/experiment_create.html', { #redisplay question
                'filename': filename,
                'time': time
            })

def run(request):
    return 4

