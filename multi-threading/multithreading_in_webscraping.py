import threading
import requests
from bs4 import BeautifulSoup

langchain_intro_url = "https://python.langchain.com/docs/introduction/"
langchain_concepts_url = "https://python.langchain.com/docs/concepts/"
langchain_tutorials_url = "https://python.langchain.com/docs/tutorials/"

urls = [langchain_intro_url, langchain_concepts_url, langchain_tutorials_url]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"length of conent from {url}: {len(soup.text)} characters")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished execution.")