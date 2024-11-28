import requests

def download_list(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return []

def process_lists(urls):
    all_lines = {}
    duplicates = {}

    for url in urls:
        lines = download_list(url)
        for line in lines:
            line = line.strip()
            if line and not line.startswith("!") and not line.startswith("#"):
                if line in all_lines:
                    if line not in duplicates:
                        duplicates[line] = set()
                    duplicates[line].add(url)
                else:
                    all_lines[line] = url

    return all_lines, duplicates

def main():
    urls = [
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt",
        "https://raw.githubusercontent.com/neodevpro/neodevhost/master/adblocker",
        "https://raw.githubusercontent.com/Cats-Team/AdRules/main/dns.txt",
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_5.txt",
        "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt"
    ]

    all_lines, duplicates = process_lists(urls)

    duplicate_sources = set()
    for sources in duplicates.values():
        duplicate_sources.update(sources)

    with open("comads.txt", "w") as f:
        for line in sorted(all_lines.keys()):
            f.write(line + "\n")

if __name__ == "__main__":
    main()
