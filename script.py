import asyncio
import requests

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

urls = [{1: 'https://www.walmart.com/'},
        {2: 'https://www.coles.com.au/'},
        {3: "https://www.target.com"},
        {4: 'https://www.amazon.fr'},

        ]

results = []


def get_key(dict_input: dict):
    return list(dict_input.keys())[0]


async def ping_url(url, retailer):
    response = requests.get(url, headers=headers, timeout=20)
    await asyncio.sleep(1)
    return {retailer: {url: response.elapsed.total_seconds()}}

if __name__ == "__main__":
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)

	ping1 = asyncio.gather(*[ping_url(url[get_key(url)], get_key(url)) for url in urls])
	ping2 = asyncio.gather(*[ping_url(url[get_key(url)], get_key(url)) for url in urls])
	ping3 = asyncio.gather(*[ping_url(url[get_key(url)], get_key(url)) for url in urls])

	all_pings = asyncio.gather(ping1, ping2, ping3)
	results = loop.run_until_complete(all_pings)
	loop.close()
	results

