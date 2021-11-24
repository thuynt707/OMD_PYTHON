# Import Flask class và hàm render_template để render file HTML
from flask import Flask, render_template, request, Response, redirect
# flask cho phép tạo 1 máy chủ

# Khởi tạo Flask app và kiểm tra xem nó là main script hay imported
app = Flask(__name__)

movies = {
    "1": {
        "id": 1,
        "title": "Squid Game",
        "year": 2021
    },
    "2": {
        "id": 2,
        "title": "My Name",
        "year": 2020
    }
}


# Chỉ định URL kích hoạt hàm homepage
@app.route("/")
# Hàm homepage() chạy khi đường dẫn khớp với route /
def homepage():
    # Render file HTML và trả về cho trình duyệt
    # Truyền dữ liệu để render
    return render_template("index.html", movies=movies)


@app.route("/about")
def about():
    return render_template("about.html")

# Tham số URL
@app.route("/movies/<movie_id>")
# Tham số trong URL sẽ được truyền cho hàm
def detail(movie_id):
    movie = movies.get(movie_id)
    Response(render_template("movie.html", movie=movie), status=404, mimetype="text/html")
    return render_template("movie.html", movie=movie)

@app.route("/movies", methods=["GET"])
def render_form():
    return render_template("new-movie.html")

@app.route("/movies", methods=["POST"])
def new_movie():
    title = request.form["title"]
    year = request.form["year"]
    movies["3"]={"id":103, "title": title, "year": year}
    return redirect("/", code=302)
    
# Kiểm tra nếu là main script
if __name__ == "__main__":
    # Chạy Flask app
    # Bật debug để restart server mỗi khi có thay đổi trong mã
    app.run(debug=True)
