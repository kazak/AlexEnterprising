# AlexEnterprising

Теперь разметка картинок входит в постоянные обязанности Лёши. Картинок становится всё больше, и Лёше пришла в голову идея привлечь внешних людей ему на помощь.

Кроме того чтобы давать одно задание сразу нескольким людям и выбирать самый частый ответ, Лёша решил предварительно разметить несколько заданий самостоятельно. Он не хочет учитывать ответы тех, кто отвечает верно на эти задания с вероятностью меньше 0,6.

Помогите Леше по предразмеченным задачам и вердиктам получить качественную разметку.

# Формат ввода:
  Сначала подаются строки (строк неизвестное количество) задач размеченных Лёшей в формате через пробел:

<task_id> <verdict>

где <task_id> - строчка, однозначно определяющая задание, а <verdict> - некоторое целое число, отвечающее за ответ на задачу

Далее (строк неизвестное количество) вам подается вердикт одного исполнителя на одну из задач в формате через пробел:

<worker_id> <task_id> <verdict>

где <worker_id> - некоторая строчка, однозначно определяющая исполнителя, <task_id> - строчка, однозначно определяющая задание, а <verdict> - некоторое целое число, отвечающее за ответ на задачу

# Формат вывода: 
  В качестве ответа на задачу вам нужно на отдельных строках вывести вердикты на задачи (без учёта предразмеченных задач):  &lt;task_id> &lt;verdict>  &lt;task_id> от &lt;verdict> отделено пробелом  Важно, при выводе &lt;task_id> должны быть отсортированы в лексикографическом порядке по возрастанию.
