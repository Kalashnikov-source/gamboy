from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

#dados
SYMBOLS = ['🍒', '🍋', '🍊', '🍇', '🔔', '⭐', '7️⃣']
PAYOUTS = {
    '7️⃣7️⃣7️⃣': 1000,
    '🍒🍒🍒': 500,
    '🔔🔔🔔': 200
}


@app.route('/api/spin', methods=['POST'])
def spin():
    try:
        data = request.get_json()
        if not data or 'betAmount' not in data:
            return jsonify({'error': 'Dados inválidos'}), 400

        bet_amount = int(data['betAmount'])
        if bet_amount <= 0:
            return jsonify({'error': 'Valor de aposta inválido'}), 400
        
        result = ''.join(random.choices(SYMBOLS, k=3))

        prize = PAYOUTS.get(result, 0) * bet_amount if result in PAYOUTS else 0

        return jsonify({
            'result': result,
            'prize': prize,
            'balance': 1000 - bet_amount + prize
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)