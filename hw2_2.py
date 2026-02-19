task_queue=[]
task_history=[]
def task_add(task):
    task_queue.append(task)
    return f'Задача успешно добавлена. Номер задачи в очереди:{len(task_queue)-1}', 
def next(queue:list, history:list):
    history.append(task_queue.pop(0)) if len(task_queue)>0 else 0
    return f'Задача выполнена. Количество задач в очереди:{len(task_queue)}' if len(task_queue)>=0 else 'B очереди нет задач'
def task_list(queue:list, history:list):
    return f'Список задач:\n Выполненные:{history}\n B очереди:{queue}'
def task_priority(task, queue:list):
    a = [queue.pop(queue.index(task))]
    queue= a+queue
    return 'Задача успешно приоритезирована'

