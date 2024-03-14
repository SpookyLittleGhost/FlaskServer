import json

from flask import Flask, request

app = Flask(__name__)

w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False


@app.route("/", methods=['GET', 'POST'])
def test():
    contents = request.get_json(silent=True)
    print("Message recieved:")
    print(contents)

    global w_pressed
    global a_pressed
    global s_pressed
    global d_pressed

    if 'Key up' in contents:
        print("A key was released: ")
        print(contents['Key up'])

        key = contents['Key up']

        if key == 'w':
            w_pressed = False
            print("ACTION: w_pressed set to FALSE")
        elif key == 'a':
            a_pressed = False
            print("ACTION: a_pressed set to FALSE")
        elif key == 's':
            s_pressed = False
            print("ACTION: s_pressed set to FALSE")
        elif key == 'd':
            d_pressed = False
            print("ACTION: d_pressed set to FALSE")
        else:
            print("Invalid key, nothing done.")

    elif 'Key down' in contents:
        print("A key was pressed: ")
        print(contents['Key down'])

        key = contents['Key down']

        if key == 'w':
            w_pressed = True
            print("ACTION: w_pressed set to TRUE")
        elif key == 'a':
            a_pressed = True
            print("ACTION: a_pressed set to TRUE")
        elif key == 's':
            s_pressed = True
            print("ACTION: s_pressed set to TRUE")
        elif key == 'd':
            d_pressed = True
            print("ACTION: d_pressed set to TRUE")
        else:
            print("Invalid key, nothing done.")

    return "OK!"


if __name__ == '__main__':
    app.run(host='192.168.8.104', port=8000)
