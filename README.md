# KKBox Chart Scraper

## Introduction

This Python script scrapes various charts from KKBox, a popular music streaming service in Asia, and provide a feature of search-by-artist to list all songs in charts that match.

- Chart settings are configured to default to the **Traditional Chinese** interface for the **Taiwan** region.
- The *find-by-artist* function is done by finding artist name *containing* the given input words.
- The script uses **Selenium** and **Chrome Browser Driver** to interact with the website and extract the chart data.

## Installation

### I. Python3 Environment

Installed the latest version of Python 3.
* You can download it from [here](https://www.python.org/downloads/).

### II. Install Chrome Browser

Install Chrome browser if absent.
* You can download it from [here](https://www.google.com/intl/zh-TW/chrome/).

### III. Install Browser Driver for Chrome

1. Check your Chrome browser version
2. Install the capatible version of Browser Driver to your environment
    * You can download it from [here](https://chromedriver.chromium.org/downloads).
3. After installation, make sure to add it to your system's PATH.

### IV. Installing Required Python Libraries

To install the required Python libraries, follow these steps:

(MacOS/Windows)

```
$ pip install selenium
```


## Execution

### Commands

Option 1 - In terminal, run python file directly
```
kkbox_chart_scraper $ python3 python3/scrape_kkchart_by_artist.py 
```

Option 2 - In terminal, run the entrypoint-alike shell script
```
kkbox_chart_scraper $ ./sh/run_scrape_kkchart_by_artist.sh
```

Option 3 - In your desktop, go to the project's `sh` folder and *double click* the `run_scrape_kkchart_by_artist.sh` file.


### Example

```
$ python3 scrape_kkchart_by_artist.py 
Please enter the artist you want to search: Tanya
-------------------------------------------------------------------------------
Available chart types:
1. ChartType.HOURLY - 即時榜 (https://kma.kkbox.com/charts/hourly)
2. ChartType.DAILY_NEW - 新歌日榜 (https://kma.kkbox.com/charts/daily/newrelease)
3. ChartType.DAILY_GENERAL - 單曲日榜 (https://kma.kkbox.com/charts/daily/song)
4. ChartType.WEEKLY_NEW - 新歌週榜 (https://kma.kkbox.com/charts/weekly/newrelease)
5. ChartType.WEEKLY_GENERAL - 單曲週榜 (https://kma.kkbox.com/charts/weekly/song)
6. ChartType.YEARLY_NEW - 年度單曲累積榜 (https://kma.kkbox.com/charts/yearly/newrelease)
7. Select All
-------------------------------------------------------------------------------
Please enter the number of the chart type you want to search: 1
-------------------------------------------------------------------------------
Tanya has 3 songs in chart 即時榜 :
No 9 - 善良的我們
No 53 - 芬蘭距離
No 98 - Rebecca
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
$ 
```

## License
This project is licensed under the terms of the custom license. See the [LICENSE](LICENSE) file for license rights and limitations.