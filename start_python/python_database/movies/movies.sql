CREATE DATABASE IF NOT EXISTS movies;

USE movies;

CREATE TABLE IF NOT EXISTS movies (
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL
    ) Engine=InnoDB AUTO_INCREMENT=101;

CREATE TABLE IF NOT EXISTS actors (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    bio VARCHAR(1000)
    ) Engine=InnoDB AUTO_INCREMENT=101;
    
CREATE TABLE IF NOT EXISTS movie_actors (
	movie_id INT,
    actor_id INT,
    PRIMARY KEY(movie_id, actor_id),
    FOREIGN KEY movie (movie_id) REFERENCES movies (id),
    FOREIGN KEY actor (actor_id) REFERENCES actors (id)
    ) Engine=InnoDB;
    
INSERT INTO movies (title, year)
VALUES ('The Good Doctor', 2020),
		('My Name', 2021),
        ('Vagabone', 2019),
        ('Outside The Wire', 2021),
        ('Aquaman', 2018);
        
INSERT INTO actors(name, bio)
VALUES ('Freddie Highmore', 'Alfred Thomas "Freddie" Highmore là một diễn viên trẻ gốc Anh. Highmore có một sự nghiệp nhiều triển vọng và thành công với nhiều vai diễn và giải thưởng dành cho diễn viên trẻ'),
		('Antonia Thomas', 'Antonia Laura Thomas là một nữ diễn viên và ca sĩ người Anh. Cô được biết đến với các vai diễn Alisha Daniels trong loạt phim hài-chính kịch E4 Misfits, Evie trong loạt phim hài Lovesick của Kênh 4 / Netflix và Tiến sĩ Claire Browne trong bộ phim truyền hình ABC The Good Doctor.'),
        ('Lee Sung-gi', 'Lee Seung Gi là một ca sĩ, diễn viên, dẫn chương trình và ngôi sao giải trí người Hàn Quốc. Được biết đến với cái tên "Hoàng tử Ballad", anh sở hữu số lượng lớn các bài hit như "Because You\'re My Woman", "Delete", "Will You Marry Me", and "Return".'),
        ('Bae Suzy', 'Bae Soo-ji, thường được biết đến với nghệ danh Bae Suzy, là một nữ ca sĩ kiêm diễn viên người Hàn Quốc. Cô là cựu thành viên của nhóm nhạc nữ Miss A thuộc JYP Entertainment, còn được biết đến với biệt hiệu "Tình đầu quốc dân" ở Hàn Quốc. Sau khi kết thúc hợp đồng với JYP, Suzy gia nhập Management SOOP.'),
        ('Han So-hee', 'Han So-hee là nữ diễn viên người Hàn Quốc. Cô đóng vai chính trong các phim truyền hình như Money Flower, Lang quân 100 ngày, My Name và vai phụ trong Viên đá bí ẩn. Cô trở nên nổi tiếng sau khi thể hiện nhân vật Yeo Da-kyung trong bộ phim truyền hình Thế giới hôn nhân'),
        ('Park Hee-soon', 'Park Hee-soon là một diễn viên Hàn Quốc. Anh tốt nghiệp với bằng Sân khấu tại Học viện Nghệ thuật Seoul, và là thành viên của Mokwha Repertory Company từ năm 1990 đến năm 2001.'),
        ('Anthony Mackie', 'Anthony Dwane Mackie là một diễn viên người Mỹ. Anh được biết đến với vai Falcon thuộc MCU.'),
        ('Damson Idris', 'Damson Idris là một diễn viên người Anh. Anh hiện đóng vai chính trong bộ phim tội phạm Snowfall của John Singleton, ra mắt ngày 5 tháng 7 năm 2017 trên FX. Anh ấy đã đóng vai đồng chính trong bộ phim hành động khoa học viễn tưởng của Netflix là Outside the Wire.'),
        ('Jason Momoa', 'Joseph Jason Namakaeha Momoa là nam diễn viên, đạo diễn và nhà sản xuất phim người Mỹ. Jason Momoa nổi tiếng với các vai diễn siêu anh hùng trong vũ trụ DC Mở rộng DC Extended Universe, bắt đầu từ năm 2016 với vai thủy thần Aquaman trong Batman v Superman: Dawn of Justice, Justice League và Aquaman.'),
        ('Amber Heard', 'Amber Laura Heard là một nữ diễn viên kiêm người m
        ẫu Mỹ thành danh qua các vai diễn trong "Never Back Down", "Pineapple Express", phim hành động Drive Angry đóng cùng Nicolas Cage, The Informers, The Stepfather, Zombieland và The Joneses và gần đây nhất là Aquaman.');
        
INSERT INTO movie_actors (movie_id, actor_id)
VALUE (101, 101), (101, 102), (102, 105), (102, 106), (103, 103), (103, 104), (104, 107), (104, 108), (105, 109), (105, 110);