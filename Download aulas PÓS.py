import requests
import re
import sys
import os


lessons = {
            "Introdução à Ciência de Dados e à Inteligência Artificial" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/513920520?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/513937612?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/513954413?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/513973389?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/514264039?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/514278493?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/514291086?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/514309571?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/514437686?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/514449649?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/514461613?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/514478849?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Fundamentos de Estatística para Ciência de Dados" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/519548558?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/521456379?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/521529605?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/522951506?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/521469486?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/521489720?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/521556791?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/521571433?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/521896223?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/521916595?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/521932612?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/521954689?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/522365274?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/522380023?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/522392650?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/522402609?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/522884500?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/522903875?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/522924072?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/522941675?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/522440585?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/522986959?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/522992903?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/522998336?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Python para Ciência de Dados" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/531323095?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/531472102?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/531487322?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/531498586?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/531505124?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/531513757?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/531542267?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/531548078?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/531557297?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/531562918?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/531534958?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/531568628?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/531574053?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/531583516?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/531544379?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/531545661?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/531547264?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/531548686?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/531560887?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/531562211?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/531563210?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/531564726?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Bancos de Dados Relacionais e Não-Relacionais" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/538738478?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/538752876?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/538764630?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/538782663?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/537766304?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/537774950?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/537790562?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/537861821?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/538789669?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/538796384?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/538802589?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/538813810?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/538838479?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/538850516?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/538858334?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/538868244?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/538878232?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/538893077?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/538906491?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/538912584?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/538918727?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/538928482?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/538936396?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/538945120?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Pré-processamento de Dados" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/545315382?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/545311483?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/545332196?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/545322176?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/545340200?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/545345467?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/545444200?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/545449776?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/544807823?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/544832612?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/544838172?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/544845949?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/545221056?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/545237681?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/545250182?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/545267086?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/545268885?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/567656057?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/545272473?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/565411515?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/545285657?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/545294419?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/545288375?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Gerência de Infraestrutura para Big Data" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/554421362?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/554562026?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/554482630?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/554490328?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/554580058?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/554590849?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/554596669?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/554502984?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/554510465?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/554514501?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/554543999?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/554532950?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/554542357?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/554556869?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/554619647?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/554551410?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/554558203?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/554670600?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/554676491?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/554566113?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/554664430?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/554667061?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/554661769?api=1&player_id=vimeoAula&autoplay=1"
            }
        }







def create_directory(dirName):
    try:
        os.makedirs(dirName)    
        print("[+] Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("[-] Directory " , dirName ,  " already exists")  

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


for lesson, lessonData in lessons.items():
    print(lesson)
    if not os.path.isdir(f"./{lesson}"):
        create_directory(f"./{lesson}")
    for lessonName, link in lessonData.items():
        if not os.path.exists(f"./{lesson}/{lessonName}.mp4"):
            print(f"[+] Acessing {link}")
            r = requests.get(link, headers=headers, allow_redirects=True)
            html = r.content.decode('utf-8')
            link_mp4 = parser(html)
            download(link_mp4, f"./{lesson}/{lessonName}")

