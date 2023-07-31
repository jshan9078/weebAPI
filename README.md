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

## More Info: How does it work?

### Webscraping
As mentioned above, the API is inherently a web scraper that grabs data from [animepahe](https://animepahe.ru/). None of the content served through the API is owned or produced by me. I experimented with methods employing *beautifulsoup4* and *selenium*, but found that simply using RegEx on the raw html from the frontend of the web pages worked more effeciently. These frontends are obtained by using *requests sessions*.

### Bypassing DDoS-Guard

Animepahe employs a DDoS-Guard guard challenge. This is not of concern if one is hosting the API locally, but if it is being hosted on a service such as *AWS* or *Google Cloud Run*, the the python requests library fails to fetch the frontend of animepahe. To solve this, cookies and headers can be used as shown in the various functions inside the [weebAPI folder](https://github.com/JonnyACCI/weebAPI/tree/main/weebAPI). Credit for the function used to retrieve cookies goes to [gallery-dl](https://github.com/mikf/gallery-dl)

### Decrypting the Intermediary Page
*When one tries to download an episode off animepahe (after choosing the desired download option), they will redirected to a `pahe.win` page.*

![](https://cdn.discordapp.com/attachments/928022919337103393/1135459680689332284/image.png)
*For example, clicking the 1080p option of this episode, will take me to the following `pahe.win` page*

![](https://cdn.discordapp.com/attachments/928022919337103393/1135460137201578044/image.png)
*From here, clicking continue will take me to the following intermediary site on `kwix.cx`*

![](https://cdn.discordapp.com/attachments/928022919337103393/1135460951630544896/image.png)

**To get to the `kwix.cx` page, decryption must be used on the `pahe.win` site to get a token. Credit for the [decryption functions](https://github.com/JonnyACCI/weebAPI/blob/main/weebAPI/downloadmanager/decrypter.py) used goes to [animdl](https://github.com/justfoolingaround/animdl)**

### Getting the Download Link for A File
**A download link can be obtained for a particular download option of a specific episode. To get this link, a POST request is made to the kwix.cx page. The location of the response is the download link.**
