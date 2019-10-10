s=['dodavannya','vidnimannya','mnogennya','dilennya','pidnesennya do stepenya','pidnesennya do kvadratu']
t=('''Vy vybraly {0}''')
t2=('''Rezultatom  {0} chysel {1} ta {2} bude chyslo {3} ''')
a=input('''Please enter the operation 
+  (dodavannya)
-  (vidnimannya)
*  (mnogennya)
/  (dilennya)
** (pidnesennya do stepenya)
^  (pidnesennya do kvadratu)  
 ''')
if a=='+':
	print(t.format(s[0]))
	b=float(input('''Vvedit pershe chyslo  '''))
	c=float(input('''Vvedit druge chyslo  '''))
	d=b+c
	print(t2.format(s[0],b,c,d))
elif a=='-':
	print(t.format(s[1]))
	b=float(input('''Vvedit pershe chyslo  '''))
	c=float(input('''Vvedit druge chyslo  '''))
	d=b-c
	print(t2.format(s[1],b,c,d))
elif a=='*':
	print(t.format(s[2]))
	b=float(input('''Vvedit pershe chyslo  '''))
	c=float(input('''Vvedit druge chyslo  '''))
	d=b*c
	print(t2.format(s[2],b,c,d))
elif a=='/':
	print(t.format(s[3]))
	b=float(input('''Vvedt pershe chyslo  '''))
	c=float(input('''Vvedit druge chyslo  '''))
	d=b/c
	print(t2.format(s[3],b,c,d))
elif a=='**':
	print(t.format(s[4]))
	b=float(input('''Vvedit pershe chyslo  '''))
	c=float(input('''Vvedit chyslo  stepenya '''))
	d=b**c
	print(t2.format(s[4],b,c,d))
elif a=='^':
	print(t.format(s[5]))
	b=float(input('''Vvedit chyslo  '''))
	if float(b)/int(b)==1:
		d=b*b
		print('Rezultatom pidnesennya chysla',int(b), 'do kvadratu bude chyslo',int(d))
	elif float(b)/float(b)>=1:
		print('''Vvedit chile chyslo''')         
else:
	print('Vvedit pravylne znachennya')