FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
COPY main.py lib/ ${LAMBDA_TASK_ROOT}

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
