from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        signal = data["Signal"]
        
        # Controllo base (qui poi aggiungeremo l'AI)
        if signal in ["buy", "sell"]:
            av_command = f'a=PIGGYBANK b={signal} e=capitaldemo q=1 s=GOLD t=market'
            webhook_url = "https://your-autoview-webhook-url.com"
            requests.post(webhook_url, json={"command": av_command})
            return jsonify({"status": "success", "message": "Ordine inviato"})
        else:
            return jsonify({"status": "rejected", "message": "Segnale non valido"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
