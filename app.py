from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("Testing custome exception.")
    except Exception as e:
        housing_exc=HousingException(e,sys)
        logging.info(housing_exc.error_message)
    logging.info("Testing logging module")
    return "Starting ML Project. CI/CD pipeline established!"

if __name__ == '__main__':
    app.run(debug=True)