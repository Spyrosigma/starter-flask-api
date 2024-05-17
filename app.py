from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from supabase import create_client
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)
CORS(app)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

cross_origin()
@app.route('/api', methods=['POST'])
def save_data():
    data = request.json
    user_email = data.get('user_email')
    Hiscore = data.get('Hiscore')

    userdata = {"user_email": user_email, "Hiscore": Hiscore}
    data = supabase.table("demo").insert(userdata).execute()

    if data is None:
        return jsonify({"message": "Failed to save data"}), 500
    else:
        return jsonify({"message": "Data saved successfully"}), 201


cross_origin()
@app.route('/')
def home():
    return ('''
            <img src="/static/logo.png" alt="GFG" style="width: 80%; height: auto; display: block;
      margin: 200px auto;">
        
            <footer style="position: absolute;
            bottom: 0;
            width: 99vw;
        
            color: green;       
            font-size:5vh;
            padding: 10px 0px 10px 0px;   
            text-align: center;"> 
            Made with <span style="color:red;"> &hearts; </span> ~ NAMDEV </footer>
            ''')
    
cross_origin
@app.route('/api')
def api():
    return ('''
        <h1 style="font-size:50px;"> Kya bhai? Hain? </h1>
        
            <div class="tenor-gif-embed" data-postid="17088362" data-share-method="host" data-aspect-ratio="1.34454" data-width="50%">
            
            <a href="https://tenor.com/view/dwayne-johnson-the-rock-wwe-world-wrestling-entertainment-wrestler-gif-17088362">
            Dwayne Johnson The Rock GIF</a>from 
            <a href="https://tenor.com/search/dwayne+johnson-gifs">Dwayne Johnson GIFs</a>
            
            </div> 

            <footer style="position: absolute;
            bottom: 0;
            width: 99vw;
        
            color: green;       
            font-size:5vh;
            padding: 10px 0px 10px 0px;   
            text-align: center;"> 
            Made with <span style="color:red;"> &hearts; </span> ~ NAMDEV </footer>
            
            <script type="text/javascript" async src="https://tenor.com/embed.js">
            </script>
    ''')

if __name__ == '__main__':
    app.run(debug=True)

    