from django.shortcuts import render, redirect
from django.views.generic import CreateView, View

from hadoop_choice.forms import DistributedFilesystemForm, DistributedProgrammingForm, \
    MachineLearningForm, SQLonHadoopForm, ChoiceAlgorithmFrom

from hadoop_choice.models import *

from hadoop_choice.algorithm.main import *


class MainView(View):
    def get(self, request, *args, **kwargs):
        form_distributed_filesystem = DistributedFilesystemForm(prefix="form_distributed_filesystem ")
        form_distributed_programming = DistributedProgrammingForm(prefix="form_distributed_programming")
        form_machine_learning = MachineLearningForm(prefix="form_machine_learning")
        form_sql_on_hadoop = SQLonHadoopForm(prefix="form_sql_on_hadoop")
        choice_algorithm = ChoiceAlgorithmFrom(prefix='choice_algorithm')
        return render(request, 'hadoop_choice.html', {'form_distributed_filesystem': form_distributed_filesystem,
                                                      'form_distributed_programming': form_distributed_programming,
                                                      'form_machine_learning': form_machine_learning,
                                                      'form_sql_on_hadoop': form_sql_on_hadoop,
                                                      'choice_algorithm': choice_algorithm,

        })

    def post(self, request, *args, **kwargs):
        print("post")
        form_distributed_filesystem = DistributedFilesystemForm(request.POST, prefix="form_distributed_filesystem ")
        form_distributed_programming = DistributedProgrammingForm(request.POST, prefix="form_distributed_programming")
        form_machine_learning = MachineLearningForm(request.POST, prefix="form_machine_learning")
        form_sql_on_hadoop = SQLonHadoopForm(request.POST, prefix="form_sql_on_hadoop")
        choice_algorithm = ChoiceAlgorithmFrom(request.POST, prefix="choice_algorithm")

        if form_distributed_filesystem.is_valid() and form_distributed_programming.is_valid() and form_machine_learning.is_valid() and form_sql_on_hadoop.is_valid():
            choice_algorithm.is_valid()
            df_data = form_distributed_filesystem.cleaned_data
            pr_data = form_distributed_programming.cleaned_data
            ml_data = form_machine_learning.cleaned_data
            sql_data = form_sql_on_hadoop.cleaned_data
            ch_alg = choice_algorithm.cleaned_data

            result = {}
            c = Choice()
            if ch_alg.get('usual_algorithm', None):
                result['1) Usual Algorithm'] = c.choice_usual_algorithm(df_data, pr_data, ml_data, sql_data)
            if ch_alg.get('all_set_pareto', None):
                result['2) Set Pareto'] = c.choice_set_pareto(df_data, pr_data, ml_data, sql_data)
            print(result)
            return render(request, 'result.html', {'result': result})

        return


class AllComponentView(View):
    def get(self, request, *args, **kwargs):
        all_data = {
            "DistributedFilesystem": DistributedFilesystem.objects.all(),
            "SQLonHadoop": SQLonHadoop.objects.all(),
            "MachineLearning": MachineLearning.objects.all(),
            "DistributedProgramming": DistributedProgramming.objects.all(),
        }
        return render(request, 'list_all_models_in_component.html', {"some_dict": all_data})


class CreateBaseView(CreateView):
    model = None
    template_name = 'add_model.html'
    slug_name = ""
    success_url = "/hadoop_choice/"

    def get_context_data(self, **kwargs):
        context = super(CreateBaseView, self).get_context_data(**kwargs)
        context['name'] = self.slug_name
        return context


class CreateDistributedFilesystemView(CreateBaseView):
    model = DistributedFilesystem
    slug_name = "DistributedFilesystem"


class CreateDistributedProgrammingView(CreateBaseView):
    model = DistributedProgramming
    slug_name = "DistributedProgramming"


class CreateMachineLearningView(CreateBaseView):
    model = MachineLearning
    slug_name = "MachineLearning"


class CreateSQLonHadoopView(CreateBaseView):
    model = SQLonHadoop
    slug_name = "SQLonHadoop"


class DeleteAllModelView(View):
        def get(self, request, *args, **kwargs):
            DistributedFilesystem.objects.all().delete()
            DistributedProgramming.objects.all().delete()
            MachineLearning.objects.all().delete()
            SQLonHadoop.objects.all().delete()
            return render(request, 'list_all_models_in_component.html', {"some_dict": {"All model": "DELETED"}})


main_input_view = MainView.as_view()
all_component = AllComponentView.as_view()

create_distributed_filesystem = CreateDistributedFilesystemView.as_view()
create_distributed_programming = CreateDistributedProgrammingView.as_view()
create_machine_learning = CreateMachineLearningView.as_view()
create_sql_on_hadoop = CreateSQLonHadoopView.as_view()

delete_all_model = DeleteAllModelView.as_view()