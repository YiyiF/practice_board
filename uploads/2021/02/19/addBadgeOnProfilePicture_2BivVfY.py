#! /usr/bin/env python3

import requests, os
from PIL import Image, ImageDraw, ImageFont

def getProfilePicture(qq_id, size=100):
    # Get Profile Picture.
    # https://blog.csdn.net/lddtime/article/details/64590011
    profilePictureUrl = 'http://q1.qlogo.cn/g?b=qq&nk=' + qq_id + '&s=' + size
    pictureContent = requests.get(profilePictureUrl)
    pictureContent.raise_for_status()
    filename = qq_id + '.png'
    imageFile = open((os.path.basename(filename)), 'wb')
    for chunk in pictureContent.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    return filename

def addBadgeOnPicture(profilePicture, num):
    # Create badge image.
    badge = Image.new('RGBA', (20, 20), (0, 0, 0, 0))
    draw_table = ImageDraw.Draw(im=badge)
    draw_table.text(xy=(0, 0), text=num, fill='red', font=ImageFont.FreeTypeFont('/System/Library/Fonts/Avenir.ttc', size=20))
    # badge.show()

    # Add badge on profile picture.
    profilePicture = Image.open(profilePicture)
    badgedPicture = profilePicture.copy()
    width, height = badgedPicture.size
    badgedPicture.paste(badge, (width - 10, 5), badge)
    badgedPicture.show()
    badgedPicture.save('result.png')

def run():
    qq = input('QQ number: ')
    size = input('Size of profile picture: ')
    badge = input('Badge number: ')
    profilePicture = getProfilePicture(qq, size)
    addBadgeOnPicture(profilePicture, badge)

if __name__ == '__main__':
    run()