FROM public.ecr.aws/lambda/python:3.11

WORKDIR ${LAMBDA_TASK_ROOT}/build
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install
COPY main.py .
COPY src ./src

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
