from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Page d'accueil basique
@app.route('/')
def home():
    return "<h1>Blue Team API - Active</h1><p>Endpoint disponible : /api/analyze?text=votre_mot_de_passe</p>"

# Endpoint REST qui simule un outil d'analyse
@app.route('/api/analyze', methods=['GET'])
def analyze_password():
    # On récupère le texte envoyé dans l'URL
    text = request.args.get('text', '')
    
    if not text:
        return jsonify({"erreur": "Veuillez fournir un texte via le paramètre ?text="}), 400
    
    # Traitement orienté sécurité : Génération de l'empreinte SHA-256
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    length = len(text)
    
    # Logique simple d'évaluation
    if length < 8:
        strength = "Critique : Trop court"
    elif length >= 12:
        strength = "Robuste"
    else:
        strength = "Moyen"

    # Réponse au format JSON
    return jsonify({
        "cible": text,
        "longueur": length,
        "niveau_securite": strength,
        "empreinte_sha256": sha256_hash
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)