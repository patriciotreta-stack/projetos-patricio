from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    
    if request.method == 'POST':
        cidade = request.form.get('cidade')
        api_key = "d0d059849b3d4f1c2b9a6d8a221e046d"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&appid={api_key}&lang=pt_br"

        try:
            response = requests.get(url).json()

            if response.get('cod') == 200:
    
               condicao_principal = response['weather'][0]['main'].lower()
    
               weather_data = {
                   'cidade': cidade,
                   'temp': response['main']['temp'],
                   'desc': response['weather'][0]['description'],
                   'icon': response['weather'][0]['icon'],
                   'classe_clima': condicao_principal 
            }
        except Exception as e:
            weather_data = {'erro': 'Erro ao conectar com o serviço de clima.'}

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)