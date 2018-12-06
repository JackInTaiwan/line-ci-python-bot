import os
from flask import Flask, request
from handlers import app



if __name__ == "__main__":

    port = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=port)