import sys
import tkinter as tk
import tkinter.ttk as ttk
import income_tax_support

import xlsxwriter as xls

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = View (root)
    income_tax_support.init(root, top)
    root.mainloop() 



class View:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Times New Roman} -size 20 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
                 
        img = tk.PhotoImage(file="icon/incometax.png")
        top.geometry("798x629+322+66")
        top.title("Income Tax Calculator")
        top.iconphoto(top,img)
        top.configure(background="#27707f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0,0)

        self.eq1 = tk.StringVar()
        self.eq2 = tk.StringVar()
        self.eq12 = tk.StringVar()
        self.eq3 = tk.StringVar()

        self.v = tk.IntVar()

        self.eq1.set("")
        self.eq2.set("")
        self.eq12.set("")
        self.eq3.set("")

        self.L1 = tk.Label(top)
        self.L1.place(relx=0.0, rely=0.0, height=51, width=804)
        self.L1.configure(activebackground="#f9f9f9")
        self.L1.configure(activeforeground="black")
        self.L1.configure(background="#000000")
        self.L1.configure(disabledforeground="#a3a3a3")
        self.L1.configure(font=font13)
        self.L1.configure(foreground="#ffffff")
        self.L1.configure(highlightbackground="#d9d9d9")
        self.L1.configure(highlightcolor="black")
        self.L1.configure(text='''INCOME TAX CALCULATOR''')
        self.L1.configure(width=804)

        self.L_un = tk.Label(top)
        self.L_un.place(relx=0.0, rely=0.0, height=51, width=100)
        self.L_un.configure(activebackground="#f9f9f9")
        self.L_un.configure(activeforeground="black")
        self.L_un.configure(background="#000000")
        self.L_un.configure(disabledforeground="#a3a3a3")
        self.L_un.configure(font=font11)
        self.L_un.configure(foreground="#ffffff")
        self.L_un.configure(highlightbackground="#d9d9d9")
        self.L_un.configure(highlightcolor="black")
        self.L_un.configure(text='''Username''')
        self.L_un.configure(width=804)


        self.B_set = tk.Button(top)
        self.B_set.place(relx=0.900, rely=0.004, height=45, width=45)
        self.B_set.configure(activebackground="#ececec")
        self.B_set.configure(activeforeground="#000000")
        self.B_set.configure(background="#27707f")
        self.B_set.configure(disabledforeground="#a3a3a3")
        self.B_set.configure(font=font10)
        self.B_set.configure(foreground="#ffffff")
        self.B_set.configure(highlightbackground="#d9d9d9")
        self.B_set.configure(highlightcolor="black")
        self.B_set.configure(pady="0")
        self.B_set.configure(relief="flat")
        self.img = tk.PhotoImage(file="./icon/setting.png")
        self.B_set.configure(image=self.img)
        self.B_set.configure(command=self.setting)

        self.L2_3 = tk.Label(top)
        self.L2_3.place(relx=0.01, rely=0.095, height=21, width=80)
        self.L2_3.configure(activebackground="#f9f9f9")
        self.L2_3.configure(activeforeground="black")
        self.L2_3.configure(background="#000000")
        self.L2_3.configure(disabledforeground="#a3a3a3")
        self.L2_3.configure(font=font11)
        self.L2_3.configure(foreground="#ffffff")
        self.L2_3.configure(highlightbackground="#d9d9d9")
        self.L2_3.configure(highlightcolor="black")
        self.L2_3.configure(justify='left')
        self.L2_3.configure(text='''Name:''')

        self.E1_n = tk.Entry(top)
        self.E1_n.place(relx=0.121, rely=0.095,height=22, relwidth=0.18)
        self.E1_n.configure(background="#c0d1ea")
        self.E1_n.configure(disabledbackground="#c0d1ea")
        self.E1_n.configure(disabledforeground="#afafaf")
        self.E1_n.configure(font="TkFixedFont")
        self.E1_n.configure(foreground="#000000")
        self.E1_n.configure(highlightbackground="#000000")
        self.E1_n.configure(highlightcolor="black")
        self.E1_n.configure(highlightthickness="2")
        self.E1_n.configure(insertbackground="black")
        self.E1_n.configure(relief="flat")
        self.E1_n.configure(selectbackground="#c4c4c4")
        self.E1_n.configure(selectforeground="black")

        self.L2_4 = tk.Label(top)
        self.L2_4.place(relx=0.310, rely=0.095, height=21, width=80)
        self.L2_4.configure(activebackground="#f9f9f9")
        self.L2_4.configure(activeforeground="black")
        self.L2_4.configure(background="#000000")
        self.L2_4.configure(disabledforeground="#a3a3a3")
        self.L2_4.configure(font=font11)
        self.L2_4.configure(foreground="#ffffff")
        self.L2_4.configure(highlightbackground="#d9d9d9")
        self.L2_4.configure(highlightcolor="black")
        self.L2_4.configure(justify='left')
        self.L2_4.configure(text='''PAN No.:''')

        self.E1_p = tk.Entry(top)
        self.E1_p.place(relx=0.421, rely=0.095,height=22, relwidth=0.25)
        self.E1_p.configure(background="#c0d1ea")
        self.E1_p.configure(disabledbackground="#c0d1ea")
        self.E1_p.configure(disabledforeground="#afafaf")
        self.E1_p.configure(font="TkFixedFont")
        self.E1_p.configure(foreground="#000000")
        self.E1_p.configure(highlightbackground="#000000")
        self.E1_p.configure(highlightcolor="black")
        self.E1_p.configure(highlightthickness="2")
        self.E1_p.configure(insertbackground="black")
        self.E1_p.configure(relief="flat")
        self.E1_p.configure(selectbackground="#c4c4c4")
        self.E1_p.configure(selectforeground="black")





        self.L2_1 = tk.Label(top)
        self.L2_1.place(relx=0.476, rely=0.143, height=21, width=154)
        self.L2_1.configure(activebackground="#f9f9f9")
        self.L2_1.configure(activeforeground="black")
        self.L2_1.configure(background="#000000")
        self.L2_1.configure(disabledforeground="#a3a3a3")
        self.L2_1.configure(font=font11)
        self.L2_1.configure(foreground="#ffffff")
        self.L2_1.configure(highlightbackground="#d9d9d9")
        self.L2_1.configure(highlightcolor="black")
        self.L2_1.configure(justify='left')
        self.L2_1.configure(text='''Financial Year :''')
  
        
        fy_list = ['2018-2019','2019-2020','2020-2021','2021-2022']
        self.CB_1 = ttk.Combobox(top)
        self.CB_1.place(relx=0.686, rely=0.143, height=21, width=130)
        self.CB_1.configure(value=fy_list)
        self.CB_1.current()

        self.L3 = tk.Label(top)
        self.L3.place(relx=0.0, rely=0.143, height=21, width=144)
        self.L3.configure(activebackground="#f9f9f9")
        self.L3.configure(activeforeground="black")
        self.L3.configure(background="#000000")
        self.L3.configure(disabledforeground="#a3a3a3")
        self.L3.configure(font=font11)
        self.L3.configure(foreground="#ffffff")
        self.L3.configure(highlightbackground="#d9d9d9")
        self.L3.configure(highlightcolor="black")
        self.L3.configure(justify='left')
        self.L3.configure(text='''Select Your Age :''')
        

        self.E1_Age = tk.Entry(top)
        self.E1_Age.place(relx=0.188, rely=0.143,height=22, relwidth=0.25)
        self.E1_Age.configure(background="#c0d1ea")
        self.E1_Age.configure(disabledbackground="#c0d1ea")
        self.E1_Age.configure(disabledforeground="#afafaf")
        self.E1_Age.configure(font="TkFixedFont")
        self.E1_Age.configure(foreground="#000000")
        self.E1_Age.configure(highlightbackground="#000000")
        self.E1_Age.configure(highlightcolor="black")
        self.E1_Age.configure(highlightthickness="2")
        self.E1_Age.configure(insertbackground="black")
        self.E1_Age.configure(relief="flat")
        self.E1_Age.configure(selectbackground="#c4c4c4")
        self.E1_Age.configure(selectforeground="black")


        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.0, rely=0.195, relwidth=1.004)

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=-0.013, rely=0.714, relwidth=1.004, relheight=0.003)

        self.L4 = tk.Label(top)
        self.L4.place(relx=0.013, rely=0.27, height=31, width=174)
        self.L4.configure(activebackground="#f9f9f9")
        self.L4.configure(activeforeground="black")
        self.L4.configure(background="#000000")
        self.L4.configure(borderwidth="5")
        self.L4.configure(disabledforeground="#a3a3a3")
        self.L4.configure(font=font11)
        self.L4.configure(foreground="#ffffff")
        self.L4.configure(highlightbackground="#d184ce")
        self.L4.configure(highlightcolor="#e297e5")
        self.L4.configure(highlightthickness="10")
        self.L4.configure(text='''Gross Salary :''')
        self.L4.configure(width=174)

        self.E1 = tk.Entry(top)
        self.E1.place(relx=0.238, rely=0.27,height=30, relwidth=0.18)
        self.E1.configure(background="#c0d1ea")
        self.E1.configure(disabledbackground="#c0d1ea")
        self.E1.configure(disabledforeground="#afafaf")
        self.E1.configure(font="TkFixedFont")
        self.E1.configure(foreground="#000000")
        self.E1.configure(highlightbackground="#000000")
        self.E1.configure(highlightcolor="black")
        self.E1.configure(highlightthickness="3")
        self.E1.configure(insertbackground="black")
        self.E1.configure(relief="flat")
        self.E1.configure(selectbackground="#c4c4c4")
        self.E1.configure(selectforeground="black")
        
        self.L5 = tk.Label(top)
        self.L5.place(relx=0.013, rely=0.334, height=31, width=174)
        self.L5.configure(activebackground="#f9f9f9")
        self.L5.configure(activeforeground="black")
        self.L5.configure(background="#000000")
        self.L5.configure(borderwidth="5")
        self.L5.configure(disabledforeground="#a3a3a3")
        self.L5.configure(font=font11)
        self.L5.configure(foreground="#ffffff")
        self.L5.configure(highlightbackground="#d184ce")
        self.L5.configure(highlightcolor="#e297e5")
        self.L5.configure(highlightthickness="10")
        self.L5.configure(text='''Exemption from Salary :''')

        self.E2 = tk.Entry(top)
        self.E2.place(relx=0.238, rely=0.334,height=30, relwidth=0.18)
        self.E2.configure(background="#c0d1ea")
        self.E2.configure(disabledbackground="#c0d1ea")
        self.E2.configure(disabledforeground="#afafaf")
        self.E2.configure(font="TkFixedFont")
        self.E2.configure(foreground="#000000")
        self.E2.configure(highlightbackground="#000000")
        self.E2.configure(highlightcolor="black")
        self.E2.configure(highlightthickness="3")
        self.E2.configure(insertbackground="black")
        self.E2.configure(relief="flat")
        self.E2.configure(selectbackground="#c4c4c4")
        self.E2.configure(selectforeground="black")

        self.L6 = tk.Label(top)
        self.L6.place(relx=0.013, rely=0.397, height=31, width=174)
        self.L6.configure(activebackground="#f9f9f9")
        self.L6.configure(activeforeground="black")
        self.L6.configure(background="#000000")
        self.L6.configure(borderwidth="5")
        self.L6.configure(disabledforeground="#a3a3a3")
        self.L6.configure(font=font11)
        self.L6.configure(foreground="#ffffff")
        self.L6.configure(highlightbackground="#d184ce")
        self.L6.configure(highlightcolor="#e297e5")
        self.L6.configure(highlightthickness="10")
        self.L6.configure(text='''Income from Interest :''')

        self.E3 = tk.Entry(top)
        self.E3.place(relx=0.238, rely=0.397,height=30, relwidth=0.18)
        self.E3.configure(background="#c0d1ea")
        self.E3.configure(disabledbackground="#c0d1ea")
        self.E3.configure(disabledforeground="#afafaf")
        self.E3.configure(font="TkFixedFont")
        self.E3.configure(foreground="#000000")
        self.E3.configure(highlightbackground="#000000")
        self.E3.configure(highlightcolor="black")
        self.E3.configure(highlightthickness="3")
        self.E3.configure(insertbackground="black")
        self.E3.configure(relief="flat")
        self.E3.configure(selectbackground="#c4c4c4")
        self.E3.configure(selectforeground="black")

        self.L7 = tk.Label(top)
        self.L7.place(relx=0.013, rely=0.461, height=31, width=174)
        self.L7.configure(activebackground="#f9f9f9")
        self.L7.configure(activeforeground="black")
        self.L7.configure(background="#000000")
        self.L7.configure(borderwidth="5")
        self.L7.configure(disabledforeground="#a3a3a3")
        self.L7.configure(font=font11)
        self.L7.configure(foreground="#ffffff")
        self.L7.configure(highlightbackground="#d184ce")
        self.L7.configure(highlightcolor="#e297e5")
        self.L7.configure(highlightthickness="10")
        self.L7.configure(text='''Other Income :''')

        self.E4 = tk.Entry(top)
        self.E4.place(relx=0.238, rely=0.461,height=30, relwidth=0.18)
        self.E4.configure(background="#c0d1ea")
        self.E4.configure(disabledbackground="#c0d1ea")
        self.E4.configure(disabledforeground="#afafaf")
        self.E4.configure(font="TkFixedFont")
        self.E4.configure(foreground="#000000")
        self.E4.configure(highlightbackground="#000000")
        self.E4.configure(highlightcolor="black")
        self.E4.configure(highlightthickness="3")
        self.E4.configure(insertbackground="black")
        self.E4.configure(relief="flat")
        self.E4.configure(selectbackground="#c4c4c4")
        self.E4.configure(selectforeground="black")

        self.L8 = tk.Label(top)
        self.L8.place(relx=0.0, rely=0.525, height=31, width=184)
        self.L8.configure(activebackground="#f9f9f9")
        self.L8.configure(activeforeground="black")
        self.L8.configure(background="#000000")
        self.L8.configure(borderwidth="5")
        self.L8.configure(disabledforeground="#a3a3a3")
        self.L8.configure(font=font11)
        self.L8.configure(foreground="#ffffff")
        self.L8.configure(highlightbackground="#d184ce")
        self.L8.configure(highlightcolor="#e297e5")
        self.L8.configure(highlightthickness="10")
        self.L8.configure(text='''Interest paid on Home Loan :''')
        self.L8.configure(width=184)

        self.E5 = tk.Entry(top)
        self.E5.place(relx=0.238, rely=0.525,height=30, relwidth=0.18)
        self.E5.configure(background="#c0d1ea")
        self.E5.configure(disabledbackground="#c0d1ea")
        self.E5.configure(disabledforeground="#afafaf")
        self.E5.configure(font="TkFixedFont")
        self.E5.configure(foreground="#000000")
        self.E5.configure(highlightbackground="#000000")
        self.E5.configure(highlightcolor="black")
        self.E5.configure(highlightthickness="3")
        self.E5.configure(insertbackground="black")
        self.E5.configure(relief="flat")
        self.E5.configure(selectbackground="#c4c4c4")
        self.E5.configure(selectforeground="black")

        self.L9 = tk.Label(top)
        self.L9.place(relx=0.013, rely=0.588, height=31, width=174)
        self.L9.configure(activebackground="#f9f9f9")
        self.L9.configure(activeforeground="black")
        self.L9.configure(background="#000000")
        self.L9.configure(borderwidth="5")
        self.L9.configure(disabledforeground="#a3a3a3")
        self.L9.configure(font=font11)
        self.L9.configure(foreground="#ffffff")
        self.L9.configure(highlightbackground="#d184ce")
        self.L9.configure(highlightcolor="#e297e5")
        self.L9.configure(highlightthickness="10")
        self.L9.configure(text='''Rental Income Received :''')

        self.E6 = tk.Entry(top)
        self.E6.place(relx=0.238, rely=0.588,height=30, relwidth=0.18)
        self.E6.configure(background="#c0d1ea")
        self.E6.configure(disabledbackground="#c0d1ea")
        self.E6.configure(disabledforeground="#afafaf")
        self.E6.configure(font="TkFixedFont")
        self.E6.configure(foreground="#000000")
        self.E6.configure(highlightbackground="#000000")
        self.E6.configure(highlightcolor="black")
        self.E6.configure(highlightthickness="3")
        self.E6.configure(insertbackground="black")
        self.E6.configure(relief="flat")
        self.E6.configure(selectbackground="#c4c4c4")
        self.E6.configure(selectforeground="black")

        self.L10 = tk.Label(top)
        self.L10.place(relx=0.013, rely=0.652, height=31, width=174)
        self.L10.configure(activebackground="#f9f9f9")
        self.L10.configure(activeforeground="black")
        self.L10.configure(background="#000000")
        self.L10.configure(borderwidth="5")
        self.L10.configure(disabledforeground="#a3a3a3")
        self.L10.configure(font=font11)
        self.L10.configure(foreground="#ffffff")
        self.L10.configure(highlightbackground="#d184ce")
        self.L10.configure(highlightcolor="#e297e5")
        self.L10.configure(highlightthickness="10")
        self.L10.configure(text='''Interest Paid on Loan :''')

        self.E7 = tk.Entry(top)
        self.E7.place(relx=0.238, rely=0.652,height=30, relwidth=0.18)
        self.E7.configure(background="#c0d1ea")
        self.E7.configure(disabledbackground="#c0d1ea")
        self.E7.configure(disabledforeground="#afafaf")
        self.E7.configure(font="TkFixedFont")
        self.E7.configure(foreground="#000000")
        self.E7.configure(highlightbackground="#000000")
        self.E7.configure(highlightcolor="black")
        self.E7.configure(highlightthickness="3")
        self.E7.configure(insertbackground="black")
        self.E7.configure(relief="flat")
        self.E7.configure(selectbackground="#c4c4c4")
        self.E7.configure(selectforeground="black")

        self.L11 = tk.Label(top)
        self.L11.place(relx=0.476, rely=0.27, height=31, width=224)
        self.L11.configure(activebackground="#f9f9f9")
        self.L11.configure(activeforeground="black")
        self.L11.configure(background="#000000")
        self.L11.configure(borderwidth="5")
        self.L11.configure(disabledforeground="#a3a3a3")
        self.L11.configure(font=font11)
        self.L11.configure(foreground="#ffffff")
        self.L11.configure(highlightbackground="#d184ce")
        self.L11.configure(highlightcolor="#e297e5")
        self.L11.configure(highlightthickness="10")
        self.L11.configure(text='''Basic Deductions - 80C :''')
        
        self.E8 = tk.Entry(top)
        self.E8.place(relx=0.764, rely=0.27,height=30, relwidth=0.18)
        self.E8.configure(background="#c0d1ea")
        self.E8.configure(disabledbackground="#c0d1ea")
        self.E8.configure(disabledforeground="#afafaf")
        self.E8.configure(font="TkFixedFont")
        self.E8.configure(foreground="#000000")
        self.E8.configure(highlightbackground="#000000")
        self.E8.configure(highlightcolor="black")
        self.E8.configure(highlightthickness="3")
        self.E8.configure(insertbackground="black")
        self.E8.configure(relief="flat")
        self.E8.configure(selectbackground="#c4c4c4")
        self.E8.configure(selectforeground="black")

        self.L12 = tk.Label(top)
        self.L12.place(relx=0.476, rely=0.334, height=31, width=224)
        self.L12.configure(activebackground="#f9f9f9")
        self.L12.configure(activeforeground="black")
        self.L12.configure(background="#000000")
        self.L12.configure(borderwidth="5")
        self.L12.configure(disabledforeground="#a3a3a3")
        self.L12.configure(font=font11)
        self.L12.configure(foreground="#ffffff")
        self.L12.configure(highlightbackground="#d184ce")
        self.L12.configure(highlightcolor="#e297e5")
        self.L12.configure(highlightthickness="10")
        self.L12.configure(text='''Interest from Deposits - 80TTA :''')

        self.E9 = tk.Entry(top)
        self.E9.place(relx=0.764, rely=0.334,height=30, relwidth=0.18)
        self.E9.configure(background="#c0d1ea")
        self.E9.configure(disabledbackground="#c0d1ea")
        self.E9.configure(disabledforeground="#afafaf")
        self.E9.configure(font="TkFixedFont")
        self.E9.configure(foreground="#000000")
        self.E9.configure(highlightbackground="#000000")
        self.E9.configure(highlightcolor="black")
        self.E9.configure(highlightthickness="3")
        self.E9.configure(insertbackground="black")
        self.E9.configure(relief="flat")
        self.E9.configure(selectbackground="#c4c4c4")
        self.E9.configure(selectforeground="black")

        self.L13 = tk.Label(top)
        self.L13.place(relx=0.476, rely=0.397, height=31, width=224)
        self.L13.configure(activebackground="#f9f9f9")
        self.L13.configure(activeforeground="black")
        self.L13.configure(background="#000000")
        self.L13.configure(borderwidth="5")
        self.L13.configure(disabledforeground="#a3a3a3")
        self.L13.configure(font=font11)
        self.L13.configure(foreground="#ffffff")
        self.L13.configure(highlightbackground="#d184ce")
        self.L13.configure(highlightcolor="#e297e5")
        self.L13.configure(highlightthickness="10")
        self.L13.configure(text='''Medical Insurance - 80D  :''')

        self.E10 = tk.Entry(top)
        self.E10.place(relx=0.764, rely=0.397,height=30, relwidth=0.18)
        self.E10.configure(background="#c0d1ea")
        self.E10.configure(disabledbackground="#c0d1ea")
        self.E10.configure(disabledforeground="#afafaf")
        self.E10.configure(font="TkFixedFont")
        self.E10.configure(foreground="#000000")
        self.E10.configure(highlightbackground="#000000")
        self.E10.configure(highlightcolor="black")
        self.E10.configure(highlightthickness="3")
        self.E10.configure(insertbackground="black")
        self.E10.configure(relief="flat")
        self.E10.configure(selectbackground="#c4c4c4")
        self.E10.configure(selectforeground="black")

        self.L14 = tk.Label(top)
        self.L14.place(relx=0.476, rely=0.461, height=31, width=224)
        self.L14.configure(activebackground="#f9f9f9")
        self.L14.configure(activeforeground="black")
        self.L14.configure(background="#000000")
        self.L14.configure(borderwidth="5")
        self.L14.configure(disabledforeground="#a3a3a3")
        self.L14.configure(font=font11)
        self.L14.configure(foreground="#ffffff")
        self.L14.configure(highlightbackground="#d184ce")
        self.L14.configure(highlightcolor="#e297e5")
        self.L14.configure(highlightthickness="10")
        self.L14.configure(text='''Donations to Charity - 80G :''')

        self.E11 = tk.Entry(top)
        self.E11.place(relx=0.764, rely=0.461,height=30, relwidth=0.18)
        self.E11.configure(background="#c0d1ea")
        self.E11.configure(disabledbackground="#c0d1ea")
        self.E11.configure(disabledforeground="#afafaf")
        self.E11.configure(font="TkFixedFont")
        self.E11.configure(foreground="#000000")
        self.E11.configure(highlightbackground="#000000")
        self.E11.configure(highlightcolor="black")
        self.E11.configure(highlightthickness="3")
        self.E11.configure(insertbackground="black")
        self.E11.configure(relief="flat")
        self.E11.configure(selectbackground="#c4c4c4")
        self.E11.configure(selectforeground="black")

        self.L15 = tk.Label(top)
        self.L15.place(relx=0.476, rely=0.525, height=31, width=224)
        self.L15.configure(activebackground="#f9f9f9")
        self.L15.configure(activeforeground="black")
        self.L15.configure(background="#000000")
        self.L15.configure(borderwidth="5")
        self.L15.configure(disabledforeground="#a3a3a3")
        self.L15.configure(font=font11)
        self.L15.configure(foreground="#ffffff")
        self.L15.configure(highlightbackground="#d184ce")
        self.L15.configure(highlightcolor="#e297e5")
        self.L15.configure(highlightthickness="10")
        self.L15.configure(text='''Interest on Educational Loan - 80E :''')

        self.E12 = tk.Entry(top)
        self.E12.place(relx=0.764, rely=0.525,height=30, relwidth=0.18)
        self.E12.configure(background="#c0d1ea")
        self.E12.configure(disabledbackground="#c0d1ea")
        self.E12.configure(disabledforeground="#afafaf")
        self.E12.configure(font="TkFixedFont")
        self.E12.configure(foreground="#000000")
        self.E12.configure(highlightbackground="#000000")
        self.E12.configure(highlightcolor="black")
        self.E12.configure(highlightthickness="3")
        self.E12.configure(insertbackground="black")
        self.E12.configure(relief="flat")
        self.E12.configure(selectbackground="#c4c4c4")
        self.E12.configure(selectforeground="black")

        self.L16 = tk.Label(top)
        self.L16.place(relx=0.476, rely=0.588, height=31, width=224)
        self.L16.configure(activebackground="#f9f9f9")
        self.L16.configure(activeforeground="black")
        self.L16.configure(background="#000000")
        self.L16.configure(borderwidth="5")
        self.L16.configure(disabledforeground="#a3a3a3")
        self.L16.configure(font=font11)
        self.L16.configure(foreground="#ffffff")
        self.L16.configure(highlightbackground="#d184ce")
        self.L16.configure(highlightcolor="#e297e5")
        self.L16.configure(highlightthickness="10")
        self.L16.configure(text='''Interest on Housing Loan - 80EEA :''')

        self.E13 = tk.Entry(top)
        self.E13.place(relx=0.764, rely=0.588,height=30, relwidth=0.18)
        self.E13.configure(background="#c0d1ea")
        self.E13.configure(disabledbackground="#c0d1ea")
        self.E13.configure(disabledforeground="#afafaf")
        self.E13.configure(font="TkFixedFont")
        self.E13.configure(foreground="#000000")
        self.E13.configure(highlightbackground="#000000")
        self.E13.configure(highlightcolor="black")
        self.E13.configure(highlightthickness="3")
        self.E13.configure(insertbackground="black")
        self.E13.configure(relief="flat")
        self.E13.configure(selectbackground="#c4c4c4")
        self.E13.configure(selectforeground="black")

        self.L17 = tk.Label(top)
        self.L17.place(relx=0.439, rely=0.652, height=31, width=254)
        self.L17.configure(activebackground="#f9f9f9")
        self.L17.configure(activeforeground="black")
        self.L17.configure(background="#000000")
        self.L17.configure(borderwidth="5")
        self.L17.configure(disabledforeground="#a3a3a3")
        self.L17.configure(font=font11)
        self.L17.configure(foreground="#ffffff")
        self.L17.configure(highlightbackground="#d184ce")
        self.L17.configure(highlightcolor="#e297e5")
        self.L17.configure(highlightthickness="10")
        self.L17.configure(text='''Employee's contribution to NPS - 80CCD :''')
        
        self.E14 = tk.Entry(top)
        self.E14.place(relx=0.764, rely=0.652,height=30, relwidth=0.18)
        self.E14.configure(background="#c0d1ea")
        self.E14.configure(disabledbackground="#c0d1ea")
        self.E14.configure(disabledforeground="#afafaf")
        self.E14.configure(font="TkFixedFont")
        self.E14.configure(foreground="#000000")
        self.E14.configure(highlightbackground="#000000")
        self.E14.configure(highlightcolor="black")
        self.E14.configure(highlightthickness="3")
        self.E14.configure(insertbackground="black")
        self.E14.configure(relief="flat")
        self.E14.configure(selectbackground="#c4c4c4")
        self.E14.configure(selectforeground="black")

        self.L18 = tk.Label(top)
        self.L18.place(relx=0.025, rely=0.731, height=31, width=154)
        self.L18.configure(activebackground="#f9f9f9")
        self.L18.configure(activeforeground="black")
        self.L18.configure(background="#000000")
        self.L18.configure(borderwidth="5")
        self.L18.configure(disabledforeground="#a3a3a3")
        self.L18.configure(font=font12)
        self.L18.configure(foreground="#ffffff")
        self.L18.configure(highlightbackground="#d184ce")
        self.L18.configure(highlightcolor="#e297e5")
        self.L18.configure(highlightthickness="10")
        self.L18.configure(text='''Total Income :''')

        self.L23 = tk.Label(top)
        self.L23.place(relx=0.226, rely=0.731, height=31, width=184)
        self.L23.configure(activebackground="#f9f9f9")
        self.L23.configure(activeforeground="black")
        self.L23.configure(background="#000000")
        self.L23.configure(borderwidth="5")
        self.L23.configure(disabledforeground="#a3a3a3")
        self.L23.configure(font=font12)
        self.L23.configure(foreground="#ffffff")
        self.L23.configure(highlightbackground="#d184ce")
        self.L23.configure(highlightcolor="#e297e5")
        self.L23.configure(highlightthickness="10")
        self.L23.configure(textvariable=self.eq1)

        self.L19 = tk.Label(top)
        self.L19.place(relx=0.025, rely=0.779, height=31, width=154)
        self.L19.configure(activebackground="#f9f9f9")
        self.L19.configure(activeforeground="black")
        self.L19.configure(background="#000000")
        self.L19.configure(borderwidth="5")
        self.L19.configure(disabledforeground="#a3a3a3")
        self.L19.configure(font=font12)
        self.L19.configure(foreground="#ffffff")
        self.L19.configure(highlightbackground="#d184ce")
        self.L19.configure(highlightcolor="#e297e5")
        self.L19.configure(highlightthickness="10")
        self.L19.configure(text='''Deductions :''')

        self.L24 = tk.Label(top)
        self.L24.place(relx=0.226, rely=0.779, height=31, width=184)
        self.L24.configure(activebackground="#f9f9f9")
        self.L24.configure(activeforeground="black")
        self.L24.configure(background="#000000")
        self.L24.configure(borderwidth="5")
        self.L24.configure(disabledforeground="#a3a3a3")
        self.L24.configure(font=font12)
        self.L24.configure(foreground="#ffffff")
        self.L24.configure(highlightbackground="#d184ce")
        self.L24.configure(highlightcolor="#e297e5")
        self.L24.configure(highlightthickness="10")
        self.L24.configure(textvariable=self.eq2)

        self.L20 = tk.Label(top)
        self.L20.place(relx=0.025, rely=0.827, height=31, width=154)
        self.L20.configure(activebackground="#f9f9f9")
        self.L20.configure(activeforeground="black")
        self.L20.configure(background="#000000")
        self.L20.configure(borderwidth="5")
        self.L20.configure(disabledforeground="#a3a3a3")
        self.L20.configure(font=font12)
        self.L20.configure(foreground="#ffffff")
        self.L20.configure(highlightbackground="#d184ce")
        self.L20.configure(highlightcolor="#e297e5")
        self.L20.configure(highlightthickness="10")
        self.L20.configure(text='''Gross Total Income :''')

        self.L25 = tk.Label(top)
        self.L25.place(relx=0.226, rely=0.827, height=31, width=184)
        self.L25.configure(activebackground="#f9f9f9")
        self.L25.configure(activeforeground="black")
        self.L25.configure(background="#000000")
        self.L25.configure(borderwidth="5")
        self.L25.configure(disabledforeground="#a3a3a3")
        self.L25.configure(font=font12)
        self.L25.configure(foreground="#ffffff")
        self.L25.configure(highlightbackground="#d184ce")
        self.L25.configure(highlightcolor="#e297e5")
        self.L25.configure(highlightthickness="10")
        self.L25.configure(textvariable=self.eq12)

        self.L21 = tk.Label(top)
        self.L21.place(relx=0.025, rely=0.89, height=51, width=154)
        self.L21.configure(activebackground="#f9f9f9")
        self.L21.configure(activeforeground="black")
        self.L21.configure(background="#000000")
        self.L21.configure(borderwidth="5")
        self.L21.configure(disabledforeground="#a3a3a3")
        self.L21.configure(font=font12)
        self.L21.configure(foreground="#ffffff")
        self.L21.configure(highlightbackground="#d184ce")
        self.L21.configure(highlightcolor="#e297e5")
        self.L21.configure(highlightthickness="10")
        self.L21.configure(text='''Payable Income Tax :''')

        self.L26 = tk.Label(top)
        self.L26.place(relx=0.226, rely=0.89, height=51, width=184)
        self.L26.configure(activebackground="#f9f9f9")
        self.L26.configure(activeforeground="black")
        self.L26.configure(background="#000000")
        self.L26.configure(borderwidth="5")
        self.L26.configure(disabledforeground="#a3a3a3")
        self.L26.configure(font=font12)
        self.L26.configure(foreground="#ffffff")
        self.L26.configure(highlightbackground="#d184ce")
        self.L26.configure(highlightcolor="#e297e5")
        self.L26.configure(highlightthickness="10")
        self.L26.configure(textvariable=self.eq3)


        

        self.B_Cal = tk.Button(top)
        self.B_Cal.place(relx=0.677, rely=0.731, height=44, width=207)
        self.B_Cal.configure(activebackground="#ececec")
        self.B_Cal.configure(activeforeground="#000000")
        self.B_Cal.configure(background="#000000")
        self.B_Cal.configure(disabledforeground="#a3a3a3")
        self.B_Cal.configure(font=font10)
        self.B_Cal.configure(foreground="#ffffff")
        self.B_Cal.configure(highlightbackground="#d9d9d9")
        self.B_Cal.configure(highlightcolor="black")
        self.B_Cal.configure(pady="0")
        self.B_Cal.configure(relief="flat")
        self.B_Cal.configure(text='''Calculate''')
        self.B_Cal.configure(command=self.calculate)

        self.B_Clr = tk.Button(top)
        self.B_Clr.place(relx=0.677, rely=0.811, height=44, width=107)
        self.B_Clr.configure(activebackground="#ececec")
        self.B_Clr.configure(activeforeground="#000000")
        self.B_Clr.configure(background="#000000")
        self.B_Clr.configure(disabledforeground="#a3a3a3")
        self.B_Clr.configure(font=font10)
        self.B_Clr.configure(foreground="#ffffff")
        self.B_Clr.configure(highlightbackground="#d9d9d9")
        self.B_Clr.configure(highlightcolor="black")
        self.B_Clr.configure(pady="0")
        self.B_Clr.configure(relief="flat")
        self.B_Clr.configure(text='''Clear''')
        self.B_Clr.configure(command=self.clear)

        self.L22 = tk.Label(top)
        self.L22.place(relx=0.013, rely=0.207, height=31, width=324)
        self.L22.configure(activebackground="#f9f9f9")
        self.L22.configure(activeforeground="black")
        self.L22.configure(background="#000000")
        self.L22.configure(disabledforeground="#a3a3a3")
        self.L22.configure(font=font10)
        self.L22.configure(foreground="#ffffff")
        self.L22.configure(highlightbackground="#d9d9d9")
        self.L22.configure(highlightcolor="black")
        self.L22.configure(justify='left')
        self.L22.configure(text='''INCOME :''')

        self.L22_2 = tk.Label(top)
        self.L22_2.place(relx=0.476, rely=0.207, height=31, width=374)
        self.L22_2.configure(activebackground="#f9f9f9")
        self.L22_2.configure(activeforeground="black")
        self.L22_2.configure(background="#000000")
        self.L22_2.configure(disabledforeground="#a3a3a3")
        self.L22_2.configure(font=font10)
        self.L22_2.configure(foreground="#ffffff")
        self.L22_2.configure(highlightbackground="#d9d9d9")
        self.L22_2.configure(highlightcolor="black")
        self.L22_2.configure(justify='left')
        self.L22_2.configure(text='''DEDUCTION :''')

        self.B_p = tk.Button(top)
        self.B_p.place(relx=0.815, rely=0.811, height=44, width=97)
        self.B_p.configure(activebackground="#ececec")
        self.B_p.configure(activeforeground="#000000")
        self.B_p.configure(background="#000000")
        self.B_p.configure(disabledforeground="#a3a3a3")
        self.B_p.configure(font=font10)
        self.B_p.configure(foreground="#ffffff")
        self.B_p.configure(highlightbackground="#d9d9d9")
        self.B_p.configure(highlightcolor="black")
        self.B_p.configure(pady="0")
        self.B_p.configure(relief="flat")
        self.B_p.configure(text='''Print''')
        self.B_p.configure(command=self.i_print)

        '''self.B_h = tk.Button(top)
                                self.B_h.place(relx=0.677, rely=0.89, height=34, width=107)
                                self.B_h.configure(activebackground="#ececec")
                                self.B_h.configure(activeforeground="#000000")
                                self.B_h.configure(background="#000000")
                                self.B_h.configure(disabledforeground="#a3a3a3")
                                self.B_h.configure(font=font10)
                                self.B_h.configure(foreground="#ffffff")
                                self.B_h.configure(highlightbackground="#d9d9d9")
                                self.B_h.configure(highlightcolor="black")
                                self.B_h.configure(pady="0")
                                self.B_h.configure(relief="flat")
                                self.B_h.configure(text='history')
                                self.B_h.configure(command=self.history)'''


        


        self.exp1 = ""
        self.exp2 = ""
        self.exp12 = ""
        self.exp3 = ""
        self.fy = ""
        self.cag = ""

        



        self.inc_tax = 0

    def income(self):
        self.inc = 0
        self.inc = self.inc + int(self.E1.get()) + int(self.E2.get()) + int(self.E3.get()) + int(self.E4.get()) + int(self.E5.get()) + int(self.E6.get()) + int(self.E7.get())
        return self.inc

    def deduct(self):
        self.dec = 0
        self.dec = self.dec + int(self.E8.get())+int(self.E9.get())+int(self.E10.get())+int(self.E11.get())+int(self.E12.get())+int(self.E13.get())+int(self.E14.get())
        return self.dec

    def ttl_income(self):

        self.ttl_inc = self.income() - self.deduct()
        
        return self.ttl_inc

    def less_rebate(self):
        print(self.inc_tax)
        #Less Rebate u/s 87A
        if self.inc_tax <= 12500:
            self.inc_tax = self.inc_tax*0
            return self.inc_tax

    def surcharge(self):

        self.cess = self.sur50 = self.sur1c = 0
        self.cess = self.cess + int(self.inc_tax*4/100)

        if 5000000 < self.ttl_income() <= 10000000:
            self.sur50 = self.sur50 + int(self.inc_tax*10/100)   

        elif self.ttl_income()>10000000:
            self.sur1c = self.sur1c + int(self.inc_tax*15/100)

        self.sur = self.cess + self.sur50 + self.sur1c
        return self.sur

    def below60(self):
        #self.inc_b2 = self.inc_b5 = self.inc_b10 = self.inc_b11 = 0

        if (self.ttl_income()<=250000):
            self.inc_tax = self.inc_tax + 0 #self.inc_b2

        if ((250000<self.ttl_income()<=500000) or (500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000)) :
            #self.inc_b5 = self.inc_b5+int((self.ttl_income()-250000)*5/100)
            self.inc_tax = self.inc_tax + int((self.ttl_income()-250000)*5/100) #self.inc_b5
            

        if((500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000)):
#            self.inc_b10 = self.inc_b10 + int((self.ttl_income()-500000)*20/100)
            self.inc_tax = self.inc_tax + int((self.ttl_income()-500000)*20/100) #self.inc_b10
            

        if(self.ttl_income()>1000000):
            #self.inc_b11 = self.inc_b11 + int((self.ttl_income()-1000000)*30/100)
            self.inc_tax = self.inc_tax + int((self.ttl_income()-1000000)*30/100) #self.inc_b11
            

        self.less_rebate()

        self.inc_tax = self.surcharge()
        return self.inc_tax

        
    def above60(self):
        if (self.ttl_income()<=300000):
            self.inc_a3 = 0
            self.inc_tax = self.inc_tax + self.inc_a3
            

        if(300000<self.ttl_income()<=500000) or (500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
            self.inc_a5 = int((self.ttl_income()-300000)*5/100)
            self.inc_tax = self.inc_tax + self.inc_a5
            

        if(500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
            self.inc_a10 = int((self.ttl_income()-500000)*20/100)
            self.inc_tax = self.inc_tax + self.inc_a10
            

        if(self.ttl_income()>1000000):
            self.inc_a11 = int((self.ttl_income()-1000000)*30/100)
            self.inc_tax = self.inc_tax + self.inc_a11
            

        self.less_rebate()
        

        self.inc_tax = self.surcharge()
        return self.inc_tax

    def above80(self):
        if (self.ttl_income()<=500000):
            self.inc_a83 = 0
            self.inc_tax = self.inc_tax + self.inc_a83
            

        if(500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
            self.inc_a810 = int((self.ttl_income()-500000)*20/100)
            self.inc_tax = self.inc_tax + self.inc_a810
            

        if(self.ttl_income()>1000000):
            self.inc_a811 = int((self.ttl_income()-1000000)*30/100)
            self.inc_tax = self.inc_tax + self.inc_a811
            

        self.inc_tax = self.surcharge()
        return self.inc_tax


    def clear(self): 
        self.inc_tax = 0
        self.exp1=self.exp2=self.exp3=self.exp12=self.cag=""  
        self.eq1.set("")
        self.eq2.set("")
        self.eq12.set("")
        self.eq3.set("")
        self.fy = ""


    def calculate(self):
        print(self.inc_tax)



        self.fy = self.fy + str(self.CB_1.get())
                

        self.exp1 = self.exp1 + str(self.income())
        self.eq1.set(self.exp1)

        self.exp2 = self.exp2 + str(self.deduct())
        self.eq2.set(self.exp2)

        self.exp12 = self.exp12 + str(self.ttl_income())
        self.eq12.set(self.exp12)

        if int(self.E1_Age.get()) < 60:
            print(self.E1_Age.get())
            self.cag = self.cag + "Citizen"
            self.exp3 = self.exp3 + str(self.below60())
            self.eq3.set(self.exp3)

        if 60 <= int(self.E1_Age.get()) < 80:
            print(self.E1_Age.get())
            self.cag = self.cag + "Senior Citizen"
            self.exp3 = self.exp3 + str(self.above60())
            self.eq3.set(self.exp3)

        if int(self.E1_Age.get()) >= 80:
            print(self.E1_Age.get())
            self.cag = self.cag + "Super Senior Citizen"
            self.exp3 = self.exp3 + str(self.above80())
            self.eq3.set(self.exp3)


    def i_print(self):

        # Create an new Excel file and add a worksheet.
        self.workbook = xls.Workbook('inc.xlsx')
        self.worksheet = self.workbook.add_worksheet()

         # Add a bold format to use to highlight cells.
        bold = self.workbook.add_format({'bold': True})

        self.worksheet.set_column('D:F', 25)

        self.worksheet.insert_image('G2', 'icon/incometax.png')

        self.worksheet.write('E2', 'INCOME TAX CALCULATOR',bold)

        
        # Write some simple text.
        self.worksheet.write('D3','Name:' ,bold)
        self.worksheet.write('E3',str(self.E1_n.get()))
        self.worksheet.write('D4', 'Financial year:',bold)
        self.worksheet.write('E4', self.CB_1.get(), bold)

        self.worksheet.write('D5', 'PAN No.:', bold)
        self.worksheet.write('E5', str(self.E1_p.get()), bold)
        self.worksheet.write('F5', self.cag, bold)

        self.worksheet.write('D7', 'Sr.No.', bold)
        self.worksheet.write('E7', 'Description', bold)
        self.worksheet.write('F7', 'Amount (in ₹)', bold)

        self.worksheet.write('D8', '1.')
        self.worksheet.write('D9', '2.')
        self.worksheet.write('D10', '3.')

        self.worksheet.write('E8', 'Total Income:')
        self.worksheet.write('E9', 'Total Deduction:')
        self.worksheet.write('E10', 'Payable Income Tax:')

        self.worksheet.write(7, 5, self.exp1)
        self.worksheet.write(8, 5, self.exp2)
        self.worksheet.write(9, 5, self.exp3)

        self.workbook.close()

    

    def setting(self):
        pass

if __name__ == '__main__':
    vp_start_gui()





