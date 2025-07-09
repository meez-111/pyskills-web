from flask import Flask, render_template


app = Flask(__name__)

skills_list = [
    ("Python", "90"),
    ("Flask", "100"),
    ("Django", "50"),
    ("JavaScript", "80"),
    ("HTML/CSS", "100"),
    ("SQL", "70"),
    ("Git", "55"),
    ("Docker", "65"),
    ("Machine Learning", "10"),
    ("Data Analysis", "81"),
]


@app.route("/")
def skills():
    return render_template(
        "skills.html",
        title="My Skills",
        page_head="My skills",
        page_desc="This is My Skills page",
        custom_css="skills",
        skills=skills_list,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Me",
        page_head="Who am I?",
        page_desc="This is the About Me page",
        custom_css="about",
    )


if __name__ == "__main__":
    app.run(port=9000, debug=True)
