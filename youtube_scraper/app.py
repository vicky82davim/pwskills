from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
import os
import json
import re

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
        # fake user agent to avoid getting blocked by Google
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

        youtube_url = f"https://www.youtube.com/@PW-Foundation/videos"
        response = requests.get(youtube_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        images_tags = soup.find_all('script')

        txt = images_tags[36].get_text()

        name = re.findall(r"ytInitialData = ({.*?});", txt)[0]

        res = json.loads(name)

        res1 = res['contents']['twoColumnBrowseResultsRenderer']['tabs']

        del res1[0]

        video_details = dict()
        count = 0
        for i in res1:
                if 'tabRenderer' in i.keys():
                        if 'content' in i['tabRenderer'].keys():
                                con = i['tabRenderer']['content']['richGridRenderer']['contents']
                                for j in con:
                                        if count > 4:
                                                break
                                        if 'richItemRenderer' in j:
                                                if 'thumbnail' in j['richItemRenderer']['content']['videoRenderer']:
                                                        video_id = j['richItemRenderer']['content']['videoRenderer']['videoId']
                                                        thumb = j['richItemRenderer']['content']['videoRenderer']['thumbnail']['thumbnails'][0]['url']
                                                        title = j['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
                                                        viewCountText = j['richItemRenderer']['content']['videoRenderer']['viewCountText']['simpleText']
                                                        publishedTimeText = j['richItemRenderer']['content']['videoRenderer']['publishedTimeText']['simpleText']
                                                        
                                                        vdtl = {
                                                                'video_id': "https://www.youtube.com/watch?v="+video_id,
                                                                'thumbnail': thumb,
                                                                'title': title,
                                                                'viewCountText':viewCountText,
                                                                'publishedTimeText': publishedTimeText
                                                        }
                                                        
                                                        
                                                        video_details[video_id] = vdtl
                                                        count = count+1


        return render_template('result.html', video_details)

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
