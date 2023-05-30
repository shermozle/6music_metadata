FROM python:3.9
ADD main.py .
RUN pip install requests datetime
CMD ["python", "./main.py"]