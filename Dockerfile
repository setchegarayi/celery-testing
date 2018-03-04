FROM python:3.6
COPY . /app
RUN cd /app && pip install -r requirements.txt
EXPOSE 8000
#RUN cd /tmp/app && chmod +x /tmp/run.sh
#RUN cd /tmp/app
#CMD ./run.sh
#CMD celery -A tasks worker -l info -Q firstq
#CMD cd /app && celery -A tasks beat
CMD /bin/bash
