import numpy as np
from datetime import datetime
import os

from encoder import inference as encoder

import base64
import soundfile as sf

encoder.load_model("./Real_Time_Voice_Cloning/saved_models/default/encoder.pt")

SAMPLE_RATE = 22050
audio = "Record" 

def _compute_embedding(audio):
    embedding = encoder.embed_utterance(encoder.preprocess_wav(audio, SAMPLE_RATE))
    return embedding

def get_embed(encode64):
    gen_file_name = generate_file_name_from_time()
    file_name = "{}.wav".format(gen_file_name)
    
    voice = base64.b64decode(encode64)
    with open(file_name, "wb") as wav_file:
        wav_file.write(voice)   
    
    embed = _compute_embedding(file_name)
      
    #convert embed to base64
    embed64 = base64.b64encode(embed)
    
    os.remove(file_name)
    # embed64_tostr = embed64.decode('utf8').replace("'", '"')
    return embed64

def generate_file_name_from_time():
    dt = datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')
    return dt