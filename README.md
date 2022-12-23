# Inshorts News API [Unofficial]

---

This API is capable of fetching news contents from various sources as gathered by Inshorts ram.

-
## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. all
2. national //Indian News only
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke
12. science
13. automobile

---

## Usage

Make a get request specifying the category of news you want

```
https://inshorts.deta.dev/news?category={category_name}
```

Example - https://inshorts.deta.dev/news?category=science

---

## Response Format

The response JSON Object looks something like this -

```JSON
{
  "category": "technology",
  "data": [
    {
      "author": "Rakesh Kumar",
      "content": "| #BharatBiotech's #nasalvaccine to be part of booster dose, available on CoWIN app from today",
      "date": "23 Deember 2023",
      "imageUrl": "https://static.getinpix.com/public/images/v1/variants/jpg/m/2020/03_mar/15_sun/img_1584273701082_423.jpg",
      "readMoreUrl": "https://twitter.com/timesofindia/status/1606166468697137152 ",
      "time": "11:25 am",
      "title": "\n booster dose ",
    } 
    {
      "author": "Rakesh Kumar",
      "content": "At our eighth #GoogleForIndia, we shared the progress that we, along with our partners have made to bring you more AI-based innovations that are India-first and India-focussed.",
      "date": "19 December 2022",
      "imageUrl": "https://twitter.com/GoogleIndia/status/1604785022011334656/photo/1",
      "readMoreUrl": "https://twitter.com/GoogleIndia/status/1604785022011334656?cxt=HHwWgIDTnbPeq8UsAAAA ",
      "time": "3:55 pm",
      "title": "\nGoogle shares AI-based innovations that are India-first and India-focussed.\n"
    }
    ],
  "success": true
}
```

---

## Setup

Install all dependencies listed in _requirements.txt_ file.

1. To install all dependencies run -

   ```bash
   $ sudo -H pip3 install -r requirements.txt
   ```

2. Start the server

   ```bash
   $ python ram.py
   ```

---


