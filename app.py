from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        if request.method == "POST":
            pn = request.form.get("projectName")
            pa = request.form.get("projectAbout") 
            dis = request.form.get("discord")
            pu = request.form.get("projectUrl") 
            ps = request.form.get("projectSetup") 

            html_content = f"""
<h1 align="center">{pn}</h1>
<p align="center">{pa}</p>
<p align="center">
    <a href="https://discord.com/users/{dis}"><img alt="Discord" src="https://img.shields.io/badge/discord-000000?logo=discord"></a>
    <a href="https://github.com/{pu}"><img alt="Star" src="https://img.shields.io/github/stars/{pu}?logo=github"></a>
    <a href="https://github.com/{pu}"><img alt="Fork" src="https://img.shields.io/github/forks/{pu}"></a>
    <a href="https://gitmoji.dev">
    <img
    src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
    alt="Gitmoji"
  />
    </a>
</p>
<h3 align="center">Run and debug</h3>
<p align="center">

```
{ps}
```

</p>
<h3 align="center">Star history</h3>
<p align="center">
    <img src="https://api.star-history.com/svg?repos={pu}&type=Date">
</p>
"""

            with open("out.md", "w") as filename:
                filename.write(html_content)
                return "OK"
    except Exception as e:
        print(f"An error occurred: {e}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
