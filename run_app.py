from pyngrok import ngrok
import os

# Start an ngrok tunnel
public_url = ngrok.connect(port=4040)
print("Streamlit app is available at:", https://darling-giraffe-splendid.ngrok-free.app)

# Run the Streamlit app
os.system("streamlit run app.py")
