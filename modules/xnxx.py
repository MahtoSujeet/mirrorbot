import ffmpeg_streaming, ffmpeg
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import os

def download (arg):
	video = ffmpeg_streaming.input("https://hls-hw.xvideos-cdn.com/videos/hls/17/e9/9d/17e99d474170e6c10e57584c8687a8b4/hls.m3u8?e=1639828349&l=0&h=c82b5b1b185ef60440c260fb2f9487e5")
	
	
	
	_360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
	_480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
	_720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

	hls = video.hls(Formats.h264())
	hls.representations(_720p)
	
	hls.output("video.mp4")
	
	return "video.mp4"
	
def test():
	download("hey")
	
if __name__=="__main__":
	test()
