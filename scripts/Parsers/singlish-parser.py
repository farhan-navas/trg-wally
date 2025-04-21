import httpx
import json
import re
from selectolax.parser import HTMLParser
from urllib.parse import quote  # Add this import


def retrieveWordCategory(baseUrl):
    pages = ["0-9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    singlishDictionary = []

    for page in pages:
        html = getCategoryHTML(baseUrl, page)
        details = retrieveWords(baseUrl, html)
        singlishDictionary.append({
            "Prefix": page,
            "Words": details
        })

    with open("../../data/raw/singlish/singlishDicitionary.json", "w") as f:
        json.dump(singlishDictionary, f, indent=4)



def getCategoryHTML(baseUrl, letter):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

    # Get initial page
    resp = httpx.get(baseUrl + "letter?l=" + letter, headers=header)
    html = HTMLParser(resp.text)

    return html

def getWordHTML(baseUrl, word):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

    # Get initial page
    resp = httpx.get(baseUrl + "?q=" + word, headers=header)
    html = HTMLParser(resp.text)

    return html

def extractText(html, selection):
    try:
        raw_text = html.css_first(selection).text()
        cleaned = raw_text.strip()
        cleaned = re.sub(r'\n+', ' ', cleaned)  
        cleaned = re.sub(r'\s{2,}', ' ', cleaned)  
        return cleaned
    except AttributeError:
        return None

def extractList(html, sectionName):
    detailArray = []
    for detail_div in html.css('div.details'):
        heading = detail_div.css_first('h3')
        if heading and sectionName.lower() in heading.text().lower():
            detailArray = [a.text(strip=True) for a in detail_div.css('a.nyms-list')]

    if len(detailArray) == 0:
        return None
    else:
        return detailArray

def parseWord(html):
    # Creat a dicitionary to hold the words and defintion
    word = {
        "Word": extractText(html, "div.word-box"),
        "English Translation": extractText(html, "div.ety-container"),
        "Definition": extractText(html, "li.definition"),
        "Example": extractText(html, "p.word-example"),
        "Related": extractList(html, "related"),
        "Categories": extractList(html, "categories")    
        }

    return word

def retrieveWords(baseUrl, html):
    words = html.css("a.list-link")  # Fixed selector
    wordlist = []
    
    for word_element in words:
        # Clean text and encode
        raw_word = word_element.text(strip=True)
        encoded_word = quote(raw_word)  # Proper URL encoding
        
        # Get word page
        newhtml = getWordHTML(baseUrl, encoded_word)
        if newhtml:  # Check if HTML is valid
            wordlist.append(parseWord(newhtml))
    
    return wordlist




if __name__ == "__main__":
    baseUrl = "https://singlishdict.app/"
    retrieveWordCategory(baseUrl)