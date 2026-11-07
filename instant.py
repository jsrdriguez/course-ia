from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"


@app.get("/openai", response_class=HTMLResponse)
def open_ai():
    client = OpenAI()
    message = """
¡Estás en un sitio web que acaba de entrar en producción por primera vez!
Por favor, responde con un anuncio entusiasta para dar la bienvenida a los visitantes, explicando que el sitio está en producción por primera vez.
"""
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>¡En vivo al instante!</title></head><body><p>{reply}</p></body></html>"
    return html


# This is important for Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)