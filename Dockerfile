FROM python:3.9

MAINTAINER Andriy Andrukhiv <andriy.i.andrukhiv@lpnu.ua>

ADD main.py /
ADD config.yaml /
ADD nginx.log /

RUN python -m pip install --upgrade pip
RUN pip install PyGithub
RUN pip install PyYAML

CMD [ "python", "./main.py" ]
