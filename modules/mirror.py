import requests

def mirror(arg):
	args= arg.split("|")
	try:
		link= args[0].strip()
		try:
			file_name= args[1].strip()
		except Exception:
			file_name= args[0].split("/")[-1]
	except Exception as e:
		return f"ERROR : {e}"
	
	response= requests.get(link, stream= True)
	open(file_name, "w").close()
	with open(file_name, "wb") as file:
		for chunk in response.iter_content(chunk_size= 1024):
			file.write(chunk)
	return file_name
			
			
	