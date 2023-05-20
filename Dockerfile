FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install Flask
RUN pip install scikit-learn
COPY . .
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

