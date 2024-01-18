from flask import Flask
from sqlalchemy import select

from .orm.core import Session, get_session
from .orm import CategotyModel
app = Flask(__name__)

@app.route("/")
def index():
    return "Status: Ok"

@app.get("/category/all")
def get_all_categories(session=Session):
    return (
        session.execute(select(CategotyModel))
        
    ).all()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
