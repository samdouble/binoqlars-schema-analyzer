FROM public.ecr.aws/lambda/python:3.11

WORKDIR ${LAMBDA_TASK_ROOT}/build
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
COPY lib ./lib

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
