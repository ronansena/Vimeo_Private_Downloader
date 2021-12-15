from vimeo_downloader import Vimeo
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

try:
    arrayLine = []
    #In the path put on the variable pathFiles you must create the file listVideos.txt with the list of the download codes.
    pathFiles = "/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/"
    #folder to save the downloads
    pathFilesDownload = "/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/Video"
    
    with open(pathFiles+"listVideos.txt", 'r') as objFile:
        for objFileLine in objFile:                     
            arrayLine = objFileLine.split(",")
            idVideo = arrayLine[0].strip().replace("\n","") 
            nomeVideo = arrayLine[1].strip().replace("\n","").replace(" ","_").replace("(","_").replace(")","_").replace("!","")
            #In here put the token of the site     
            cookies = """
                ADPycduHZQUBZ9rwk9GPRcwHjSMLJdWTWEJoSu4QsZ-Sc8KUPa4YzmkjWbrmcfMpRHOb4PeF-IelnYg65sLE9d4SfHtXFGJ_cg
            """.strip()
            try:
                v = Vimeo(
                    embedded_on="https://programadetestesequalidade.club.hotmart.com/lesson/V4Vr2ax842/introducao-ao-modulo",
                    url="https://player.vimeo.com/video/"+idVideo,
                    cookies=cookies    
                )
            except Exception as exception:
                with open(pathFiles+"logErro.txt", 'a') as fileLogErroObj:
                        fileLogErroObj.write(str(exception))
                        fileLogErroObj.write("\n")
                        print(exception)
                        continue    
            try:
                best_stream = v.best_stream
                mp4_url = best_stream.direct_url      
                best_stream.title = remove_accents(nomeVideo)                
                ## Download
                try:
                    best_stream.download(download_directory=pathFilesDownload)                        
                except Exception as exception:
                    with open(pathFiles+"logErro.txt", 'a') as fileLogErroObj:
                            fileLogErroObj.write(str(exception))
                            fileLogErroObj.write("\n")
                            print(exception)
                            continue
            except Exception as exception:
                 with open(pathFiles+"logErro.txt", 'a') as fileLogErroObj:
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