FROM python:3.10.13-alpine

ADD main.py .
RUN pip install requests beautifulsoup4 python-dotenv

CMD [“python”, “./main.py”] 