try: 
    from googlesearch import search 
    import requests
    import wget
    from tqdm import tqdm
    from clint.textui import progress

except ImportError: 
        
    print("in 2 dastoor ro vared kon \n(pip install -r requirements.txt)\n(pip3 install -r requirements.txt)")
    print("********************")
    print("enter these two command \n(pip install -r requirements.txt)\n(pip3 install -r requirements.txt)")

class bcolors:
    blue = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    normal = '\033[0m'

def download_link(link):

	# url = link
	# buffer_size = 1024
	# response = requests.get(url, stream=True)

	# file_size = int(response.headers.get("Content-Length", 0))

	# filename = url.split("/")[-1]

	# progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
	# with open(filename, "wb") as f:
	#     for data in progress:
	#         # write data read to the file
	#         f.write(data)
	#         # update the progress bar manually
	#         progress.update(len(data))
	r = requests.get(music_url, stream=True)

	name = music_url[ music_url.rfind("/")+1   : ].replace("%20"," ")

	with open(name, "wb") as Pymusic:

	    total_length = int(r.headers.get('content-length'))

	    for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):

	        if ch:

	            Pymusic.write(ch)






# to search
print(bcolors.blue+"matn ahang , maddahi ya ... ro benevis\n ***be farsi benevisid\n")
print("enter a part of the music text \n"+bcolors.normal)
query = input()
print("\n")
site_list = []
for j in search(query,  lang='ir', num=10, stop=10, pause=2): 
    if j.find("youtube.com") == -1 and j.find("aparat.com") == -1 :
        site_list.append(j)



for music_i in range (len(site_list)):


	music_list = []
	webpage=requests.get( site_list[music_i] )
	webpage = webpage.text    

	cc = 0
	while 1==1 :
	    c = webpage.find('.mp3"',cc)
	    cc = c+1
	    #print(c)
	    #print(webpage[c-20:c+20])
	    if c == -1:
	        #print("braked")
	        break
	    b = webpage.rfind('href="',0,c+1)
	    #print(b)
	    a = webpage.rfind('<',0,c+1)
	    #print(a)
	    if a != -1 and b != -1 and c != -1 :
	        if a < b :       
	            music_url = webpage[b+6:c+4]
	            #print(music_url)
	            music_list.append(music_url)
	

	if len(music_list) > 0 :

		for i in range (len(music_list)) :
		    print(i,end="")
		    print(" =>  ",end="")
		    print(music_list[i][ music_list[i].rfind("/")+1   : ].replace("%20"," "))
		    if i == 4 :

		        break
		    

		print(bcolors.blue+"\nkodoom ro download konam ?? ( adadesh ro vared kon )\n")
		print("which one do you want ?(enter number) \n"+bcolors.normal)
		while 1 == 1 :    
		    try:
		        music_num = int(input())
		        break
		    except :
		        print("\n ***faghat adad vared kon !!! \n ***just enter number !!\n")
		    
		print(bcolors.green+"\ndownload shoro shod")        
		print("\ndownload started :)\n"+bcolors.normal)

		#mp3 = requests.get(music_list[music_num])
		#name = music_url[ music_url.rfind("/")+1   : ].replace("%20"," ")
		#with open('./' + name , 'wb') as f:
		#    f.write(mp3.content)

		#wget.download(music_list[music_num])
		print(bcolors.yellow+"")
		download_link(music_list[music_num])
		print(bcolors.green+"\ndownload tamoom shod \nahang zakhire shod\n")
		print("download end  \nmusic saved"+bcolors.normal)
		break





    
