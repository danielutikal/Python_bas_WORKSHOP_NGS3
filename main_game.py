from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return render_template("start.html", min = 0, max = 1001, attempts = 0)
    else:
        min_number = int(request.form.get("min", "0"))
        max_number = int(request.form.get("max", "1001"))
        user_answer = request.form.get("user_answer", "")
        guess = int(request.form.get("guess", 500))
        attempts = int(request.form.get("attempts", "0")) + 1

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you win":
            return render_template("Win.html", guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return render_template("program.html", guess=guess, min=min_number, max=max_number, attempts=attempts)


if __name__ == "__main__":
    app.run(debug=True, port=5010)