from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('fashion_mnist_cnn.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    img = np.array(data['image']).reshape(1, 28, 28, 1)
    img = img.astype('float32') / 255.0
    pred = model.predict(img)
    class_idx = int(np.argmax(pred, axis=1)[0])
    return jsonify({'predicted_class': class_idx})

if __name__ == '__main__':
    app.run(debug=True)