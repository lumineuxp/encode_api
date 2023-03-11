from flask import Flask, request
import sys
project_name = "./Real_Time_Voice_Cloning"
sys.path.append(project_name)

import Real_Time_Voice_Cloning.model as model
import base64
import json
from connect import db,Tales

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lumineuxp:hgnuPHIJS9O7@ep-raspy-hall-234246.ap-southeast-1.aws.neon.tech/syn_voice_app"
db.init_app(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api-embed', methods=['POST'])
def get_embed():
    wav_file64= request.json['wav']
    embed64 = model.get_embed(wav_file64) #base64
    ex_syn = model.get_ex_syn(embed64)
    embed64_tostr = embed64.decode('utf8').replace("'", '"')
    syn_tostr = ex_syn.decode('utf8').replace("'", '"')
    
    jsonstr = {
        'embed': embed64_tostr,
        'ex_synthesize_voice' : syn_tostr
        
    } 
   
    json_data = json.dumps(jsonstr)
    return json_data
    

@app.route('/get_tales')
def get_tales():
    tales_db = db.session.execute(db.select(Tales).order_by(Tales.id)).all()
    
    tales = []
    for tale in tales_db :
        
        jsonstr = {
            'tald_id': tale[0].id,
            'cover' : tale[0].cover_img,
            'title' : tale[0].title,
            'story' : tale[0].story
        } 
        tales.append(jsonstr)
     
    json_data = json.dumps(tales)
    return json_data


if __name__ == "__main__":

    app.run(debug = True)

