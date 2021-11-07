genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    melon_best_album = []
    # 어떤 장르가 노래 조회수 합이 가장 높은지 체크
    top_genre = {}
    for i, genre in enumerate(genre_array):
        if not genre in top_genre:
            top_genre[genre] = play_array[i]
        else:
            top_genre[genre] += play_array[i]

    sort_top_genre = sorted(top_genre.items(), key=lambda x: x[1], reverse=True)
    # 장르 내의 조회수 기준으로 탑 2 선발
    for top_genre in list(dict(sort_top_genre).keys()):
        genre_song = {}
        for i, genre in enumerate(genre_array):
            if genre == top_genre:
                genre_song[i] = play_array[i]
        print(genre_song)
        sort_genre_song = sorted(genre_song.items(), key=lambda x: x[1], reverse=True)
        print(list(dict(sort_genre_song).keys()))
        # print(list(dict(sort_genre_song).keys()))
        # melon_best_album += list(dict(sort_genre_song).keys())[:2]

    # 조회수가 같다면 인덱스 순서 우선

    return melon_best_album


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
# print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))
