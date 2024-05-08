FROM python:3.10

ADD main.py /app/

ADD Task.py /app/

ADD ToDoList.py /app/

WORKDIR /app

#RUN pip install unittest install dependencies

CMD [ "python", "main.py" ]


