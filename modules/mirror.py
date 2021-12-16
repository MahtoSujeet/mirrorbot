from pytube import YouTube, exceptions

print("*****This is a basic YouTube downloader script made by Rebel******\n\n")

link= input("Enter the link to the YouTube video: ")
try:
	vid= YouTube(link)
except exceptions.RegexMatchError:
	print("Please rerun the script and Enter a valid link this time, bsdk👺")
	exit()

# Resolution Selection
res= input("Please Enter the resolution(if you want 720p, enter 720 and likewise 480 for 480p. To download audio, Enter 'a'): ")

# Directory
dir_ = input("Enter the directory where you want to download the file: ")
if len(dir_) !=0:
	if dir_[-1] != "/":
		dir_ = dir_+"/"
try:
	with open(dir_+".test_file_by_ytdl_script.rebel", "w") as file:
		pass
except FileNotFoundError:
	print("This directory does not exist!")
	
	
if res=="a":
	stream= vid.streams.get_audio_only()
else:
	stream= vid.streams.filter(resolution=res).first()
	
print("Downloading has been started!")
print(f"Size of the file: {stream.filesize}")
stream.download(dir_)
print("Downloaded Successfully!")
