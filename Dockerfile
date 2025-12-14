FROM python:3.11.14-alpine3.23

WORKDIR /TheFortress

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN addgroup -S customgroup && adduser -S customuser -G customgroup

USER customuser

ENTRYPOINT [ "flask", "--app", "app", "run"]
CMD ["--host=0.0.0.0"]
