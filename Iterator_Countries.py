import json


class Countries:
    country_page = []

    def __init__(self, path):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        for dictionary in self.json:
            self.country_page.append(dictionary['name']['common'])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.country_page):
            split_country_page = self.country_page[self.index].split(' ')
            word_fusion = '_'.join(split_country_page)
            country_reference = 'https://en.wikipedia.org/wiki/' + word_fusion
            self.index += 1
            return f'{word_fusion}: {country_reference}'
        else:
            raise StopIteration


if __name__ == '__main__':
    output_file = open('countries_with_links.txt', 'w')

    for c in Countries('countries.json'):
        output_file.write(c + '\n')

    output_file.close()


