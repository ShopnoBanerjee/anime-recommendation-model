from flask import Flask,redirect,url_for,request,render_template
import random

import recommender_script as r
from recommender_script import cosine_sim
from recommender_script import df
from recommender_script import recommendation


# print(df)
# print(cosine_sim)

# def recom_2(t1,t2,t3,t4,t5):
#     l1=recommendation(t1)
#     l2=recommendation(t2)
#     l3=recommendation(t3)
#     l4=recommendation(t4)
#     l5=recommendation(t5)
    
#     for i in range(0,4): 
#         lr=l1[i]+l2[i]+l3[i]+l4[i]+l5[i]
    
#     return lr

app = Flask(__name__)

@app.route('/')
def index():
    random_titles = random.sample(df['title'].tolist(), min(10, len(df)))
    return render_template('index.html', titles=random_titles)

@app.route('/submit', methods=['POST','GET'])
def submit():
    # Get the selected movie titles from the form
    if request.method == 'POST':
        selected_title = request.form.get('movie')
        # print(selected_title)
        # print(type(selected_title))
        # recs=recommendation(selected_title)
        return redirect(url_for("result",selected_title=selected_title))
        # return render_template('result.html',recs=list)

    else:
    # Redirect to the home page
        return redirect('/')

@app.route('/result/<selected_title>')
def result(selected_title):
    recs=recommendation(selected_title)
    return render_template('result.html',recs=recs,selected_title=selected_title)

if __name__ == '__main__':
    app.run(debug=True)