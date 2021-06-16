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
	""" This function will generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each 
	directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames). """
	file_paths = []  # List which will store all of the full filepaths.

	# Walk the tree.
	for root, directories, files in os.walk(directory):
		for filename in files:
			# Join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)  # Add it to the list.

	return file_paths  # Self-explanatory.

def get_info(data):
	newdata = data
	pagetitle = ""
	css = "https://ampersandia.neocities.org/style.css"
	logo = "&"
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

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("textilewebsite/")
print(full_file_paths)

for i in full_file_paths:
	with open(i, "r") as og:
		data = og.read()
		gotten = get_info(data)
		data = gotten["data"]
		print(textile.textile(data))
		with open(i.replace("textilewebsite/", "htmlwebsite/").replace(".textile","") + ".html", "w") as new:
			newdata = beginning.replace("##PAGETITLE##", gotten["pagetitle"]).replace("##CSS##", gotten["css"]).replace("##LOGO##", gotten["logo"]) + textile.textile(data) + ending
			new.write(newdata)
