import streamlit as st
from pytube import Playlist

def download_youtube_playlist(playlist_url, download_path, quality):
    if playlist_url != "" and download_path != '':
        try:
            playlist = Playlist(playlist_url)
            
            for video in playlist.videos:
                st.write(f'Downloading {video.title}')
                
                if quality == "highest":
                    video.streams.get_highest_resolution().download(output_path=download_path)
                elif quality == "lowest":
                    video.streams.get_lowest_resolution().download(output_path=download_path)
                else:
                    selected_stream = video.streams.filter(res=quality).first()
                    selected_stream.download(output_path=download_path)
                
                st.write(f'Downloaded {video.title}')
            st.success("All Videos Downloaded Successfully")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter playlist link and Download path")

def main():
    st.title("YouTube Playlist Downloader")
    st.write("Enter the YouTube playlist link, the download path, and select the video quality.")
    
    playlist_url = st.text_input("Paste Link here")
    download_path = st.text_input("Enter a Path You Need to save (Available that much Space)")
    quality = st.selectbox("Select video quality", ["highest", "lowest", "360p", "480p", "720p", "1080p"])
    
    if st.button("Download Playlist"):
        download_youtube_playlist(playlist_url, download_path, quality)

if __name__ == "__main__":
    main()
