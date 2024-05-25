from flask import Flask
from configuration import configure_all

#inicialização
app = Flask(__name__)
#configurações 
configure_all(app)
#execution
app.run(debug=True)
