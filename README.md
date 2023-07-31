# weebAPI
**A RESTful API made with FastAPI to obtain anime data from [animepahe](https://animepahe.ru/)**

### Technologies Used
- Python requests library + RegEx for web scraping
- FastAPI to create the RESTful API
- Docker to containerize the application
- Google Cloud Run to host the API

## User Guide
**The API is hosted here [`weeb-api-7nrxlzoyjq-uc.a.run.app`](https://weeb-api-7nrxlzoyjq-uc.a.run.app)**

**To view the documentation for the API, simply go to [`weeb-api-7nrxlzoyjq-uc.a.run.app/docs`](https://weeb-api-7nrxlzoyjq-uc.a.run.app/docs)**

**The containerized images for every version are posted on Docker Hub here [`https://hub.docker.com/r/jshan9078/weeb-api/tags`](https://hub.docker.com/r/jshan9078/weeb-api/tags)**

### Examples
-----
**Note:** You can test the endpoints of the API from the documentation page linked above. Alternatively, simply construct a URL as follows.

> #### get_search_results
**Use this endpoint to obtain search results for a desired anime**

`https://weeb-api-7nrxlzoyjq-uc.a.run.app/get_search_results/naruto` returns the following JSON data

![](https://cdn.discordapp.com/attachments/928022919337103393/1135464972726587402/image.png)

> #### get_full_data
**Use this endpoint to obtain complete data for an anime series.**

*siteLink refers to the identifier `https://animepahe.ru/anime/{identifier}`*

`https://weeb-api-7nrxlzoyjq-uc.a.run.app/get_full_data/90c9fc20-0c15-cee2-0d03-6f1fb998cec3` returns the following JSON data

![](https://cdn.discordapp.com/attachments/928022919337103393/1135465749264216164/image.png)

> #### get_episode
**Use this endpoint to obtain complete data for a particular episode.**

*siteLink refers to the identifier `https://animepahe.ru/anime/{identifier}`*

`https://weeb-api-7nrxlzoyjq-uc.a.run.app/get_episode/90c9fc20-0c15-cee2-0d03-6f1fb998cec3/1` returns the following JSON data

![](https://media.discordapp.net/attachments/928022919337103393/1135472403053563955/image.png?width=1440&height=90)

> #### get_download_options
**Use this endpoint to obtain the download options for a particular episode.**

*episodeLink refers to the whole episode link*

`https://weeb-api-7nrxlzoyjq-uc.a.run.app/get_download_options/https://animepahe.ru/play/f1af0e39-d51f-34e4-decb-761d18d39729/d9ad6a27917400b6582742c55b1e39be76d234524db0789302c87bc4f9e827dd` returns the following JSON data

![](https://cdn.discordapp.com/attachments/928022919337103393/1135473723500134480/image.png)

> #### get_download_link
**Use this endpoint to obtain the download link**

*intermediaryPageLink refers to the `pahe.win` link*

`https://weeb-api-7nrxlzoyjq-uc.a.run.app/get_download_link/https://pahe.win/NMZna` returns the following string data

![](https://cdn.discordapp.com/attachments/928022919337103393/1135474860278165565/image.png)

## More Info: How does it work?

### Webscraping
As mentioned above, the API is inherently a web scraper that grabs data from [animepahe](https://animepahe.ru/). None of the content served through the API is owned or produced by me. I experimented with methods employing *beautifulsoup4* and *selenium*, but found that simply using RegEx on the raw html from the frontend of the web pages worked more effeciently. These frontends are obtained by using *requests sessions*.

### Bypassing DDoS-Guard

Animepahe employs a DDoS-Guard guard challenge. This is not of concern if one is hosting the API locally, but if it is being hosted on a service such as *AWS* or *Google Cloud Run*, the the python requests library fails to fetch the frontend of animepahe. To solve this, cookies and User-Agent HTTP headers can be used as shown in the various functions inside the [weebAPI folder](https://github.com/JonnyACCI/weebAPI/tree/main/weebAPI). Credit for the function used to retrieve cookies goes to [gallery-dl](https://github.com/mikf/gallery-dl).

### Decrypting the Intermediary Page
*When one tries to download an episode off animepahe, there are options.

![](https://cdn.discordapp.com/attachments/928022919337103393/1135459680689332284/image.png)
*For example, clicking the 1080p option of this episode, will take me to this `pahe.win` page*.

![](https://cdn.discordapp.com/attachments/928022919337103393/1135460137201578044/image.png)
*From here, clicking continue will take me to the following page on `kwix.cx`*

![](https://cdn.discordapp.com/attachments/928022919337103393/1135460951630544896/image.png)

**To get to the `kwix.cx` page, decryption must be used on the `pahe.win` site to get a token. Credit for the [decryption functions](https://github.com/JonnyACCI/weebAPI/blob/main/weebAPI/downloadmanager/decrypter.py) used goes to [animdl](https://github.com/justfoolingaround/animdl)**

### Getting the Download Link for A File
**A download link can be obtained for a particular download option of a specific episode. To get this link, a POST request is made to the kwix.cx page. The location of the response is the download link.**
