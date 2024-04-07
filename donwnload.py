from pytube import YouTube
import requests
import wikipedia
import os
from progress.bar import Bar


def DownloadPhoto(url, path = 'downloads/pictures/', download=False):
    
    responce    = requests.get( url )
    status_code = responce.status_code
    headers     = responce.headers
    content     = responce.content
    text        = responce.text
    if download:
        
        if status_code == 200:
            print( 'Downloading...' )
            with open(f"{ path }photo-{ headers['Content-Length'] }.jpg", 'wb') as f:
                f.write( content )

    return status_code, headers, 


def DonwloadYouTubeVideo(url, path = 'videos/', donwload = False):
    
    youtube  = YouTube( url=url )
    youtube.from_id
    
    title    = youtube.title
    views    = youtube.views
    lenght   = youtube.length

    if donwload:
        print( "Downloading..." )
        youtube.streams.get_highest_resolution().download( path )


    print(f"[Заголовок]:                { title  }")
    print(f"[Количество просмотров]:    { views  }")
    print(f"[Продолжительность видео]:  { lenght }")


def DonwnloadWikipedia(page, path='downloads/wikipedia', language='ru', donwload=False):
    
    wikipedia.set_lang( language )
    
    python_page = wikipedia.page( page )
    # search_page = wikipedia.search( search )

    origin_title = python_page.original_title
    summary      = python_page.summary
    url          = python_page.url
    html         = python_page.html
    title        = python_page.title
    images       = python_page.images

    if donwload:
        print( 'Downloading...' )
        with open( f'{path}/{ origin_title }.txt','w', encoding = 'utf-8' ) as f:
            f.write( origin_title      + '\n')
            f.write( summary           + '\n')
            f.write( '[URL address]: ' +  url)
            
    return title, summary, url, html, images


def replese_dir( path_dir, replese_dir ):
    "|Photo or Video replese|"
    ls = os.listdir( path_dir )
    l  = len( ls )

    for index in range( 0, l ):

        with open( path_dir + '/' +  ls[index], 'rb' ) as rb:
            with open( replese_dir + '/' + ls[index], 'wb' ) as wb:
                wb.write( rb.write() )
                
    return ls



