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

def main():
	if len(argv) != 3:
		usage()

	file = argv[2]
	if(argv[1] == "-u"):
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
	elif(argv[1] == "-d"):
		remote = "http://a.pomf.se/" + file
		print(remote)
		dl = urllib2.urlopen(remote)
		fsave = open(file, 'wb')
		fsave.write(dl.read())
		fsave.close()
if __name__ == '__main__':
	main()