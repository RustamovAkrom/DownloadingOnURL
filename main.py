from donwnload import DonwloadYouTubeVideo, DonwnloadWikipedia, DownloadPhoto


def menu():
    print( 'Download Video in YouTube -----> 1' )
    print( 'Download Photo in url     -----> 2' )
    print( 'Download text on Wikipedia-----> 3' )
    print( 'exit                      -----> 0' )

    x = int(input( 'enter:  ' ))

    match x:
        case 1:
            url = input('enter url Video: ')
            
            DonwloadYouTubeVideo( url, donwload=True )

        case 2:
            url = input('enter url photo: ')
            DownloadPhoto(url, download = True)
            
        case 3:
            url = input( 'wikipedia search enter:  ' )
            DonwnloadWikipedia(url, donwload = True )

        case _:
            print( "not fount" )
    menu()
def main():
    try:
        menu()
    except:
        print("Error in download!")
    finally:
        menu()

if __name__=='__main__':
    main()