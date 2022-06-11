# playwright-tests
- python3 virtualenv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- playwright install
- python3 -m pytest

# dockerized execution of tests

- docker build -t custom-playwright . 
- docker run -it --net=host -e URL='http://54.196.37.255:3000/' custom-playwright



