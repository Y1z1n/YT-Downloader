try:
    import pytube, tabulate, argparse
    from colorama import init , Fore, Back, Style
    from moviepy.editor import VideoFileClip
    from sys import argv
    init()
except:
    from os import system
    print(Fore.RED+"[*] Installing requirments ")
    print(Style.RESET_ALL)
    system("pip install tabulate")
    system("pip install git+https://github.com/nficano/pytube")
    system("pip install argparse")
    system("pip install moviepy")
    system("pip install colorama")
    system("cls || clear")
    init()
#SYNTAX 
# python "Download youtube vids.py" -Format mp3 -Video Video https://www.youtube.com/watch?v={CODE}


# python "Download youtube vids.py" -Format mp3 -Video Playlist https://www.youtube.com/playlist?list={CODE}

print(Fore.RED + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
print(Fore.RED + tabulate.tabulate([['Y1z1n.programs', "Download Youtube vids"]], ['Creator account on instagram', "Usage of the tool"], tablefmt="pretty"))
print(Style.RESET_ALL)
def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    del clip.reader
    del clip
def download_video(url, video=False):
    yt = pytube.YouTube(url)
    yt.streams.filter().first().download()
    if video==False:
        convert(yt.streams.get_by_itag(18).default_filename)
    else:
        return yt.streams.get_by_itag(18).default_filename

def convert(filename):
    convert_to_mp3(filename)
def download_videos(urls, filetype):
    filenames = []
    if filetype=="mp3":
        video_or_nah=False
    else:
        video_or_nah=True
    for index, url in enumerate(urls, start=1):
        filenames.append(download_video(url, video_or_nah))
        print(Fore.GREEN + f"Downloaded | [{index}]: {filenames[index -1]}\n")
        print(Style.RESET_ALL)
    if filetype == "mp3":
        for video in filenames:
            convert(video)

def download_playlist(url, filetype):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, filetype)

def Args():
    try:
        parser = argparse.ArgumentParser(description="Big")
        parser.add_argument("-Format", help="Format of the video", default="mp3")
        parser.add_argument("u", help="URL")
        parser.add_argument("-Video", help="Video or Playlist",default="Video")
        # Choice = input("\n\n[1] A video \n[2] A playlist\n--->")
        args = parser.parse_args()
        # print(args.Format, args.Video, args.u)
        if args.Video == "Playlist" and args.Format == "mp3": #THE PROBLEM HEREE
            download_playlist(args.u, "mp3")
        elif args.Video =="Playlist" and args.Format == "mp4":
            download_playlist(args.u, "mp4")
        elif args.Video == "Video":
            filename = download_video(args.u ,False if args.Format == "mp3" else True)
            print(Fore.GREEN + f"Downloaded | {filename}")
            if args.Format == "mp3":
                print(Fore.GREEN + "Converting to mp3 :\n")
                convert_to_mp3(filename)
            print(Style.RESET_ALL)

    except AttributeError:
        None #hehe
    except:
        None #also hehe

if len(argv) > 1:
    Args()
else:
    Choice = input(Fore.YELLOW + "\n\n[1] A video \n[2] A playlist\n--->")
    url = input(Fore.YELLOW + "[?] Url please -> ")
    filetype = input(Fore.YELLOW + "[?] video or song -> ")
    if Choice == "1":
        print(Style.RESET_ALL)
        download_video(url, True if filetype=="video" else False)
        print(Fore.GREEN + "[*] Finished")
    else:
        print(Style.RESET_ALL) 
        download_playlist(url, True if filetype=="video" else False)
        print(Fore.GREEN + "[*] Finished")
