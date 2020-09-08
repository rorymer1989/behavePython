# behavePython
Base para behave Python


[project root directory]
|-- [product code packages]
|-- features
|   |-- __init__.py
|   |-- environment.py
|   |-- *.feature
|   `-- steps
|       |-- __init__.py
|       `-- *_steps.py
|
|-- web_source
|   |-- __init__.py
|   |-- web.py
|   `-- web_factory.py
|              
`-- [behave.ini]
`-- [fixtures.py]


Rum:
python -m behave --tags=Test
