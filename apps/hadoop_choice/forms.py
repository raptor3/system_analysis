from django import forms
from hadoop_choice.models import *


class DistributedFilesystemForm(forms.ModelForm):
    class Meta:
        model = DistributedFilesystem
        fields = ('min_replication', 'min_write_retries', 'min_block_size')


class DistributedProgrammingForm(forms.ModelForm):
    class Meta:
        model = DistributedProgramming
        fields = ('min_reduce_tasks', 'max_reduce_tasks', 'min_map_tasks', 'max_map_tasks', 'support_streaming', 'programming_language')


class MachineLearningForm(forms.ModelForm):
    class Meta:
        model = MachineLearning
        fields = ('open_source','distributed', 'supervise_learning', 'unsupervise_learning', 'reinforcement_learning')

class SQLonHadoopForm(forms.ModelForm):
    class Meta:
        model = SQLonHadoop
        fields = ('execute_engine','min_tread_workers', 'max_tread_workers', 'allow_multiple_session')


class ChoiceAlgorithmFrom(forms.Form):
    usual_algorithm = forms.BooleanField(required=False)
    all_set_pareto = forms.BooleanField(required=False)