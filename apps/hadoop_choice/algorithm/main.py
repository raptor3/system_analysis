from hadoop_choice.models import *



class Choice:
    def allDFS(self):
        return DistributedFilesystem.objects.all()

    def allML(self):
        return MachineLearning.objects.all()

    def allPR(self):
        return DistributedProgramming.objects.all()

    def allSQL(self):
        return SQLonHadoop.objects.all()

    def selectDFS(self, allDFS, data, only_one=False):
        selectDFS = []

        for dsf in allDFS:
            flag = True
            if data['min_block_size'] < dsf.min_block_size or data['min_block_size'] > dsf.max_block_size:
                flag = False

            if data['min_write_retries'] < dsf.min_write_retries or data['min_write_retries'] > dsf.max_write_retries:
                flag = False

            if data['min_replication'] < dsf.min_replication or data['min_replication'] > dsf.max_replication:
                flag = False
            if flag:
                if only_one:
                    return dsf
                else:
                    selectDFS.append(dsf)
        return selectDFS

    def selectSQL(self, allSQL, data, only_one=False):
        selectSQL = []

        for sql in allSQL:
            flag = True
            if data['min_tread_workers'] < sql.min_tread_workers:
                flag = False
            if data['max_tread_workers'] > sql.max_tread_workers:
                flag = False
            if data['allow_multiple_session'] and data['allow_multiple_session'] != sql.allow_multiple_session:
                flag = False
            if data['execute_engine'] != sql.execute_engine:
                flag = False
            if flag:
                if only_one:
                    return sql
                else:
                    selectSQL.append(sql)
        return selectSQL

    def selectPR(self, allPR, data, only_one=False):
        selectPR = []

        for pr in allPR:
            flag = True
            if data['min_reduce_tasks'] < pr.min_reduce_tasks:
                flag = False
            if data['max_reduce_tasks'] > pr.max_reduce_tasks:
                flag = False
            if data['min_map_tasks'] < pr.min_map_tasks:
                flag = False
            if data['max_map_tasks'] > pr.max_map_tasks:
                flag = False

            if data['support_streaming'] and data['support_streaming'] != pr.support_streaming:
                flag = False
            if data['programming_language'] != 'all' and data['programming_language'] != pr.programming_language:
                flag = False
            if flag:
                if only_one:
                    return pr
                else:
                    selectPR.append(pr)
            return selectPR

    def selectML(self, allML, data, only_one=False):
        selectML = []

        for ml in allML:
            flag = True
            if data['open_source'] and data['open_source'] != ml.open_source:
                flag = False
            if data['distributed'] and data['distributed'] != ml.distributed:
                flag = False
            if data['supervise_learning'] and data['supervise_learning'] != ml.supervise_learning:
                flag = False
            if data['unsupervise_learning'] and data['unsupervise_learning'] != ml.unsupervise_learning:
                flag = False
            if data['reinforcement_learning'] and data['reinforcement_learning'] != ml.reinforcement_learning:
                flag = False
            if flag:
                if only_one:
                    return ml
                else:
                    selectML.append(ml)
        return selectML

    def choice_usual_algorithm(self, dfs_data, pr_data, ml_data, sql_data):
        allDFS = self.allDFS()
        allML = self.allML()
        allPR = self.allPR()
        allSQL = self.allSQL()

        dfs = self.selectDFS(allDFS, dfs_data, only_one=True)
        sql = self.selectSQL(allSQL, sql_data, only_one=True)
        pr = self.selectPR(allPR, pr_data, only_one=True)
        ml = self.selectML(allML, ml_data, only_one=True)


        return [dfs, sql, pr, ml]

    def choice_set_pareto(self, dfs_data, pr_data, ml_data, sql_data):
        allDFS = self.allDFS()
        allML = self.allML()
        allPR = self.allPR()
        allSQL = self.allSQL()

        dfs_selected = self.selectDFS(allDFS, dfs_data, only_one=False)
        sql_selected = self.selectSQL(allSQL, sql_data, only_one=False)
        pr_selected = self.selectPR(allPR, pr_data, only_one=False)
        ml_selected = self.selectML(allML, ml_data, only_one=False)

        pareto_set = []
        for dfs in dfs_selected:
            for sql in sql_selected:
                for pr in pr_selected:
                    for ml in ml_selected:
                        pareto_set.append([dfs, sql, pr, ml])
        return pareto_set
