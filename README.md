## Description
Minimalistic python tool for training your poker ranges. Enter a range and test yourself with given hands.

## Requirement
- python3
- pip install -r requirements.txt

## Usage
- Start the script with "python3 src/app.py" from the root folder of the project 
- Enter the type of range
- Enter the range 
- Enter the number of hands to work on
- Hands will appear, just press 'y' or 'n' for yes/no to indicate if the hand showing on screen is within your range or not/ or 'q' to quit
- See your result

## Run API

You can launch the api with this command :
```sh
uvicorn src.api:app
```
### Docs is available

You can find the documentation of the api here :
http://127.0.0.1:8000/docs
![image](https://user-images.githubusercontent.com/55802491/210111506-ccacc4d5-a2d5-4c1a-bb7a-c4d979aa93e0.png)

## Run test:
```sh
export PYTHONPATH=.
```
```sh
pytest
```
