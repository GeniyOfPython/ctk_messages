import customtkinter as ctk

class MessageFrame(ctk.CTkFrame):
    def __init__(self, master, text_of_message, who = None, **kwargs):
        super().__init__(master = master, **kwargs)
        self.TEXT_OF_MESSAGE = text_of_message
        self.WHO = who
        
        self.LABEL_TEXT = ctk.CTkLabel(
            master=self,
            text=self.TEXT_OF_MESSAGE
        )
        
        self.LABEL_TEXT.grid(row=0, column=0, sticky=ctk.E)
        
        # self.LABEL_USER = ctk.CTkLabel(
        #     master=self,
        #     text=self.USER_NAME
        # )
        
        # self.LABEL_USER.grid(row=1, column=1, sticky=ctk.N)
    