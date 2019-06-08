# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
from django.shortcuts import render
import os
from django.conf.urls import include
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBPx2-SBWiqWJy4p4LnUmoRWMWJwHiKw6s"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="id",
        channelId="UCK4a1HaugtjTmMtRhdBh1ww",
        maxResults=1,
        order="date"
    )
    response = request.execute()


    answer2= response["items"][0]["id"]["videoId"]



    print(answer2)
    return render(request, 'index2.html', answer2)
    print(response)

if __name__ == "__main__":
    main()
