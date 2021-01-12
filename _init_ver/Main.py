from Window import window
from login import login_user

# #New code 
# #Comment this section out and uncomment Previous code to go to window directly
#1------------------------------------#
login = login_user(0)
login.promptWindow.mainloop()
#1end---------------------------------#

# #Previous Code 
# #Comment this section out and uncomment New code to apply login window
#2------------------------------------#
# home = window(True)
# home.root.mainloop()
#2end---------------------------------#