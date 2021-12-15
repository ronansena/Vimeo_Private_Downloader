from vimeo_downloader import Vimeo

cookies = """
    ADPycduHZQUBZ9rwk9GPRcwHjSMLJdWTWEJoSu4QsZ-Sc8KUPa4YzmkjWbrmcfMpRHOb4PeF-IelnYg65sLE9d4SfHtXFGJ_cg
 """.strip()

v = Vimeo(
    embedded_on="https://programadetestesequalidade.club.hotmart.com/lesson/V4Vr2ax842/introducao-ao-modulo",
    url="https://player.vimeo.com/video/547005059",
    cookies=cookies,    
)

best_stream = v.best_stream
mp4_url = best_stream.direct_url

title = best_stream.title

## Download
best_stream.download()