FROM python:3.10-slim AS builder

WORKDIR /install
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.10-slim AS runner

WORKDIR /app
COPY --from=builder /install /usr/local
COPY app /app/app
COPY config /app/config
COPY docs /app/docs
COPY scripts /app/scripts

ENV PYTHONUNBUFFERED=1
ENV KV_ENV=production

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
