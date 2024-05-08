FROM python:3.10

ADD main.py /app/

ADD Task.py /app/

ADD TodoList.py /app/

ADD Test_Task.py /app/

ADD Test_TodoList.py /app/


WORKDIR /app
RUN echo "${{ secrets.DOCKER_HUB_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_HUB_USERNAME }}" --password-stdin



CMD [ "python", "main.py" ]


