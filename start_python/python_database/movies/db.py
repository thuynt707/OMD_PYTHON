from pymysql import connect, cursors

db_config = {
    "host": "remotemysql.com",
    "user": "QyYiCxuWS2",
    "password": "DIeOFa6xzf",
    "database": "QyYiCxuWS2",
    "cursorclass": cursors.DictCursor
}

con = connect(**db_config)
cur = con.cursor()

def get_movies():
    sql = '''SELECT * FROM movies'''
    cur.execute(sql)

    movies = cur.fetchall()
    return movies

def get_actors():
    sql = '''SELECT * FROM actors'''
    cur.execute(sql)

    actors = cur.fetchall()
    return actors

def find_movie(movie_id):
    sql = '''SELECT * FROM movies WHERE id = %s'''
    cur.execute(sql, movie_id)

    movie = cur.fetchone()
    actors = []

    if movie:
        sql = f'''
        SELECT * 
        FROM actors 
        JOIN movie_actors ON actors.id = movie_actors.actor_id 
        WHERE movie_actors.movie_id = {movie['id']}
        '''
        cur.execute(sql)
        actors = cur.fetchall()
    return movie, actors

def add_movie(title, year):
    sql = '''INSERT INTO movies (title, year) VALUES (%s, %s)'''
    cur.execute(sql, (title, year))
    con.commit()
