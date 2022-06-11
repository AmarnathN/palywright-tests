FROM mcr.microsoft.com/playwright/python:v1.22.0-focal
copy . /playwright_e2e

WORKDIR /playwright_e2e

RUN pip3 install -r requirements.txt
RUN playwright install

CMD [ "python3","-m","pytest" ]