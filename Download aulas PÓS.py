import requests
import re
import sys


urls = {
            "https://player.vimeo.com/video/538738478?api=1&player_id=vimeoAula&autopause=0",
            "https://player.vimeo.com/video/538752876?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538764630?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538782663?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/537766304?api=1&player_id=vimeoAula&autopause=0",
            "https://player.vimeo.com/video/537774950?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/537790562?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/537861821?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538789669?api=1&player_id=vimeoAula&autopause=0",
            "https://player.vimeo.com/video/538796384?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538802589?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538813810?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538838479?api=1&player_id=vimeoAula&autopause=0",
            "https://player.vimeo.com/video/538850516?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538858334?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538868244?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538878232?api=1&player_id=vimeoAula&autopause=0",
            "https://player.vimeo.com/video/538893077?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538906491?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538912584?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538918727?api=1&player_id=vimeoAula&autopause=0",
            "https://player.vimeo.com/video/538928482?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538936396?api=1&player_id=vimeoAula&autoplay=1",
            "https://player.vimeo.com/video/538945120?api=1&player_id=vimeoAula&autoplay=1"
        }



headers = {'Referer': 'https://salavirtual.pucrs.br/'}



def parser(input):
    regex = r"\"profile\":\".+\",\"width\":1920,\"mime\":\"video\/mp4\",\"fps\":.+,\"url\":\"(.+?)\",\"cdn\":\"akamai_interconnect\",\"quality\":\"1080p\",\"id\":\".+\",\"origin\":\"gcs\",\"height\":1080"
    matches = re.finditer(regex, input)
    for matchNum, match in enumerate(matches, start=0):
        return match.group(1)


def download(link, x):
    file_name = f"{x}.mp4"
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

x=0

for url in urls:
    x = x + 1
    print(f"[+] Acessing {url}")
    r = requests.get(url, headers=headers, allow_redirects=True)
    html = r.content.decode('utf-8')
    link_mp4 = parser(html)
    print(f"[+] Link for mp4 1080p: {link_mp4}")
    download(link_mp4, x)
    print(f"File saved {x}.mp4")
