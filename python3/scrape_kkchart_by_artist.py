from selenium import webdriver
from selenium.webdriver.common.by import By
from enum import Enum
import os

class ChartType(Enum):
    HOURLY = {'chart_name': '即時榜', 'url': 'https://kma.kkbox.com/charts/hourly'}
    DAILY_NEW = {'chart_name': '新歌日榜', 'url': 'https://kma.kkbox.com/charts/daily/newrelease'}
    DAILY_GENERAL = {'chart_name': '單曲日榜', 'url': 'https://kma.kkbox.com/charts/daily/song'}
    WEEKLY_NEW = {'chart_name': '新歌週榜', 'url': 'https://kma.kkbox.com/charts/weekly/newrelease'}
    WEEKLY_GENERAL = {'chart_name': '單曲週榜', 'url': 'https://kma.kkbox.com/charts/weekly/song'}
    YEARLY_NEW = {'chart_name': '年度單曲累積榜', 'url': 'https://kma.kkbox.com/charts/yearly/newrelease'}

class ChartScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def scrape(self, url):
        self.driver.get(url)
        chart_row_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.charts-list-row')
        hourly_rankings = []
        for chart_row in chart_row_elements:
            rank = chart_row.find_elements(By.CSS_SELECTOR, 'span.charts-list-rank')[0].text
            artist = chart_row.find_elements(By.CSS_SELECTOR, 'span.charts-list-artist')[0].text
            song = chart_row.find_elements(By.CSS_SELECTOR, 'span.charts-list-song')[0].text
            hourly_rankings.append({
                "rank": rank,
                "artist": artist,
                "song": song
            })
        return hourly_rankings

    def close(self):
        self.driver.quit()

class Chart:
    __chart_type = None
    __rankings = None

    def __init__(self, chart_type: ChartType, rankings):
        self.__chart_type = chart_type
        self.__rankings = rankings

    @staticmethod
    def build(chart_type: ChartType, url: str):
        scraper = ChartScraper()
        rankings = scraper.scrape(chart_type.value['url'])
        scraper.close()
        return Chart(chart_type, rankings)

    def find_rankings_by_artist(self, artist):
        rankings = []
        for ranking in self.__rankings:
            if artist in ranking['artist']:
                rankings.append(ranking)
        return rankings

    def show_rankings_by_artist(self, artist):
        rankings = self.find_rankings_by_artist(artist)
        print(f'{artist} has {len(rankings)} songs in chart {self.__chart_type.value["chart_name"]} :')

        for song_in_ranking in rankings:
            print(f'No {song_in_ranking["rank"]} - {song_in_ranking["song"]}')
        return rankings

def print_a_line():
    # Get the width of the terminal
    width = os.get_terminal_size().columns

    # Print a line of dashes that is exactly the width of the terminal
    print('-' * width)

if __name__ == '__main__':
    artist_to_search = input('Please enter the artist you want to search: ')
    print_a_line()

    # Create a list of the ChartType enum members
    chart_types = list(ChartType)

    print("Available chart types:")
    # Display the chart types with their index as the option number
    for i, chart_type in enumerate(chart_types, 1):
        print(f'{i}. {chart_type} - {chart_type.value["chart_name"]} ({chart_type.value["url"]})')
    # Add an option for "Select All"
    print(f'{len(chart_types) + 1}. Select All')
    print_a_line()

    # Get the selected option number
    option_number = int(input('Please enter the number of the chart type you want to search: '))
    print_a_line()

    # Get the selected ChartType
    if option_number == len(chart_types) + 1:
        selected_chart_types = chart_types
    else:
        selected_chart_types = [chart_types[option_number - 1]]

    for selected_chart_type in selected_chart_types:
        chart = Chart.build(selected_chart_type, 'https://kma.kkbox.com/charts/hourly')
        chart.show_rankings_by_artist(artist_to_search)
        print_a_line()