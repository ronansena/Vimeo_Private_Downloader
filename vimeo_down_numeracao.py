from vimeo_downloader import Vimeo
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

try:
    arrayLine = []
    #In this path you must create the file listVideos.txt with the list of the download codes.
    #Also will be create the file logErro.txt automatically by the app in case of errors.
    pathFilesList = "/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/"
    #folder to save the downloads
    pathFilesDownload = "/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/Video"
    #Number init for the download videos
    count = 0
    with open(pathFilesList+"listVideos.txt", 'r') as objFile:
        for objFileLine in objFile:   
            count+= 1                
            arrayLine = objFileLine.split(",")
            idVideo = arrayLine[0].strip().replace("\n","") 
            nomeVideo = arrayLine[1].strip().replace("\n","").replace(" ","_").replace("(","_").replace(")","_").replace("!","")
            #Put your token here     
            cookies = """
                ADPycduHZQUBZ9rwk9GPRcwHjSMLJdWTWEJoSu4QsZ-Sc8KUPa4YzmkjWbrmcfMpRHOb4PeF-IelnYg65sLE9d4SfHtXFGJ_cg
            """.strip()
            try:
                v = Vimeo(
                    #Put your embedded URL here 
                    embedded_on="https://programadetestesequalidade.club.hotmart.com/lesson/V4Vr2ax842/introducao-ao-modulo",
                    url="https://player.vimeo.com/video/"+idVideo,
                    cookies=cookies    
                )
            except Exception as exception:
                with open(pathFilesList+"logErro.txt", 'a') as fileLogErroObj:
                        fileLogErroObj.write(str(exception))
                        fileLogErroObj.write("\n")
                        print(exception)
                        continue    
            try:
                best_stream = v.best_stream
                mp4_url = best_stream.direct_url      
                best_stream.title = remove_accents(count+"_"+nomeVideo)                
                ## Download
                try:
                    best_stream.download(download_directory=pathFilesDownload)                        
                except Exception as exception:
                    with open(pathFilesList+"logErro.txt", 'a') as fileLogErroObj:
                            fileLogErroObj.write(str(exception))
                            fileLogErroObj.write("\n")
                            print(exception)
                            continue
            except Exception as exception:
                 with open(pathFilesList+"logErro.txt", 'a') as fileLogErroObj:
                            fileLogErroObj.write(str(exception))
                            fileLogErroObj.write("\n")
                            print(exception)
                            continue
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError as valErr:
    print(valErr)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise