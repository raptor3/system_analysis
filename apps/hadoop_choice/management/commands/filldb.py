import sys

from django.conf import settings
from django.core.management.base import BaseCommand

from hadoop_choice.models import *


class Command(BaseCommand):
    help = 'Fill the database with test fixtures'

    def handle(self, *args, **options):
        sys.stdout.write('Starting fill db\r\n')

        sys.stdout.write('DistributedFilesystem\r\n')
        parDF = [
            ["ApacheDFS 1", 1, 10, 3, 10, 64, 256],
            ["ApacheDFS 2", 10, 20, 10, 20, 64, 256],
            ["ApacheDFS 3 ", 20, 30, 30, 40, 64, 256]
        ]
        for p in parDF:
            instance = DistributedFilesystem(name=p[0],
                                             min_replication=p[1],
                                             max_replication=p[2],
                                             min_write_retries=p[3],
                                             max_write_retries=p[4],
                                             min_block_size=p[5],
                                             max_block_size=p[6])
            instance.save()

        sys.stdout.write('MachineLearning\r\n')
        parML = [
            ["ApacheMahout", True, False, True, True, True],
            ["WEKA", True, False, True, True, False],
            ["Spark", True, True, True, True, True],

        ]
        for p in parML:
            instance = MachineLearning(name=p[0],
                                       open_source=p[1],
                                       distributed=p[2],
                                       supervise_learning=p[3],
                                       unsupervise_learning=p[4],
                                       reinforcement_learning=p[5])
            instance.save()

        sys.stdout.write('SQLonHadoop\r\n')
        parSQL = [
            ["Hive", 'tez', 1, 10, True],
            ["Hive", 'mr', 1, 10, True],
            ["Hive", 'all', 1, 10, True],

        ]
        for p in parSQL:
            instance = SQLonHadoop(name=p[0],
                                       execute_engine=p[1],
                                       min_tread_workers=p[2],
                                       max_tread_workers=p[3],
                                       allow_multiple_session=p[4])
            instance.save()

        sys.stdout.write('DistributedProgramming\r\n')
        parPR = [
            ["ApacheMapReduce 1 ", 1, 100, 1, 100, True, 'java'],
            ["ApacheMapReduce 2 ", 1, 100, 1, 100, True, 'python'],
            ["ApacheMapReduce 3 ", 1, 100, 1, 100, True, 'all'],

        ]
        for p in parPR:
            instance = DistributedProgramming(name=p[0],
                                       min_reduce_tasks=p[1],
                                       max_reduce_tasks=p[2],
                                       min_map_tasks=p[3],
                                       max_map_tasks=p[4],
                                       support_streaming=p[5],
                                       programming_language=p[6])
            instance.save()

        sys.stdout.write('Completed fill db\r\n')