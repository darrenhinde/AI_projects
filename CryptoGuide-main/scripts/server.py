from flask import Flask
#import ../scraping


app = Flask(__name__)

@app.route('/runScrape')
def hello_world():
    #scraping.scrape()
    pass
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)
