from movie_api import MovieSearch


def main():
    keyword = input("Please input keyword to search: ")
    read_posts(keyword)


def read_posts(keyword):
    movies_all = MovieSearch()
    response = movies_all.search_by_keyword(keyword)
    print(type(response), response)
    # posts = response.json


    # for p in posts:
    #     title = p.get('title')
    #     director = p.get('director')
    #     print(f'Title: {title} , Director: {director}')

    # for item in posts():
    #     print(item)




if __name__ == '__main__':
    main()
