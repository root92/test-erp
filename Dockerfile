FROM python:3.6
ENV PYTHONUNBUFFERED 1

###############################################################
## install the container
## copy files one by one and split commands to use docker cache
###############################################################

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/requirements.txt
##########################
## install python packages
##########################
RUN pip install --quiet -r requirements.txt

#####################################
## copy everything into the container
#####################################
COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]
