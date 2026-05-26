FROM python

LABEL author="Phat"

WORKDIR /app

COPY linear_sale.pkl /app/linear_sale.pkl
COPY app2.py /app/app2.py


COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8888 

CMD ["uvicorn", "app2:app", "--host", "0.0.0.0", "--port", "8888"]



