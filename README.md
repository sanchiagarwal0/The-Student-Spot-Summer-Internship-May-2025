# Web Scraper with BeautifulSoup - README

## Overview
This Python script scrapes book data from the demo website [books.toscrape.com](http://books.toscrape.com/) and saves the information to a CSV file. The script demonstrates basic web scraping techniques using Python's BeautifulSoup library.

## Features

- **Data Extraction**: Scrapes book titles and prices
- **Error Handling**: Includes comprehensive error handling for network issues and parsing problems
- **CSV Export**: Saves scraped data to an organized CSV file
- **Progress Feedback**: Prints status messages during execution

## How It Works

1. **HTTP Request**: Uses the `requests` library to fetch webpage content
2. **HTML Parsing**: BeautifulSoup parses the HTML structure
3. **Data Extraction**: Finds all book elements and extracts:
   - Book titles (from `h3 > a` tags)
   - Prices (from `price_color` class)
4. **Data Storage**: Writes extracted data to `books_data.csv`

## Requirements

- Python 3.x
- Required packages:
  ```bash
  pip install requests beautifulsoup4
  ```

## Usage

1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python scraper.py
   ```

3. Output will be saved to `books_data.csv`

## Customization

To scrape a different website:
1. Change the `url` variable
2. Update the selectors:
   - Modify `find_all('article', class_='product_pod')` to match container elements
   - Adjust `h3.a['title']` and `price_color` class selectors

## Error Handling

The script handles:
- Network connection issues
- Invalid URLs
- Missing page elements
- File permission problems

## Output Example

The CSV file will contain:
```csv
title,price
"A Light in the Attic","£51.77"
"Tipping the Velvet","£53.74"
...
```

## Ethical Considerations

- Only scrape websites that allow it
- Check `robots.txt` before scraping
- Don't overwhelm servers with rapid requests
- This example uses a demo site specifically for scraping practice

## Troubleshooting

If you encounter errors:
1. Verify package installation
2. Check your internet connection
3. Inspect if the website structure changed
4. Run with `python -v` for verbose output