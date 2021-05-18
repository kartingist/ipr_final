FROM    python:slim
COPY    /ui/ /var/www/tests
WORKDIR /var/www/tests
RUN     pip install --upgrade pip
RUN     pip install -r requirements.txt
CMD ["python", "-m", "pytest", "--reruns=1", "--browser=chrome, firefox", "--html=test_report/ui_report.html", "--self-contained-html", "--color=yes" , "-v", "--tb=short"]
