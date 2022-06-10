# Foody-crawl-dish-searching
## Introduction
    - Project DISH SEARCHING in foody.vn/da-nang
    - Step 1: Crawl data in foody by framework Scrapy
    - Step 2: Insert data from step 1 to Database (MySQL) (scrapy -> API (post) -> MySQL)
    - Step 3: Insert data from Database (MySQL) to Index elasticsearch (MySQL -> API (get) -> Index elasticsearch)
    - Step 4: Run demo and search drink name with sort(match dink name, price ascending, rating descending)
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
    