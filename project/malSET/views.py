from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import hashlib
import pefile
import base64
import math
import os

def index(request):
    return render(request, 'malSET/home.html')

def report(request, filename_b64):
    filename_bytes = base64.b64decode(filename_b64.encode("ascii"))
    filename = filename_bytes.decode("ascii").replace('%20', ' ')
    file_extension = os.path.splitext(filename)[1]
    server_file_path = os.path.join(settings.MEDIA_ROOT,os.path.basename(filename))

    with open(server_file_path, "rb") as f:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        while chunk := f.read(8192):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    DLL_dict = {}
    if file_extension == ".exe":
        pe = pefile.PE(server_file_path)

        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll_name = entry.dll.decode('utf-8')
            DLL_dict[dll_name] = []
            print(f"[*] {dll_name} imports:")
            for func in entry.imports:
                try:
                    print("\t%s at 0x%08x" % (func.name.decode('utf-8'), func.address))
                    #API_list.append(func.name.decode('utf-8'))
                    DLL_dict[dll_name].append(func.name.decode('utf-8'))
                except:
                    DLL_dict[dll_name].append('')

    file_size = os.path.getsize(server_file_path)
    context = {
        'filename': os.path.basename(filename),
        'filesize': [convert_size(file_size), str(file_size) + ' bytes'],
        'md5': md5.hexdigest(),
        'sha1': sha1.hexdigest(),
        'dll_dict': DLL_dict,
        'system_calls': [1,2,3,4],
        'api_calls': [1,2,3,4],
    }
    return render(request, 'malSET/report.html', context)

def file_upload(request):
    if request.method == 'POST' and request.FILES['filename']:
        myfile = request.FILES['filename']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        # Encode filename for url
        uploaded_file_url = fs.url(filename)

        base64_bytes = base64.b64encode(uploaded_file_url.encode("ascii"))
        return redirect('report', base64_bytes.decode("ascii"))
    return redirect('index')

    # print(request.POST)
    # print(request.FILES)
    # return HttpResponse("Uploaded")

# Internal Methods
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])