from flask import Flask, request, redirect, url_for, render_template, json, render_template_string, jsonify
from werkzeug.datastructures import ImmutableMultiDict

path = '/home/rtc/Desktop/rover-sensor-integration/rover-sensor-integration/'

app = Flask(__name__, template_folder=path + 'templates')

@app.route('/', methods=['GET', 'POST'])
def control_panel():
    # print('request.form:', request.form)
    responses = request.form.to_dict(flat=False)
    print(responses)
    
    if request.method == 'POST':
        # if request.form.get('button') == 'button-play':
        #     print("play button pressed")

        # elif request.form.get('button') == 'button-exit':
        #     print("exit button pressed")

        if request.form.get('slide'):
            volume = request.form.get('slide')
            print('volume:', volume)
            # return jsonify({'volume': volume})
            # return json.dumps({'volume': volume})

        elif request.form.get('slide2'):
            volume2 = request.form.get('slide2')
            print('volume2:', volume2)

    # print('render')
    return render_template('slider.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
