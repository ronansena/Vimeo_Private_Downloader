from vimeo_downloader import Vimeo
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

try:
    arrayLine = []
    with open("/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/listVideos.txt", 'r') as objFile:
        for objFileLine in objFile:                     
            arrayLine = objFileLine.split(",")
            idVideo = arrayLine[0].strip().replace("\n","") 
            nomeVideo = arrayLine[1].strip().replace("\n","").replace(" ","_").replace("(","_").replace(")","_").replace("!","")

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
                with open("/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/logErro.txt", 'a') as fileLogErroObj:
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
                    best_stream.download()
                except Exception as exception:
                    with open("/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/logErro.txt", 'a') as fileLogErroObj:
                            fileLogErroObj.write(str(exception))
                            fileLogErroObj.write("\n")
                            print(exception)
                            continue
            except Exception as exception:
                 with open("/home/kaus/CODE/PYTHON/Download_Vimeo_Protected/logErro.txt", 'a') as fileLogErroObj:
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