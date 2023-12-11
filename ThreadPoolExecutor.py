import time
import requests
import concurrent.futures


def get_wiki_page_existence(wiki_url, timeout=10):
    response = requests.get(url=wiki_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "doesn't exist"

    return wiki_url + " " + page_status


wiki_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(30)]

print("Running without threads:")
without_threads_start = time.time()
for url in wiki_urls:
    print(get_wiki_page_existence(wiki_url=url))
print("Without threads time:", time.time() - without_threads_start)

print("Running with threads:")
threaded_start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    the_list = []
    for url in wiki_urls:
        the_list.append(executor.submit(get_wiki_page_existence, wiki_url=url))
    for el in concurrent.futures.as_completed(the_list):
        print(el.result())
print("Running with threads time:", time.time() - threaded_start)
