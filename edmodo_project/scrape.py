'''
This file is used to scrape the database
'''
import sqlite3

import requests

conn = sqlite3.connect('db.sqlite3')

# conn.execute('CREATE TABLE "spotlight_owner" ("id" integer NOT NULL PRIMARY KEY, "first_name" varchar(128) NOT NULL, '
#             '"last_name" varchar(128) NOT NULL, "store_url" varchar(200) NOT NULL, "thumb_url" varchar(200) NOT NULL
# , '
#             '"edmodo_url" varchar(200) NOT NULL)')


def scrape_owner(domain):
    data = requests.get("https://spotlight.edmodo.com/api/search/?q=" + domain).json()
    for hit in data["hits"]:
        owner_id = str(hit["_source"]["owner"]["id"])
        print owner_id
        owner_first_name = hit["_source"]["owner"]["first_name"]
        owner_last_name = hit["_source"]["owner"]["last_name"]
        owethumb_url = hit["_source"]["owner"]["thumb_url"]
        store_url = hit["_source"]["owner"]["store_url"]
        edmodo_url = hit["_source"]["owner"]["edmodo_url"]
        try:
            conn.execute(
                "INSERT INTO spotlight_owner (id, first_name, last_name,store_url, thumb_url,edmodo_url) VALUES ("
                + ",".join(
                    [owner_id, "'" + owner_first_name + "'", "'" + owner_last_name + "'", "'" + owethumb_url + "'",
                     "'" + store_url + "'", "'" +
                     edmodo_url]) + "'" + ")")
            conn.commit()
        except sqlite3.IntegrityError:
            pass

def scrape_source(domain):
    data = requests.get("https://spotlight.edmodo.com/api/search/?q=" + domain).json()
    for hit in data["hits"]:
        id = str(hit["_source"]["id"])

        currency = str(hit["_source"]["currency"])
        min_price = str(hit["_source"]["min_price"])
        num_raters = str(hit["_source"]["num_raters"])
        creation_date = str(hit["_source"]["creation_date"])
        avg_rating = str(hit["_source"]["avg_rating"])
        seller_thumb_url = str(hit["_source"]["seller_thumb_url"])
        title = str(hit["_source"]["title"])
        img_path = str(hit["_source"]["img_path"])
        greads_review_url= str(hit["_source"]["greads_review_url"])
        owner_id = str(hit["_source"]["owner"]["id"])


        try:
            conn.execute(
                "INSERT INTO spotlight_source (id, currency, min_price, num_raters, creation_date,avg_rating,seller_thumb_url,title,img_path,greads_review_url,owner_id) VALUES ("
                + ",".join(
                    [id, "'" + currency + "'", "'" + min_price + "'", "'" + num_raters + "'","'" +
                     creation_date + "'", "'" +avg_rating+ "'", "'" +seller_thumb_url+ "'", "'" +title+ "'", "'" +img_path+ "'", "'" +greads_review_url+ "'", "'" +owner_id]) + "'" + ")")
            conn.commit()
        except sqlite3.IntegrityError:
            pass


def scrape_prod(domain):
    data = requests.get("https://spotlight.edmodo.com/api/search/?q=" + domain).json()
    for hit in data["hits"]:
        id = str(hit["_id"])
        index = hit["_index"]
        type = hit["_type"]
        score = hit["_score"]
        source_id = hit["_source"]["id"]
        try:
            conn.execute(
                "INSERT INTO spotlight_prod (id, _index, _type,_score, source_id) VALUES ("
                + ",".join(
                    [id, "'" + index + "'", "'" + type + "'", str(score),
                     str(source_id)])  + ")")
            conn.commit()
        except sqlite3.IntegrityError:
            pass

#1
scrape_owner("math")
scrape_source("math")
scrape_prod("math")

#2
scrape_owner("mitosis")
scrape_source("mitosis")
scrape_prod("mitosis")

#3
scrape_owner("fractions")
scrape_source("fractions")
scrape_prod("fractions")

#4
scrape_owner("english")
scrape_source("english")
scrape_prod("english")

#5
scrape_owner("computer")
scrape_source("computer")
scrape_prod("computer")

#6
scrape_owner("french")
scrape_source("french")
scrape_prod("french")

#7
scrape_owner("history")
scrape_source("history")
scrape_prod("history")

#8
scrape_owner("geometry")
scrape_source("geometry")
scrape_prod("geometry")

#9
scrape_owner("biology")
scrape_source("biology")
scrape_prod("biology")

#11
scrape_owner("chemistry")
scrape_source("chemistry")
scrape_prod("chemistry")

#12
scrape_owner("god")
scrape_source("god")
scrape_prod("god")


#3
scrape_owner("anatomy")
scrape_source("anatomy")
scrape_prod("anatomy")

#4
scrape_owner("programming")
scrape_source("programming")
scrape_prod("programming")

#5
scrape_owner("health")
scrape_source("health")
scrape_prod("health")

#6
scrape_owner("sports")
scrape_source("sports")
scrape_prod("sports")

#7
scrape_owner("web")
scrape_source("web")
scrape_prod("web")

#8
scrape_owner("geometry")
scrape_source("geometry")
scrape_prod("geometry")

#9
scrape_owner("geography")
scrape_source("geography")
scrape_prod("geography")

#11
scrape_owner("economics")
scrape_source("economics")
scrape_prod("economics")

#12
scrape_owner("comics")
scrape_source("comics")
scrape_prod("comics")

scrape_owner("Calculus")
scrape_source("Calculus")
scrape_prod("Calculus")


scrape_owner("Algebra")
scrape_source("Algebra")
scrape_prod("Algebra")





