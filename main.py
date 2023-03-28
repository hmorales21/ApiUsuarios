#importa
import pandas as pd
import numpy as np
import pickle

from google.cloud import storage
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

#Cree una nuevas credenciales para acceder a google storage, no me dejó con las otras credenciales
#storage_client = storage.Client.from_service_account_json('./creds/delorean-data-consulting-805bd95798d3.json')
storage_client = storage.Client()
bucket = storage_client.bucket('metadata_bucket1')
#blob = bucket.blob('modelos/modelo_usuarios.pickle')
#pickle_in = blob.download_as_string()

#modeloUsuarios =  pickle.loads(pickle_in)

#usuario entrada

#res[['user_id', 'gmap_id', 'rating']]
usuariosIn = [
            {'usr_id':'','gmap_id':'', 'rating':''}
            ]
usuariosOut =[
            {'usr_id':'1.169836652e','gmap_id':'0x808f7c0d0893e7cd:0x119e50948f09dd69'}
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predice")
def modelo_predice():
    print(usuariosOut[0])
    return usuariosOut[0]

#if __name__ == 'main':
#    app.run()
