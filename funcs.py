import keyboard
import pyautogui

from auxmodule import *


# Set Up Profile
def setUpProfile():
    status = DEFAULT

    # Go To My Profile
    status = findNClick(PROFILE, timer=TIMER_FAST)
    if status:
        print("PROFILE clicked")
    else:
        print("IMAGE not found")
        return status

    # Set Up Profile
    status = findNClick(SET_UP)
    if status:
        print("SET_UP clicked")
    else:
        print("SET_UP not found")
        return status

    status = findNClick(IMAGE)
    if status:
        print("IMAGE clicked")
    else:
        print("IMAGE not found")
        return status

    status = findNClick(CHOOSE_IMAGE)
    if status:
        print("CHOOSE_IMAGE clicked")
        keyboard.send("right")
        keyboard.send("delete")
        pyautogui.moveTo(COORDS, FLAG)
    else:
        print("CHOOSE_IMAGE not found")
        return status

    status = findNClick(CHOOSE_IMAGE)
    if status:
        print("CHOOSE_IMAGE clicked")
        keyboard.send("right")
        keyboard.send("enter")
    else:
        print("CHOOSE_IMAGE not found")
        return status

    status = findNClick(APPLY)
    if status:
        print("APPLY clicked")
    else:
        print("APPLY not found")
        return status

    status = findNClick(NEXT)
    if status:
        print("NEXT clicked")
    else:
        print("NEXT not found")
        return status
    status = findNClick(SKIP)
    if status:
        print("SKIP clicked")
    else:
        print("SKIP not found")
        return status
    status = findNClick(BIO)
    if status:
        print("BIO clicked")
    else:
        print("BIO not found")
        return status

    pyautogui.write("Lucky!")

    status = findNClick(NEXT)
    if status:
        print("BIO clicked")
    else:
        print("BIO not found")
        return status

    return FLAG


# 1. Follow Amara Finance on Twitter
def followAmara():
    status = DEFAULT

    # open twitter page
    print("moveToNClick")
    status = moveToNClick(FOLLOW_AMARA_FINANCE, FOLLOW_AMARA_FINANCE_CLICK, timer=TIMER_FAST)
    print("DONE")

    # Find and Click Follow Button
    if FLAG:
        status = findNClick(FOLLOW_BUTTON_ENG)
    if FLAG:
        status = setUpProfile()
    if FLAG:
        closeTab()

    return FLAG


# 2. Retweet Amara on Twitter
def retweetAmara():
    status = DEFAULT

    # Open twitter
    status = moveToNClick(RETWEET_AMARA_FINANCE, RETWEET_AMARA_FINANCE_CLICK)
    if status:
        print("Link Retweet Found")
    else:
        print("Retweet Link Not found")
        return status

    # Page down
    status = pageDown(AMARA_TWITTER_PAGE, 2)
    print("PAGEDOWN twice")

    # Find and click retweet button
    status = findNClick(RETWEET)
    if status:
        print("Retweet Button found")
    else:
        print("Retweet Button NOT found")
        return status

    # Retweet
    status = findNClick(RETWEET_CLICK, timer=TIMER_FAST)
    if status:
        print("Retweeted")
    else:
        print("Couldn't retweet. Button not found")

    return status


# 3. Tweet Amara With The Following HashTag
def tweetAmara():
    status = DEFAULT

    # Click menu button
    status = findNClick(TWEET_AMARA_FINANCE, timer=TIMER_FAST)
    if status:
        print("Link Tweet Amara Found")
    else:
        print("Link Tweet Amara Not Found")
        return status

    # open twitter
    status = findNClick(TWEET_AMARA_FINANCE_CLICK, timer=TIMER_FAST)
    if status:
        print("Button Tweet Found")
    else:
        print("Button Tweet Not Found")
        return status

    # Click tweet blue button
    status = findNClick(TWEET)
    if status:
        print("Blue Tweet Button Found")
    else:
        print("Blue tweet Button Not found")
        return status

    closeTab()
    print("Tab closed")
    status = findNClick(ALREADY_TWEETED, timer=TIMER_FAST)

    return status


# 4-5. Join Amara Telegram
# По умолчанию: JOIN AMARA GROUP, TIMER - 30 SEC
# Чтобы выполнить 5 пункт (Amara Channel) передать аргумент FLAG
def joinAmara(flag=0):
    status = DEFAULT

    path = JOIN_AMARA_GROUP
    timer = TIMER
    button = JOIN_AMARA_GROUP_CLICK
    continue_button = JOIN_AMARA_GROUP_CONTINUE
    if flag:
        path = JOIN_AMARA_CHANNEL
        timer = TIMER_SLOW
        button = JOIN_AMARA_CHANNEL_CLICK
        continue_button = JOIN_AMARA_CHANNEL_CONTINUE

    # Open Link
    status = findNClick(path, timer=TIMER_FAST)
    if status:
        print("Link Found")
    else:
        print("Link Not Found")
        return status
    status = findNClick(button, timer=TIMER_FAST)
    if status:
        print("Button Found")
    else:
        print("Button Not Found")
        return status

    # Continue
    pyautogui.sleep(timer)
    closeTab()
    status = findNClick(continue_button)
    if status:
        print("Continue button Found")
    else:
        print("Continue button Not found")
        return status

    return status


# 6 - 7. Follow Impossible Finance on Twitter
def followNRetweetFinance():
    status = DEFAULT

    # Open link
    status = moveToNClick(RETWEET_FINANCE, RETWEET_FINANCE_CLICK, timer=TIMER_FAST)

    # Follow Finance
    if FLAG:
        status = findNClick(OPTIONS)
    if FLAG:
        status = findNClick(FOLLOW_FINANCE)

    # Retweet
    if FLAG:
        keyboard.send("pagedown")
        status = findNClick(RETWEET)
    if FLAG:
        status = findNClick(RETWEET_FINANCE_CLICK_TWITTER, timer=TIMER_FAST)
    return FLAG


# 8-9. Visit Amara Official Wepsite
# при вызове для Amara medium передать FLAG как аргумент
# по умолчанию открывает Official Website
def visitAmara(flag=0):
    status = DEFAULT

    # Open link
    path = VISIT_AMARA
    if flag:
        path = VISIT_AMARA_MEDIUM

    status = findNClick(path, timer=TIMER_FAST)
    if status:
        print("PATH clicked")
    else:
        print("PATH not found. Retry...")
        keyboard.send("pageup")
        status = findNClick(path, timer=TIMER_FAST)
        if status:
            print("PATH clicked")
        else:
            print("PATH not found")
            return status
    if flag:
        status = findNClick(CLICK_HERE)
        if status:
            print("CLICK_HERE clicked")
        else:
            print("CLICK_HERE not found")
            return status
    else:
        # pyautogui.scroll(5)
        pyautogui.sleep(1)
        # keyboard.send("pagedown")
        status = findNClick(VISIT_AMARA_CLICK)
        if status:
            print("VISIT_AMARA_CLICK clicked")
        else:
            print("VISIT_AMARA_CLICK not found")
            print("Retry")
            keyboard.send("pageup")
            status = findNClick(VISIT_AMARA_CLICK)
            if status:
                print("FOUND")
            else:
                print("VISIT_AMARA_CLICK not found")
                return status
            return status

    # Wait and Close
    # Continue
    # print(status)
    pyautogui.sleep(TIMER)
    closeTab()
    status = findNClick(CONTINUE_BUTTON)
    if status:
        print("CONTINUE_BUTTON clicked")
    else:
        print("CONTINUE_BUTTON not found")
        return status

    return FLAG


# 10. Create a Meme for Amara ...
def createMeme():
    status = DEFAULT

    # Open Link
    status = findNClick(CREATE_MEME, timer=TIMER_FAST)
    if status:
        print("CREATE_MEME clicked")
    else:
        print("CREATE_MEME not found")
        print("retry...")
        # pyautogui.scroll(6)

        status = findNClick(CREATE_MEME, timer=TIMER_FAST)
        if status:
            print("FOUND")
            # pyautogui.moveTo(1000, 600, 1)
        else:
            print("NOT FOUND")
            return status

    status = findNClick(UPLOAD_MEME, timer=TIMER_FAST)
    if status:
        print("UPLOAD_MEME clicked")
        pyautogui.moveTo(1000, 600, 1)
    else:
        print("UPLOAD_MEME not found")
        print("retry...")
        # pyautogui.scroll(6)
        # keyboard.send("pagedown")
        status = findNClick(UPLOAD_MEME, timer=TIMER_FAST)
        if status:
            print("FOUND")
        else:
            print("NOT FOUND")
            return status

    status = findNClick(UPLOAD_FILE, timer=TIMER_FAST)
    if status:
        print("UPLOAD_FILE clicked")
    else:
        print("UPLOAD_FILE not found")
        return status

    # Choose Image
    status = findNClick(CHOOSE_IMAGE, timer=TIMER_FAST)
    if status:
        print("CHOOSE_IMAGE clicked")
        keyboard.send("right")
        keyboard.send("delete")
        pyautogui.moveTo(1000, 600, 1)
    else:
        print("CHOOSE_IMAGE not found")
        return status
    #
    # pyautogui.moveTo(FILE_BUTTON)
    # pyautogui.sleep(0.2)
    # status = findNClick(CHOOSE_IMAGE)

    status = findNClick(CHOOSE_IMAGE, timer=TIMER_FAST)
    if status:
        print("CHOOSE_IMAGE clicked")
        keyboard.send("right")
        keyboard.send("enter")
    else:
        print("CHOOSE_IMAGE not found")
        return status

    # Continue
    if check(CHECK):
        # pyautogui.scroll(80)
        pyautogui.sleep(5)
        status = findNClick(CONTUNUE_CREATE_MEME)
        if status:
            print("CONTINUE_BUTTON clicked")
        else:
            print("CONTINUE_BUTTON not found")
            print("retry...")
            keyboard.send("pagedown")
            status = findNClick(CONTUNUE_CREATE_MEME, timer=TIMER_FAST)
            if status:
                print("FOUND")
            else:
                print("NOT FOUND")
                return status

    return FLAG


# 11-13. Stay Active in the Amara Telegram Community - по умолчанию
# чтобы выполнить 12 (Join Impossible Finance ... CHANNEL) передать аргумент FINCHANNEL
# чтобы выполнить 13 (Join Impossible Finance ... GROUP) передать аргумент FINGROUP
def impossibleFinance(flag=0):
    status = DEFAULT

    link = STAY_ACTIVE
    button = CHAT_NOW
    timer = TIMER_SLOW

    if flag == FINCHANNEL:
        link = JOIN_FINANCE_CHANNEL
        button = CLICK_HERE
        timer = TIMER_FAST
    elif flag == FINGROUP:
        link = JOIN_FINANCE_GROUP
        button = JOIN_AMARA_GROUP_CLICK
        timer = TIMER_FAST

    # Open Link
    status = findNClick(link)
    if FLAG:
        status = findNClick(button)

    # Wait and Close
    # Continue
    if FLAG:
        pyautogui.sleep(timer)
        closeTab()
        status = findNClick(CONTINUE_BUTTON, timer=TIMER_FAST)

    return FLAG


def followAnn():
    # Open link
    status = DEFAULT

    status = moveToNClick(FOLLOW_ANN, FOLLOW_ANN_CLICK, timer=TIMER_FAST)
    if status:
        print("FOLLOW ANN clicked")
    else:
        print("FOLLOW ANN not found")
        return status

    # Follow
    status = findNClick(FOLLOW_BUTTON_ENG)
    if status:
        print("FOLLOW clicked")
    else:
        print("FOLLOW not found")
        return status

    pyautogui.sleep(2)
    closeTab()

    return status


# Last
def lastOne():
    status = DEFAULT

    # Open link
    status = findNClick(JOIN_LAST, timer=TIMER_FAST)
    if status:
        print("JOIN_LAST clicked")
    else:
        print("JOIN_LAST not found")
        return status

    # pageDown(OPENED_LAST, 1)
    # pyautogui.scroll(50)
    pyautogui.sleep(1)
    keyboard.send("pagedown")
    status = findNClick(LAST_CLICK, timer=TIMER_FAST)
    if status:
        print("LAST CLICK clicked")
        pyautogui.sleep(TIMER_SLOW)
        closeTab()
    else:
        print("LAST CLICK not found")
        return status
    status = findNClick(CONTINUE_BUTTON, timer=TIMER_FAST)
    if status:
        print("CONTINUE_BUTTON clicked")
    else:
        print("CONTINUE_BUTTON not found")
        return status

    return FLAG
