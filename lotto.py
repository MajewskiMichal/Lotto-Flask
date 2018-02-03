from flask import Flask, request, render_template, redirect, url_for
from random import sample


app = Flask(__name__)
app.n = 5
your_nums = []


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        hint = '{} left'.format(app.n)
        try:
            number = int(request.form['number'])
        except ValueError:
            return redirect(url_for('hello_world'))
        if number in range(1, 50) and number not in your_nums:
            your_nums.append(number)
            app.n -= 1
            if app.n < 1:
                app.n = 6
            if len(your_nums) == 6:
                return redirect(url_for('results'))
        elif number not in range(1, 50):
            hint = 'it must be a number in the range of 1-49'
        elif number in your_nums:
            hint = 'you already gave that number'
    else:
        hint = 'Pleas give a number'
    return render_template('form.html', hint=hint)


# page with results
@app.route('/results', methods=['GET'])
def results():

    win_nums = []
    lotto_results = sample(range(1, 50), 6)
    for num in your_nums:
        if num in lotto_results:
            win_nums.append(num)
            if len(win_nums) >= 3:
                return 'Yeeeee! you won, you guessed {}'.format(len(win_nums))
    return "your numbers are {0}, and lotto results are {1}," \
           " you guessed these numbers{2}".format(sorted(your_nums), sorted(lotto_results), sorted(win_nums)), your_nums.clear(),




if __name__ == '__main__':
    app.run(debug=True)
