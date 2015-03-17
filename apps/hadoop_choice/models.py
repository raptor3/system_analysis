from django.db import models


class DistributedFilesystem(models.Model):
    name = models.CharField(max_length=100)

    min_replication = models.IntegerField()
    max_replication = models.IntegerField()

    min_write_retries = models.IntegerField()
    max_write_retries = models.IntegerField()

    min_block_size = models.IntegerField()
    max_block_size = models.IntegerField()

    def __str__(self):
        return "Name : %s |" \
               "min_replication : %s |" \
               "max_replication : %s |" \
               "min_write_retries : %s |" \
               "max_write_retries : %s |" \
               "min_block_size : %s |" \
               "max_block_size : %s |" % \
               (self.name, self.min_replication, self.max_replication, self.min_write_retries, self.max_write_retries,
                self.min_block_size, self.max_block_size)


class DistributedProgramming(models.Model):
    name = models.CharField(max_length=100)

    min_reduce_tasks = models.IntegerField()
    max_reduce_tasks = models.IntegerField()

    min_map_tasks = models.IntegerField()
    max_map_tasks = models.IntegerField()

    support_streaming = models.BooleanField()

    PYTHON = 'python'
    JAVA = 'java'
    SCALA = 'scala'
    ALL = 'all'
    PROGRAMMING_LANGUAGE = (
        (PYTHON, 'PYTHON'),
        (JAVA, 'JAVA'),
        (SCALA, 'SCALA'),
        (ALL, 'ALL'),
    )
    programming_language = models.CharField(max_length=6,
                                            choices=PROGRAMMING_LANGUAGE,
                                            default=JAVA)

    def __str__(self):
        return "Name : %s |" \
               "min_reduce_tasks : %s |" \
               "max_reduce_tasks : %s |" \
               "min_map_tasks : %s |" \
               "max_map_tasks : %s |" \
               "support_streaming : %s |" \
               "programming_language : %s |" % \
               (self.name, self.min_reduce_tasks, self.max_reduce_tasks, self.min_map_tasks, self.max_map_tasks,
                self.support_streaming, self.programming_language)


class MachineLearning(models.Model):
    name = models.CharField(max_length=100)
    open_source = models.BooleanField(default=False)
    distributed = models.BooleanField(default=False)
    supervise_learning = models.BooleanField(default=False)
    unsupervise_learning = models.BooleanField(default=False)
    reinforcement_learning = models.BooleanField(default=False)

    def __str__(self):
        return "Name : %s |" \
               "open_source : %s |" \
               "distributed : %s |" \
               "supervise_learning : %s |" \
               "unsupervise_learning : %s |" \
               "reinforcement_learning : %s |" % \
               (self.name, self.open_source, self.distributed, self.supervise_learning, self.unsupervise_learning,
                self.reinforcement_learning)


class SQLonHadoop(models.Model):
    name = models.CharField(max_length=100)
    TEZ = 'tez'
    MR = 'mr'
    ALL = 'all'
    EXECUTE_ENGINE = (
        (TEZ, 'TEZ'),
        (MR, 'MR'),
        (ALL, 'ALL'),
    )
    execute_engine = models.CharField(max_length=3,
                                      choices=EXECUTE_ENGINE,
                                      default=MR)

    min_tread_workers = models.IntegerField()
    max_tread_workers = models.IntegerField()
    allow_multiple_session = models.BooleanField()

    def __str__(self):
        return "Name : %s |" \
               "execute_engine : %s |" \
               "min_tread_workers : %s |" \
               "max_tread_workers : %s |" \
               "allow_multiple_session : %s |" % \
               (self.name, self.execute_engine, self.min_tread_workers, self.max_tread_workers,
                self.allow_multiple_session)

