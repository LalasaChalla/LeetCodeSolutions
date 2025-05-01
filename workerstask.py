class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()
        workers.sort()

        task_index=0
        task_completed=0
        work_index=0
        while task_index < len(tasks) and work_index < len(workers):
            if workers[work_index]>=tasks[task_index]:
                task_completed+=1
                task_index+=1
                work_index+=1
            else:
                if pills>0 and workers[work_index] + strength >=tasks[task_index]:
                    task_completed+=1
                    task_index+=1
                    work_index+=1
                    pills=pills-1

        return task_completed


        
