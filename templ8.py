import textile
import os

beginning = ""
ending = ""

with open("basetemplate.html", "r") as f:
	data = f.read().split("##SPLITPOINT##")
	beginning = data[0]
	ending = data[1]

# Code I got from StackExchange. It works, not sure why but hey.
def get_filepaths(directory):
	file_paths = [] 

	for root, directories, files in os.walk(directory):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)  

	return file_paths

def get_info(data):
	newdata = data
	pagetitle = ""
	css = "YOUR CSS FILE HERE"
	logo = "YOUR LOGO HERE"
	if newdata.find("PAGETITLE=") == 0:
		pagetitle = newdata[newdata.find("PAGETITLE=")+10:newdata.find("##")]
		newdata = newdata.replace(newdata[:newdata.find("##")+3],"",1)
	if newdata.find("SPECIALCSS=") == 0:
		css = newdata[newdata.find("SPECIALCSS=")+11:newdata.find("##")]
		newdata = newdata.replace(newdata[:newdata.find("##")+3],"",1)
	if newdata.find("LOGO=") == 0:
		logo = newdata[newdata.find("LOGO=")+5:newdata.find("##")]
		newdata = newdata.replace(newdata[:newdata.find("##")+3],"",1)
	return {
		"data" : newdata,
		"pagetitle" : pagetitle,
		"css" : css,
		"logo" : logo
	}
   
full_file_paths = get_filepaths("textilewebsite/")
print(full_file_paths)

for i in full_file_paths:
	with open(i, "r") as og:
		data = og.read()
		gotten = get_info(data)
		data = gotten["data"]

		with open(i.replace("textilewebsite/", "htmlwebsite/") + ".html", "w") as new:
			newdata = beginning.replace("##PAGETITLE##", gotten["pagetitle"]).replace("##CSS##", gotten["css"]).replace("##LOGO##", gotten["logo"]) + textile.textile(data) + ending
			new.write(newdata)
			print(newdata)