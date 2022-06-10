# Foody-crawl-dish-searching
## STEP BY STEP:
    - pip3 install -r requirements.txt
    - docker build --tag (image name) in folder fastapi and Flask_web
    - docker-compose up
    - cmd: "cd Crawl" and "scrapy crawl foody"
    - File log to save in folder crawl
    - The crawl in complete, cmd "cd Elasticsearch" and "python3 insert_data.py"
    - Final: demo in the http://127.0.0.1:5000/
## TODO:
    - Build AIRFLOW Services Process Management
    