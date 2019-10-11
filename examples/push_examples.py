from pushbullet import Pushbullet

#Put your access token here, for examle: o.bdkFgaQxqdvUVukSitumShX3DoszszQh
pb = Pushbullet("<your access token>")

#Get all devices that the current user has access to.
print(pb.devices)

#Get a device
dev = pb.get_device("Galaxy S7 Edge")

#1. Push Notification
push = dev.push_note("Alert!", "This PUSH-notification sent fro Raspberry!")

# push is a dictionary containing the data returned by the Pushbullet API.
print('A dictionalry after 1:')
print(push)

#2. SMS-message
push = pb.push_sms(dev, "+31612345678", "This SMS sent from Raspberry!")
print('A dictionalry after 2:')
print(push)


#3. Push a file from file system
with open("thief.jpg", "rb") as pic:
    file_data = pb.upload_file(pic, "picture.jpg")
push = pb.push_file(**file_data)
print('A dictionalry after 3:')
print(push)


#4. Push a file already uploaded somewhere
push = pb.push_file(file_url="https://i.imgur.com/IAYZ20i.jpg", file_name="cat.jpg", file_type="image/jpeg")
print('A dictionalry after 4:')
print(push)
