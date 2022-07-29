FROM apache/airflow:latest
USER root
# Install any root level apt packages
RUN pip3 install --user --upgrade pip
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# Run remaining commands as the airflow runtime user
USER airflow
# Install airflow related files onto the host
#COPY ./config/airflow.cfg /opt/airflow/airflow.cfg
COPY ./plugins /opt/airflow/plugins
COPY ./dags /data/airflow/dags
COPY ./requirements.txt /opt/airflow/requirements.txt
RUN pip3 install -r /opt/airflow/requirements.txt
USER airflow
