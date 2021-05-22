FROM python:3.8.5
ADD src/ /src
WORKDIR /src
RUN pip install -r requirements.txt
RUN mkdir /log/
CMD [ "python", "./__init__.py" ]