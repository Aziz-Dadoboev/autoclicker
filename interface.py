from tkinter import *
from tkinter import messagebox

from funcs import *

status = FLAG


def callFunc(num):
    if num == 16:
        test()

    if num == 2 or num == 1:
        joinAmara()

    if num == 3 or num == 1:
        joinAmara(FLAG)

    if num == 4 or num == 1:
        tweetAmara()

    if num == 5 or num == 1:
        retweetAmara()
        closeTab()

    if num == 6 or num == 1:
        followAmara()
        findNClick(PLUS_TWO, timer=TIMER_FAST)
        findNClick(PLUS_THREE, timer=TIMER_FAST)
        pyautogui.sleep(2)

    if num == 7 or num == 1:
        followNRetweetFinance()
        closeTab()
        findNClick(PLUS_THREE_SEC, timer=TIMER_FAST)

    if num == 8 or num == 1:
        keyboard.send("pagedown")
        keyboard.send("pagedown")
        followAnn()
        findNClick(PLUS_TWO, timer=TIMER_FAST)

    if num == 9 or num == 1:
        visitAmara(FLAG)
    if num == 10 or num == 1:
        createMeme()
    if num == 11 or num == 1:
        impossibleFinance()
    if num == 12 or num == 1:
        impossibleFinance(FINCHANNEL)
    if num == 13 or num == 1:
        impossibleFinance(FINGROUP)
    if num == 14 or num == 1:
        lastOne()

    if num == 15 or num == 1:
        keyboard.send("pageup")
        visitAmara()

    return FLAG


def test():
    pyautogui.sleep(3)
    # print(pyautogui.position())
    # keyboard.send("pagedown")
    # keyboard.send("pagedown")
    # pyautogui.scroll(1)


#
# while status:
#     print("\n\n1. Everything - Все!")
#
#     print("2. Join Amara on Telegram Discussion Group")
#     print("3. Join Amara on Telegram Announcement Channel")
#     print("4. Tweet Amara on Twitter")
#     print("5. Retweet Amara on Twitter")
#     print("6. Follow Amara on Twitter & Set Up Profile")
#     print("7. Follow and Retweet impossiblefi on Twitter")
#     print("8. Follow impossiblefiAnn on Twitter")
#     print("9. Visit Amara Medium")
#     print("10. Create a meme for Amara")
#     print("11. Stay active in the Amara")
#     print("12. Join Impossible Finance Telegram Channel")
#     print("13. Join Impossible Finance Telegram Group")
#     print("14. Join impossible Finance Local Group")
#     print("15. Visit Amara Official Website")
#
#     print("0. Exit")
#
#     status = int(input("\nВыберите один пункт из меню: "))
#     if 0 < status < 17:
#         status = callFunc(status)

# root.configure(bg="Black")


# def change(button):
#     button['text'] = "Изменено"
#     button['bg'] = '#000000'
#     button['activebackground'] = '#555555'
#     button['fg'] = '#ffffff'
#     button['activeforeground'] = '#ffffff'

def clicked(num):
    callFunc(num)


def start():
    root = Tk()
    root.title("AutoClicker IMG")
    # root.geometry("350x300+300+40")

    canvas = Canvas(root, width=600, height=500)
    scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = Frame(canvas)
    # group of widgets

    # 1. All
    allButton = Button(frame, text="All of them",
                       width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    allButton.config(command=lambda: clicked(1))
    allButton.pack()

    # 2. Join Amara on Telegram Discussion Group
    joinAmaraButton = Button(frame, text="Join Amara ... Group",
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    joinAmaraButton.config(command=lambda: clicked(2))
    joinAmaraButton.pack()

    # 3. Join Amara on Telegram Announcement Channel
    joinAmaraChannelButton = Button(frame, text="Join Amara ... Channel",
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    joinAmaraChannelButton.config(command=lambda: clicked(3))
    joinAmaraChannelButton.pack()

    # 4. Tweet Amara on Twitter
    tweetAmaraButton = Button(frame, text="Tweet Amara on Twitter",
                              width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    tweetAmaraButton.config(command=lambda: clicked(4))
    tweetAmaraButton.pack()

    # 5. Retweet Amara on Twitter
    retweetAmaraButton = Button(frame, text="Retweet Amara on Twitter",
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    retweetAmaraButton.config(command=lambda: clicked(5))
    retweetAmaraButton.pack()

    # 6. Follow Amara on Twitter & Set Up Profile
    followAmaraButton = Button(frame, text="Follow Amara & Set Up Profile",
                               width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    followAmaraButton.config(command=lambda: clicked(6))
    followAmaraButton.pack()

    # 7. Follow and Retweet impossiblefi on Twitter
    followImpossibleButton = Button(frame, text="Follow & Retweet impossiblefi",
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    followImpossibleButton.config(command=lambda: clicked(7))
    followImpossibleButton.pack()

    # 8. Follow impossiblefiAnn on Twitter
    followAnnButton = Button(frame, text="Follow impossiblefiAnn on Twitter",
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    followAnnButton.config(command=lambda: clicked(8))
    followAnnButton.pack()

    # 9. Visit Amara Medium
    visitAmaraButton = Button(frame, text="Visit Amara Medium",
                              width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    visitAmaraButton.config(command=lambda: clicked(9))
    visitAmaraButton.pack()

    # 10. Create a meme for Amara
    createMemeButton = Button(frame, text="Create Meme", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    createMemeButton.config(command=lambda: clicked(10))
    createMemeButton.pack()

    # 11. Stay active in the Amara
    stayActiveButton = Button(frame, text="Stay active in the Amara",
                              width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    stayActiveButton.config(command=lambda: clicked(11))
    stayActiveButton.pack()

    # 12. Join Impossible Finance Telegram Channel
    joinImpossibleChannelButton = Button(frame, text="Join Impossible ... Channel",
                                         width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    joinImpossibleChannelButton.config(command=lambda: clicked(12))
    joinImpossibleChannelButton.pack()

    # 13. Join Impossible Finance Telegram Group
    joinImpossibleGroupButton = Button(frame, text="Join Impossible ... Group",
                                       width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    joinImpossibleGroupButton.config(command=lambda: clicked(13))
    joinImpossibleGroupButton.pack()

    # 14. Join impossible Finance Local Group
    joinLocalButton = Button(frame, text="Join ... Local Group",
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    joinLocalButton.config(command=lambda: clicked(14))
    joinLocalButton.pack()

    # 15. Visit Amara Official Website
    visitAmaraButton = Button(frame, text="Visit Amara Official Website",
                              width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
    visitAmaraButton.config(command=lambda: clicked(15))
    visitAmaraButton.pack()

    # put the frame in the canvas
    canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canvas.pack(fill='both', expand=True, side='left')
    # scroll_y['command'] = canvas.yview()
    scroll_y.pack(fill='y', side='right')

    def on_vertical(event):
        canvas.config(yscrollincrement=0.5)
        canvas.yview_scroll(-1 * event.delta, 'units')

    canvas.bind_all('<MouseWheel>', on_vertical)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
