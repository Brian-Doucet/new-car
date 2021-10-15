# new-car

The time has come for my wife and I to replace our 13 year-old car so I created a project to document that process. After much discussion we've narrowed the selection down to four different car models. For our research we decided to use [cars.com](www.cars.com) to aggregate as much information as we could about price, mileage, make, model, trim options, and dealership reviews.

In order to get the project up and running quickly, I decided to use the [Web Scraper](https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en) chrome extension offered by [webscraper.io](https://webscraper.io/) to quickly scrape the raw data from [cars.com](www.cars.com) with the help of this great blog post by [Scrape Hero](https://www.scrapehero.com/scrape-car-data-from-cars-com/).

The rest of the analysis was done using Python and the work included:
* Aggregating the separate data files. There are four files, one for each car model that we're interested in
* Cleaning and transforming the data for analysis
* Building a dashboard for analysis
