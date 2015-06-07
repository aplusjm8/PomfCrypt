from sys import version
from sys import argv
from sys import exit

import urllib2

try:
	import requests
except ImportError:
	pyver = int(version.split(".")[0])
	print("Could not run - is python" + ('2' if pyver == 2 else '') \
	+ "-requests installed?")
	exit()

def usage():
	print("Usage: " + argv[0] + " <filename>")
	exit()

file = argv[2]
def download():
		remote = "http://a.pomf.se/" + file
		dl = urllib2.urlopen(remote)
		print("Downloading " + remote + " and saving as " + file)
		fsave = open(file, 'wb')
		fsave.write(dl.read())
		fsave.close()	
def upload():
	with open("URLS.db", 'r') as inF:
		for line in inF:
			if file in line:
				print "File already present in URL database"
			else:
				try:
					response = requests.post(
						url="http://pomf.se/upload.php",
						files={"files[]":open(file, "rb")}
					)
				except Exception as e:
					print("Error uploading {0}".format(e))
					exit()

				local = file.split('/')
				local = (local[-1] if len(local) > 1 else local[0])
				remote = "http://a.pomf.se/" + response.text.split('"')[17]
				print(local + " -> " + remote)
				urltogo = file + " == " + remote
				urlman = open("URLS.db", "a+")
				urlman.write(urltogo + "\n")
				urlman.close()
def encrypt():
	print("To Add")
def decrypt():
	print("To Add")
def main():
	if len(argv) != 3:
		usage()
	if(argv[1] == "-u"):
		upload()
	elif(argv[1] == "-d"):
		download()
	elif(argv[1] == "-dd"):
		#download()
		decrypt()
	elif(argv[1] == "-eu"):
		encrypt()
		#upload
if __name__ == '__main__':
	main()