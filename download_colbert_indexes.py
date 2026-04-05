import os, urllib.request, tarfile

def download_and_extract(url, out_dir):
    filename = url.split('/')[-1]
    os.makedirs(out_dir, exist_ok=True)
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filename)
    print("Extracting...")
    with tarfile.open(filename, "r:gz") as tar:
        tar.extractall(path=out_dir)
    print("Done!")

download_and_extract('https://web.stanford.edu/class/cs224u/data/cs224u.collection.2bits.tgz', 'experiments/notebook/indexes')
download_and_extract('https://downloads.cs.stanford.edu/nlp/data/colbert/colbertv2/colbertv2.0.tar.gz', 'data/openqa')
