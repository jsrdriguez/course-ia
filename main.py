from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from openai import OpenAI

app = FastAPI()
client = OpenAI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def instant():
    return "Live from production!"


@app.get("/openai", response_class=HTMLResponse)
def open_ai():
    message = """
        ¡Estás en un sitio web que acaba de entrar en producción por primera vez!
        Por favor, responde con un anuncio entusiasta para dar la bienvenida a los visitantes, explicando que el sitio está en producción por primera vez.
    """
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>¡En vivo al instante!</title></head><body><p>{reply}</p></body></html>"
    return html


@app.get("/ideas", response_class=PlainTextResponse)
def open_ai_ideas():
    messages = [{"role": "user", "content": "Genera nuevas ideas de negocio para agentes de IA"}]
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

    return response.choices[0].message.content
