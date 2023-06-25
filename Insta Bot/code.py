from instabot import Bot
bot = Bot()
bot.login(username = "yaaraotaara11", password = "your-passkey-here")
bot.unfollow("therisingsingers")
bot.upload_photo("./kid goku.jpg", caption="The greatest saiyan warrior becomes a kid !!!")
bot.follow("therisingsingers")
bot.send_message("Hi !",["swooshpuri", "sarangchaturvedi"])
followers = bot.get_user_followers("yaaraotaara11")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("yaaraotaara11")
for followed in following:
    print(bot.get_user_info(followed))