import api

def main():
    keyword = input("Enter the keyword to search for: ")
    results = api.search_talk_python(keyword)

    print(f'There are {len(results)} topics found')
    for r in results:
        print(f'{r.category} and {r.id}')

if __name__ == '__main__':
    main()