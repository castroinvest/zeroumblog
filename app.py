from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', subdomain='twitter')
def twitter_redirect():
    return redirect('https://twitter.com/ZeroUmBlog')

@app.route('/', subdomain='medium')
def medium_redirect():
    return redirect('https://medium.com/@zeroumblog')

@app.route('/', subdomain='youtube')
def youtube_redirect():
    return redirect('https://www.youtube.com/zeroumblog')

@app.route('/', subdomain='zeroum')
def zeroum_redirect():
    return redirect('https://zeroum.blog/index.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
