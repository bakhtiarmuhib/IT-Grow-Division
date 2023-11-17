FROM python:3
COPY . .
RUN pip install -r requerments.txt
EXPOSE 8000
# CMD ["uvicorn","main:app","--reload"]
CMD ["uvicorn", "main:app","--reload","--host=0.0.0.0","--port","8000"]


