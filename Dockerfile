
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install streamlit
CMD ["streamlit", "run", "app_gui.py"]
