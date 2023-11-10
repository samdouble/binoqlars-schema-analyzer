FROM public.ecr.aws/lambda/python:3.11

WORKDIR ${LAMBDA_TASK_ROOT}/build
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY main.py .
COPY src ./src

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
