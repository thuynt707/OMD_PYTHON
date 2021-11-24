from movies import print_all_actors, print_all_movies, print_movie_info


menu = {
    "1": print_all_movies,
    "2": print_all_actors,
    "3": print_movie_info,
    "q": quit
}


def guide():
    print("App quản lý các bộ phim yêu thích")
    print("1. Hiển thị danh sách phim")
    print("2. Hiển thị danh sách diễn viên")
    print("3. Hiển thị bộ phim kèm thông tin diễn viên")
    print("4. Add movie")
    print("q. Thoát chương trình")


if __name__ == "__main__":
    while True:
        guide()

        try:
            choice = input("> ")
            menu[choice]()
        except Exception:
            print("Chọn chức năng phù hợp hoặc 'q' để thoát chương trình")
