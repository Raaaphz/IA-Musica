from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import uvicorn

# Inicializar o app FastAPI
app = FastAPI()

# Carregar o modelo com joblib
modelo = joblib.load('app/models/music_geral.robson')

# Modelo de dados para receber o texto
class TextoEntrada(BaseModel):
    texto: str

@app.post("/api/v1/ai/music/prediction")
async def realizar_predicao(dados: TextoEntrada):
    try:
        # Realizar a predição
        predicao = modelo.predict([dados.texto])
        # Retornar a predição em formato JSON
        return {"predicao": predicao[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Código para rodar o servidor com uvicorn diretamente no script
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)