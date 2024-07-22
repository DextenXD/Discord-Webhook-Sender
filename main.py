import tkinter as tk
import time
from discord_webhook import DiscordWebhook
from tkinter import messagebox

class GUI():
  
  def __init__(self):
    #GUI setetup
    self.root = tk.Tk()
    self.root.geometry("500x500")
    
    self.root.title("Discord Webhook Raider")
    self.root.iconbitmap('./favicon.ico')
    self.root.configure(bg="#808080")
    self.label = tk.Label(self.root, text="Dicscord Webhook Raider", font=("Arial", 18), bg="#808080")
    self.label.pack(padx=10, pady=10)
    
    self.textbox = tk.Text(self.root, height=5, font=("Arial", 16), bg="#a6a6a6")
    self.textbox.pack(pady=10, padx=10)
    
    self.webhook_label = tk.Label(self.root, text="Webhook URL:", font=("Arial", 12), bg="#808080")
    self.webhook_label.pack(pady=5)    
    
    self.webhook = tk.Entry(self.root, width=100, text=("Enter your webhook", 12), bg="#a6a6a6")
    self.webhook.pack(padx=10, pady=10)
   
    self.raid_var = tk.IntVar()
    self.checkbox_raid = tk.Checkbutton(text="Raider", height=2, width=10, font=("Arial", 16), bg="#808080", variable=self.raid_var)
    self.checkbox_raid.place(x=300, y=260)
    
    self.checkbox_var = tk.IntVar()
    self.checkbox_text = tk.Checkbutton(text="One Message", height=2, width=10, font=("Arial", 16), bg="#808080", variable=self.checkbox_var)
    self.checkbox_text.place(x=30, y=260)
    

    
    self.webhookButton = tk.Button(text="Use Webhook", height=2, width=15, font=("Arial", 7), bg="#808080", command=self.get_webhook_url)
    self.webhookButton.pack()
    
    self.sendButton = tk.Button(text="Send", height=2, width=10, font=("Arial", 16), bg="#808080", command=self.check_for_value)
    self.sendButton.pack(padx=10, pady=80)
    
    self.root.mainloop()
    
  # gets the webhook url
  def get_webhook_url(self):
    self.webhook_url = self.webhook.get()
    if "https://discord.com/api/webhooks/" in self.webhook_url:
      messagebox.showinfo("ty", "Thx for giving the webhook")
    elif self.webhook_url == "":
      messagebox.showerror("ERROR", "Dont leave this empty")
    elif self.webhook_url  != "https://discord.com/api/webhooks/":
      messagebox.showerror("ERROR", "Please provide a Discord webhook")
    else:
      messagebox.showerror("ERROR", "idk even know how u got this error bro")

    
  # chekcs for value and send to webhook
  def check_for_value(self):
    if self.webhook_url:
      if self.checkbox_var.get() == 1 and self.raid_var.get() == 1:
        messagebox.showerror("ERROR", "You cant select both options!")
      elif self.raid_var.get() == 1: #radier
        while self.raid_var.get() == 1:
          time.sleep(0) # change the speed the faster the higher change on your aplication crashing 0 = fastest
          user_content = self.textbox.get(1.0, tk.END)
          webhook = DiscordWebhook(url=self.webhook_url, rate_limit_retry=True, content=(f"{user_content} *Dexten's Webhook spammer on top!*"))
          response = webhook.execute()
          time.sleep(0) # change the speed the faster the higher change on your aplication crashing 0 = fastest
      elif self.checkbox_var.get() == 1: #plain text
        user_content = self.textbox.get(1.0, tk.END)
        webhook = DiscordWebhook(url=self.webhook_url, content=user_content)
        response = webhook.execute()
      else:
        messagebox.showerror("ERROR", "try selecting a option or sumbit your webhook")
        

      

    
GUI()