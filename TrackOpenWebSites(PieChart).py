import win32gui
import time
import matplotlib.pyplot as plt

def get_chrome_urls():
    urls = []
    def callback(hwnd, process):
        if win32gui.GetWindowText(hwnd) == "":
            return
        if 'chrome' not in win32gui.GetClassName(hwnd).lower():
            return
        urls.append(win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(callback, None)
    return urls

# initialize an empty dictionary to store website counts
website_counts = {}

# create an empty pie chart with no labels
plt.pie([], labels=[])

while True:
    chrome_urls = get_chrome_urls()

    # iterate through the URLs and count each one
    for url in chrome_urls:
        if " - Google Chrome" in url:
            # remove the trailing " - Google Chrome" from the URL
            url = url[:-len(" - Google Chrome")]
            # increment the count for this URL in the dictionary
            website_counts[url] = website_counts.get(url, 0) + 1

    # extract the counts and website names from the dictionary
    counts = list(website_counts.values())
    websites = list(website_counts.keys())

    # plot the pie chart with the cumulative counts
    plt.clf()
    plt.pie(counts, labels=websites, autopct='%1.1f%%')
    plt.title('Open Chrome Websites')
    plt.draw()
    plt.pause(5)  # pause for 30 seconds before updating the chart
