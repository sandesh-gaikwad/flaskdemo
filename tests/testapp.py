import requests
import json

URL = "http://0.0.0.0:5000/api/v1.0/task"
PASS=0
FAIL=0
TOTAL = 0
def verifyGet():
    global PASS
    global FAIL
    global TOTAL
    TOTAL = TOTAL + 1
    res = requests.get(URL)
    msg = json.loads(res.text.encode())
    if (msg['Message'] == "Inside get method"):
            PASS = PASS + 1
    else:
            FAIL = FAIL + 1

def verifyPost():
    global PASS
    global FAIL
    global TOTAL
    TOTAL = TOTAL + 1
    res = requests.post(URL)
    msg = json.loads(res.text.encode())
    if (msg['Message'] == "Inside post method"):
        PASS = PASS + 1
    else:
        FAIL = FAIL + 1


def verifyPut():
    global PASS
    global FAIL
    global TOTAL
    TOTAL = TOTAL + 1
    res = requests.put(URL)
    msg = json.loads(res.text.encode())
    if (msg['Message'] == 'Inside put method'):
        PASS = PASS + 1
    else:
        FAIL = FAIL + 1


def verifyDelete():
    global PASS
    global FAIL
    global TOTAL
    TOTAL = TOTAL + 1
    res = requests.delete(URL)
    msg = json.loads(res.text.encode())
    if (msg['Message'] == 'Inside delete method'):
        PASS = PASS + 1
    else:
        FAIL = FAIL + 1


if __name__ == '__main__':
    verifyGet()
    verifyPost()
    verifyPut()
    verifyDelete()
    print("PASS : " + str(PASS))
    print("FAIL : " + str(FAIL))
    print("TOTAL : " + str(TOTAL))
