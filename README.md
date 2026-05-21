# Website Keyword Monitor

A simple Python tool for checking whether specific keywords appear on selected websites.

This script visits a list of websites, checks if the target keyword exists on each page, and saves the results to a CSV file.

## Features

- Check multiple websites
- Search for specific keywords
- Save results to a CSV file
- Record check time
- Handle basic website errors

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Use

1. Open `main.py`
2. Edit the website URLs and keywords inside the `targets` list:

```python
targets = [
    {
        "url": "https://www.python.org",
        "keyword": "Python"
    },
    {
        "url": "https://github.com",
        "keyword": "GitHub"
    }
]
```

3. Run the script:

```bash
python main.py
```

4. The results will be saved as:

```text
keyword_results.csv
```

## Output Columns

The output CSV file includes:

- url
- keyword
- keyword_found
- status
- checked_at

## What This Project Demonstrates

This project shows basic skills in:

- Python automation
- Website monitoring
- Requests
- BeautifulSoup
- CSV export
- Error handling
- GitHub project workflow

## Notes

This tool is for simple public webpage keyword checking.  
It does not log in to websites, bypass restrictions, or scrape private data.
