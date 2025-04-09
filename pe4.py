import wikipedia
import os
from pathlib import Path
import time
from concurrent.futures import ThreadPoolExecutor

start_time = time.perf_counter()

search_results = wikipedia.search("generative artificial intelligence")
print("Topics related to 'generative artificial intelligence':")
for topic in search_results:
    print(f"- {topic}")

output_dir = "wikipedia_references"

def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        print (page.title)
        print (page.url)
        references = page.references
        filename = f"{page.title.replace('/', '_')}.txt"
        filepath = Path(output_dir) / filename
        os.makedirs(output_dir, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(str(ref).strip() for ref in references if str(ref).strip()))

    except Exception as e:
        print(f"Error processing {topic}: {e}")

all_topics = wikipedia.search("generative artificial intelligence")

with ThreadPoolExecutor(max_workers=5) as executor:
    list(executor.map(wiki_dl_and_save, all_topics))  # Force execution of all threads


end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"\nThis took {execution_time:.2f} seconds")