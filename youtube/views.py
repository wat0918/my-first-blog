#!/usr/bin/python3.4

from django.shortcuts import render

#def index2(request):

    #return render(request, 'index2.html')# Create your views here.


# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery

def main(request):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBPx2-SBWiqWJy4p4LnUmoRWMWJwHiKw6s"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    req1 = youtube.search().list(
        part="id",
        channelId="UCX1xppLvuj03ubLio8jslyA",
        maxResults=1,
        order="date"
    )
    response = req1.execute()

    context={
    'answer2': response["items"][0]["id"]["videoId"]
    }


    return render(request, 'index2.html', context)


#if __name__ == "__main__":
#    main()
