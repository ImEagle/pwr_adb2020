FROM python:3.8.0-slim-buster

WORKDIR /usr/pwr_adb/

COPY docker/entrypoint.sh /usr/pwr_adb/entrypoint.sh

COPY ./main/requirements.txt /usr/pwr_adb/requirements.txt
RUN pip install -r /usr/pwr_adb/requirements.txt

COPY ./main/ /usr/pwr_adb/

ENTRYPOINT ["/usr/pwr_adb/entrypoint.sh"]
