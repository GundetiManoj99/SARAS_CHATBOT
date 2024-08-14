from flask import Flask, render_template, request, jsonify
import cohere

# Initialize Cohere Client
cohere_client = cohere.Client('5oswWYIjJ1p0d2cBrRiO8SiDbTv7Iw9A4icy5mrt')  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')

    # Generate a response using Cohere
    response = cohere_client.generate(
        model='command-xlarge-nightly',  # or another model
        prompt=user_input,
        max_tokens=50,
        temperature=0.7,
        stop_sequences=["\n"]
    )

    return jsonify({'response': response.generations[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
