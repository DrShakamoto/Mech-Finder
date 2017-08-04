#!/usr/bin/env python3

import praw
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

reddit = praw.Reddit(client_id=' ',
                     client_secret=' ',
                     password=' ',
                     user_agent=' ',
                     username=' ')#creates the reddit client, fill in your reddit credentials

subreddit = reddit.subreddit('mechmarket')#gets the subreddit, fill in the name of your subreddit

def sendEmail(postLink): #sends the email
    msg = MIMEMultipart()
    msg['From'] = ' ' #email address the email is from
    msg['To'] = ' ' #recipient of the email
    msg['Subject'] = " " #email subject
    body = " " #body of the email
    body = MIMEText(body)
    msg.attach(body)
    
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)#server settings for gmail
    smtpObj.starttls()
    smtpObj.login(' ', ' ') #sender address, password
    smtpObj.send_message(msg)
    smtpObj.quit()

print("searching...")

while True:
    # Have we run this code before? If not, create an empty list
    if not os.path.isfile("posts_read.txt"):
        posts_read = []

    # If we have run the code before, load the list of posts we have replied to
    else:
        # Read the file into a list and remove any empty values
        with open("posts_read.txt", "r") as f:
            posts_read = f.read()
            posts_read = posts_read.split("\n")
            posts_read = list(posts_read)

    for submission in subreddit.new(limit=10):
        if submission.id not in posts_read:
            if 'UK' in submission.title or 'uk' in submission.title:
                sendEmail(submission.url)
                posts_read.append(submission.id)
                print("found a keyboard")
                print("searching...")
                print(submission.title)

    with open("posts_read.txt", "w") as f:
        for post_id in posts_read:
            f.write(post_id + "\n")

    
