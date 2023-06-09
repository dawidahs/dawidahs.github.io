from flask import Flask, render_template, request, url_for
from openai import ChatCompletion, Image
# assuming you have a module called openai_utils with generate_story and generate_image functions
from openai_utils import generate_story, generate_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        summary = request.form.get('summary')
        characters = request.form.get('characters')
        
        story = generate_story(title, summary, characters)
        image = generate_image(title, summary, characters)
        
        return render_template('index.html', story=story, image=image)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
