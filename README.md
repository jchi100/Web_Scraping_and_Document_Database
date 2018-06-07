# Web_Scraping_and_Document_Database

The project is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Scraping (scrapemars.py):
Use Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Data Source for scraping:
the NASA Mars News Site https://mars.nasa.gov/news/ and collect the latest News Title and Paragragh Text. 
JPL Mars Space Images site and find the image for the current Featured Mars 
On the Mars Weather twitter account https://twitter.com/marswxreport?lang=en 
 Mars Facts webpage https://space-facts.com/mars/ and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
On the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar's hemispheres.

The scraped data is stored in MongoDB

index.html on templates folder is for rendering the scraping results.

Tools: BeautifulSoup, Pandas, and Requests/Splinter, Pymongo, Bootstrap

