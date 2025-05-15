from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1 style="color: #28a745;">✅ Flask App is Running Successfully!</h1>
        <p style="color: #333333; font-size: 18px;">
            Welcome to your <strong>Azure-deployed Flask web application</strong>.
        </p>
        <p style="color: #555555; font-size: 16px;">
            This confirms your app is <span style="color: #007bff;">up and responding</span> to requests.
        </p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
