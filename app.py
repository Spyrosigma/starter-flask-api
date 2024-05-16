from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


DATA_FILE = 'data.csv'
@app.route('/api', methods=['POST'])
@cross_origin()
def store_data():
    try:
        if request.is_json:
            data = request.get_json()
            if not ('user_email' in data and 'Hiscore' in data):
                return jsonify({'error': 'Missing required keys: user_email, Hiscore'}), 400
                
            username = data['user_email']
            high_score = data['Hiscore']
            
            with open(DATA_FILE, 'a') as f:
                f.write(f"{username},{high_score}\n")

            return jsonify({'message': 'Data stored successfully!'}), 201
        else:
            return jsonify({'error': 'Request content type must be application/json'}), 415
    except Exception as e:
        print(f"Error storing data: {e}")
        return jsonify({'error': 'An error occurred while storing data..'}), 500
    
@app.route('/')
def index():
    return ('<h1 style="color:red; text-align:center; align-items:center;">  &hearts; </h1>')

# if __name__ == '__main__':
#     app.run(debug=True)  
