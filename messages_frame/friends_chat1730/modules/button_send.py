import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input
import modules.creating_from_frame as m_from

button_width = 70
button_height = 50
margin_left = 50
button_color = "orange"


counter_of_messages = 0

def send_message():
    global counter_of_messages
    print(counter_of_messages)
    button_label = ctk.CTkLabel(
        master = m_app.main_app, 
        text = m_input.text.get(),
        font = m_input.font_size
    )
    
    
    name = "Tosha"
    
    message1 = m_from.MessageFrame(
        master= m_app.main_app.FRAME4,
        text_of_message= name + "\n" + button_label._text
    )
    
    if counter_of_messages == 0:
        message1.grid(row = 0, column = 3, padx = 10, pady = 5)
        counter_of_messages += 1
    elif counter_of_messages > 0:
        message1.grid(row = 0 + counter_of_messages, column = 3, padx = 10, pady = 5)
        counter_of_messages += 1



send_button = ctk.CTkButton(
    master = m_app.main_app.FRAME3, 
    text ="->",
    width = button_width,
    height = button_height,
    fg_color = button_color,
    command= send_message
)

send_button.place(
    x = m_app.main_app.FRAME3._current_width // 2 + m_input.width_input // 2, 
    y = m_app.main_app.FRAME3._current_height - button_height, 
    anchor = ctk.CENTER
)