FROM python:3.10.2-slim

ENV PYTHONBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock", "./"]

RUN pipenv install --deploy --system && \
	rm -rf /root/.cache

COPY ["*.py", "churn-model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"]
