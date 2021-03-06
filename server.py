from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("analyzing image!!!!")

    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_secrets.json"

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'nyu2.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations


    print('Labels:')
    for label in labels:
        print(label.description)
        print(label.score)



    x = 0
    for label in labels:
        x = x+1
        if label.description == "Road":
            print("This is a road")
        else:
            print("There is no road" + str(x))


    

    print('Done!')
    print('Impact Assesmment Generated Successfully - EIS.a worked!!!!')


    return render_template('index.html', name="Yesmeen")
