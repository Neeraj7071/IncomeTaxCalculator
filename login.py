import tkinter as tk
from tkinter import ttk

top = tk.Tk()
top.geometry("840x623+234+50")
top.title("Login Page")
top.configure(background="#2e5aa5")
top.resizable(0,0)

font10 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"
font11 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
"italic -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 11 -weight bold -slant roman"  \
" -underline 0 -overstrike 0"


if __name__ == '__main__':

	Lp0 = tk.Label(top)
	Lp0.place(relx=0.018, rely=0.002, height=80, width=100)
	img1 = tk.PhotoImage(file="./icon/inc.png")
	Lp0.configure(image=img1)

	

	Lp = tk.Label(top)
	Lp.place(relx=0.018, rely=0.182, height=400, width=400)
	img2 = tk.PhotoImage(file="./icon/incometax.png")
	Lp.configure(image=img2)
	
	
	
	L1 = tk.Label(top)
	L1.place(relx=0.476, rely=0.019, height=20, width=74)
	L1.configure(activebackground="#f9f9f9")
	L1.configure(activeforeground="black")
	L1.configure(background="#2e5aa5")
	L1.configure(disabledforeground="#a3a3a3")
	L1.configure(font=font10)
	L1.configure(foreground="#ffffff")
	L1.configure(highlightbackground="#d9d9d9")
	L1.configure(highlightcolor="black")
	L1.configure(text='''Username:''')

	E1 = tk.Entry(top)
	E1.place(relx=0.476, rely=0.057,height=30, relwidth=0.219)
	E1.configure(background="#a1d6ff")
	E1.configure(disabledforeground="#a3a3a3")
	E1.configure(font="TkFixedFont")
	E1.configure(foreground="#000000")
	E1.configure(highlightbackground="#000000")
	E1.configure(highlightcolor="#000000")
	E1.configure(highlightthickness="2")
	E1.configure(insertbackground="black")
	E1.configure(relief="flat")
	E1.configure(selectbackground="#c4c4c4")
	E1.configure(selectforeground="black")

	E2 = tk.Entry(top)
	E2.place(relx=0.702, rely=0.057,height=30, relwidth=0.195)
	E2.configure(background="#a1d6ff")
	E2.configure(disabledforeground="#a3a3a3")
	E2.configure(font="TkFixedFont")
	E2.configure(foreground="#000000")
	E2.configure(highlightbackground="#000000")
	E2.configure(highlightcolor="black")
	E2.configure(highlightthickness="2")
	E2.configure(insertbackground="black")
	E2.configure(relief="flat")
	E2.configure(selectbackground="#c4c4c4")
	E2.configure(selectforeground="black")

	L2 = tk.Label(top)
	L2.place(relx=0.702, rely=0.019, height=20, width=64)
	L2.configure(activebackground="#f9f9f9")
	L2.configure(activeforeground="black")
	L2.configure(background="#2e5aa5")
	L2.configure(disabledforeground="#a3a3a3")
	L2.configure(font=font10)
	L2.configure(foreground="#ffffff")
	L2.configure(highlightbackground="#d9d9d9")
	L2.configure(highlightcolor="black")
	L2.configure(text='''Password:''')



	Button3 = tk.Button(top)
	Button3.place(relx=0.476, rely=0.12, height=15, width=90)
	Button3.configure(activebackground="#ececec")
	Button3.configure(activeforeground="#000000")
	Button3.configure(background="#2e5aa5")
	Button3.configure(disabledforeground="#a3a3a3")
	Button3.configure(font=font10)
	Button3.configure(foreground="#ffffff")
	Button3.configure(highlightbackground="#d9d9d9")
	Button3.configure(highlightcolor="black")
	Button3.configure(pady="0")
	Button3.configure(relief="flat")
	Button3.configure(text='''find Username ?''')

	

	Button4 = tk.Button(top)
	Button4.place(relx=0.702, rely=0.12, height=15, width=95)
	Button4.configure(activebackground="#ececec")
	Button4.configure(activeforeground="#000000")
	Button4.configure(background="#2e5aa5")
	Button4.configure(disabledforeground="#a3a3a3")
	Button4.configure(font=font10)
	Button4.configure(foreground="#ffffff")
	Button4.configure(highlightbackground="#d9d9d9")
	Button4.configure(highlightcolor="black")
	Button4.configure(pady="0")
	Button4.configure(relief="flat")
	Button4.configure(text='''forgot Password ?''')

	Button1 = tk.Button(top)
	Button1.place(relx=0.905, rely=0.06, height=28, width=55)
	Button1.configure(activebackground="#ececec")
	Button1.configure(activeforeground="#000000")
	Button1.configure(background="#a1d6ff")
	Button1.configure(disabledforeground="#a3a3a3")
	Button1.configure(font=font10)
	Button1.configure(foreground="#000000")
	Button1.configure(highlightbackground="#d9d9d9")
	Button1.configure(highlightcolor="black")
	Button1.configure(pady="0")
	Button1.configure(relief="flat")
	Button1.configure(text='''Login''')

	TSeparator1 = ttk.Separator(top)
	TSeparator1.place(relx=0.0, rely=0.153, relwidth=1.0)
	
	L3 = tk.Label(top)
	L3.place(relx=0.607, rely=0.172, height=31, width=104)
	L3.configure(activebackground="#f9f9f9")
	L3.configure(activeforeground="black")
	L3.configure(background="#2e5aa5")
	L3.configure(disabledforeground="#a3a3a3")
	L3.configure(font=font11)
	L3.configure(foreground="#ffffff")
	L3.configure(highlightbackground="#d9d9d9")
	L3.configure(highlightcolor="black")
	L3.configure(text='''First Name:''')

	E3 = tk.Entry(top)
	E3.place(relx=0.619, rely=0.229,height=30, relwidth=0.171)
	E3.configure(background="#a1d6ff")
	E3.configure(disabledforeground="#a3a3a3")
	E3.configure(font="TkFixedFont")
	E3.configure(foreground="#000000")
	E3.configure(highlightbackground="#000000")
	E3.configure(highlightcolor="#000000")
	E3.configure(highlightthickness="2")
	E3.configure(insertbackground="black")
	E3.configure(relief="flat")
	E3.configure(selectbackground="#c4c4c4")
	E3.configure(selectforeground="black")

	L4 = tk.Label(top)
	L4.place(relx=0.786, rely=0.172, height=31, width=104)
	L4.configure(activebackground="#f9f9f9")
	L4.configure(activeforeground="black")
	L4.configure(background="#2e5aa5")
	L4.configure(disabledforeground="#a3a3a3")
	L4.configure(font=font11)
	L4.configure(foreground="#ffffff")
	L4.configure(highlightbackground="#d9d9d9")
	L4.configure(highlightcolor="black")
	L4.configure(text='''Last Name:''')

	E4 = tk.Entry(top)
	E4.place(relx=0.798, rely=0.229,height=30, relwidth=0.171)
	E4.configure(background="#a1d6ff")
	E4.configure(disabledforeground="#a3a3a3")
	E4.configure(font="TkFixedFont")
	E4.configure(foreground="#000000")
	E4.configure(highlightbackground="#000000")
	E4.configure(highlightcolor="#000000")
	E4.configure(highlightthickness="2")
	E4.configure(insertbackground="black")
	E4.configure(relief="flat")
	E4.configure(selectbackground="#c4c4c4")
	E4.configure(selectforeground="black")

	

	L5 = tk.Label(top)
	L5.place(relx=0.5, rely=0.286, height=31, width=94)
	L5.configure(activebackground="#f9f9f9")
	L5.configure(activeforeground="black")
	L5.configure(background="#2e5aa5")
	L5.configure(disabledforeground="#a3a3a3")
	L5.configure(font=font11)
	L5.configure(foreground="#ffffff")
	L5.configure(highlightbackground="#d9d9d9")
	L5.configure(highlightcolor="black")
	L5.configure(text='''Username:''')

	E5 = tk.Entry(top)
	E5.place(relx=0.619, rely=0.286,height=30, relwidth=0.35)
	E5.configure(background="#a1d6ff")
	E5.configure(disabledforeground="#a3a3a3")
	E5.configure(font="TkFixedFont")
	E5.configure(foreground="#000000")
	E5.configure(highlightbackground="#000000")
	E5.configure(highlightcolor="#000000")
	E5.configure(highlightthickness="2")
	E5.configure(insertbackground="black")
	E5.configure(relief="flat")
	E5.configure(selectbackground="#c4c4c4")
	E5.configure(selectforeground="black")

	L6 = tk.Label(top)
	L6.place(relx=0.512, rely=0.343, height=31, width=84)
	L6.configure(activebackground="#f9f9f9")
	L6.configure(activeforeground="black")
	L6.configure(background="#2e5aa5")
	L6.configure(disabledforeground="#a3a3a3")
	L6.configure(font=font11)
	L6.configure(foreground="#ffffff")
	L6.configure(highlightbackground="#d9d9d9")
	L6.configure(highlightcolor="black")
	L6.configure(text='''Password:''')

	E6 = tk.Entry(top)
	E6.place(relx=0.619, rely=0.343,height=30, relwidth=0.35)
	E6.configure(background="#a1d6ff")
	E6.configure(disabledforeground="#a3a3a3")
	E6.configure(font="TkFixedFont")
	E6.configure(foreground="#000000")
	E6.configure(highlightbackground="#000000")
	E6.configure(highlightcolor="#000000")
	E6.configure(highlightthickness="2")
	E6.configure(insertbackground="black")
	E6.configure(relief="flat")
	E6.configure(selectbackground="#c4c4c4")
	E6.configure(selectforeground="black")

	L7 = tk.Label(top)
	L7.place(relx=0.44, rely=0.400, height=31, width=144)
	L7.configure(activebackground="#f9f9f9")
	L7.configure(activeforeground="black")
	L7.configure(background="#2e5aa5")
	L7.configure(disabledforeground="#a3a3a3")
	L7.configure(font=font11)
	L7.configure(foreground="#ffffff")
	L7.configure(highlightbackground="#d9d9d9")
	L7.configure(highlightcolor="black")
	L7.configure(text='''ReType Password:''')

	E7 = tk.Entry(top)
	E7.place(relx=0.619, rely=0.400,height=30, relwidth=0.35)
	E7.configure(background="#a1d6ff")
	E7.configure(disabledforeground="#a3a3a3")
	E7.configure(font="TkFixedFont")
	E7.configure(foreground="#000000")
	E7.configure(highlightbackground="#000000")
	E7.configure(highlightcolor="#000000")
	E7.configure(highlightthickness="2")
	E7.configure(insertbackground="black")
	E7.configure(relief="flat")
	E7.configure(selectbackground="#c4c4c4")
	E7.configure(selectforeground="black")

	L12 = tk.Label(top)
	L12.place(relx=0.548, rely=0.457, height=21, width=54)
	L12.configure(activebackground="#f9f9f9")
	L12.configure(activeforeground="black")
	L12.configure(background="#2e5aa5")
	L12.configure(disabledforeground="#a3a3a3")
	L12.configure(font=font11)
	L12.configure(foreground="#ffffff")
	L12.configure(highlightbackground="#d9d9d9")
	L12.configure(highlightcolor="black")
	L12.configure(text='''DOB:''')
	L12.configure(width=54)

	
	date = [1,2,3,4,5,6,7,8,9,10,
			11,12,13,14,15,16,17,18,19,20,
			21,22,23,24,25,26,27,28,29,30,
			31,]

	TCombobox2 = ttk.Combobox(top)
	TCombobox2.place(relx=0.619, rely=0.457, relheight=0.04
	                , relwidth=0.051)
	TCombobox2.configure(width=30)
	TCombobox2.configure(values=date)
	TCombobox2.configure(takefocus="")

	month = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'nov', 'dec']


	TCombobox3 = ttk.Combobox(top)
	TCombobox3.place(relx=0.679, rely=0.457, relheight=0.04
	                , relwidth=0.063)
	TCombobox3.configure(width=30)
	TCombobox3.configure(values=month)
	TCombobox3.configure(takefocus="")

	year = ['1931','1932','1933','1934','1935','1936','1937','1938','1939','1940',
	        '1941','1942','1943','1944','1945','1946','1947','1948','1949','1950',
			'1951','1952','1953','1954','1955','1956','1957','1958','1959','1960',
			'1961','1962','1963','1964','1965','1966','1967','1968','1969','1970',
			'1971','1972','1973','1974','1975','1976','1977','1978','1979','1980',
			'1981','1982','1983','1984','1985','1986','1987','1988','1989','1990',
			'1991','1992','1993','1994','1995','1996','1997','1998','1999','2000', '2001', '2002']


	TCombobox4 = ttk.Combobox(top)
	TCombobox4.place(relx=0.75, rely=0.457, relheight=0.04
	                , relwidth=0.087)
	TCombobox4.configure(width=30)
	TCombobox4.configure(values=year)
	TCombobox4.configure(takefocus="")

	L8 = tk.Label(top)
	L8.place(relx=0.512, rely=0.514, height=31, width=84)
	L8.configure(activebackground="#f9f9f9")
	L8.configure(activeforeground="black")
	L8.configure(background="#2e5aa5")
	L8.configure(disabledforeground="#a3a3a3")
	L8.configure(font=font11)
	L8.configure(foreground="#ffffff")
	L8.configure(highlightbackground="#d9d9d9")
	L8.configure(highlightcolor="black")
	L8.configure(text='''Question:''')

	question = ['what is your age?',
	'what is your first pet?', 
	'what is your school name?',
	'what is your first friend name?',
	'what is your favourite place in the world?']

	TCombobox1 = ttk.Combobox(top)
	TCombobox1.place(relx=0.619, rely=0.514, relheight=0.063
	, relwidth=0.349)
	TCombobox1.configure(font=font11)
	TCombobox1.configure(values=question)
	TCombobox1.configure(width=330)
	TCombobox1.configure(background="#a1d6ff")
	TCombobox1.configure(takefocus="")

	L9 = tk.Label(top)
	L9.place(relx=0.524, rely=0.591, height=31, width=74)
	L9.configure(activebackground="#f9f9f9")
	L9.configure(activeforeground="black")
	L9.configure(background="#2e5aa5")
	L9.configure(disabledforeground="#a3a3a3")
	L9.configure(font=font11)
	L9.configure(foreground="#ffffff")
	L9.configure(highlightbackground="#d9d9d9")
	L9.configure(highlightcolor="black")
	L9.configure(text='''Answer:''')

	E8 = tk.Entry(top)
	E8.place(relx=0.619, rely=0.591,height=30, relwidth=0.35)
	E8.configure(background="#a1d6ff")
	E8.configure(disabledforeground="#a3a3a3")
	E8.configure(font="TkFixedFont")
	E8.configure(foreground="#000000")
	E8.configure(highlightbackground="#000000")
	E8.configure(highlightcolor="#000000")
	E8.configure(highlightthickness="2")
	E8.configure(insertbackground="black")
	E8.configure(relief="flat")
	E8.configure(selectbackground="#c4c4c4")
	E8.configure(selectforeground="black")

	L10 = tk.Label(top)
	L10.place(relx=0.524, rely=0.648, height=31, width=74)
	L10.configure(activebackground="#f9f9f9")
	L10.configure(activeforeground="black")
	L10.configure(background="#2e5aa5")
	L10.configure(disabledforeground="#a3a3a3")
	L10.configure(font=font11)
	L10.configure(foreground="#ffffff")
	L10.configure(highlightbackground="#d9d9d9")
	L10.configure(highlightcolor="black")
	L10.configure(text='''PAN No.:''')

	E9 = tk.Entry(top)
	E9.place(relx=0.619, rely=0.648,height=30, relwidth=0.35)
	E9.configure(background="#a1d6ff")
	E9.configure(disabledforeground="#a3a3a3")
	E9.configure(font="TkFixedFont")
	E9.configure(foreground="#000000")
	E9.configure(highlightbackground="#000000")
	E9.configure(highlightcolor="#000000")
	E9.configure(highlightthickness="2")
	E9.configure(insertbackground="black")
	E9.configure(relief="flat")
	E9.configure(selectbackground="#c4c4c4")
	E9.configure(selectforeground="black")

	L11 = tk.Label(top)
	L11.place(relx=0.518, rely=0.705, height=31, width=84)
	L11.configure(activebackground="#f9f9f9")
	L11.configure(activeforeground="black")
	L11.configure(background="#2e5aa5")
	L11.configure(disabledforeground="#a3a3a3")
	L11.configure(font=font11)
	L11.configure(foreground="#ffffff")
	L11.configure(highlightbackground="#d9d9d9")
	L11.configure(highlightcolor="black")
	L11.configure(text='''Mobile No.:''')

	E10 = tk.Entry(top)
	E10.place(relx=0.619, rely=0.705,height=30, relwidth=0.35)
	E10.configure(background="#a1d6ff")
	E10.configure(disabledforeground="#a3a3a3")
	E10.configure(font="TkFixedFont")
	E10.configure(foreground="#000000")
	E10.configure(highlightbackground="#000000")
	E10.configure(highlightcolor="#000000")
	E10.configure(highlightthickness="2")
	E10.configure(insertbackground="black")
	E10.configure(relief="flat")
	E10.configure(selectbackground="#c4c4c4")
	E10.configure(selectforeground="black")

	
	Button2 = tk.Button(top)
	Button2.place(relx=0.631, rely=0.765, height=20, width=277)
	Button2.configure(activebackground="#ececec")
	Button2.configure(activeforeground="#000000")
	Button2.configure(background="#a1d6ff")
	Button2.configure(disabledforeground="#a3a3a3")
	Button2.configure(font=font9)
	Button2.configure(foreground="#000000")
	Button2.configure(highlightbackground="#d9d9d9")
	Button2.configure(highlightcolor="black")
	Button2.configure(pady="0")
	Button2.configure(relief="flat")
	Button2.configure(text='''Signup''')




top.mainloop()