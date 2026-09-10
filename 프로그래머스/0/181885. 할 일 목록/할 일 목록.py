def solution(todo_list, finished):
    num = 0
    for i in range(len(todo_list)):
        if finished[num] == True:
            todo_list.remove(todo_list[num])
            finished.remove(finished[num])
        else:
            num += 1
            
    return todo_list