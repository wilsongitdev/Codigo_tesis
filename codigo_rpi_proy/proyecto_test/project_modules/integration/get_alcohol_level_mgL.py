
def get_alcohol_level_mgL_BAC(vprom, tara):

	# algoritmo 1
	if vprom < tara:
		Relr = 0
		alcohol = 0.000
		alcbac = 0.000
		promile = 0.000

	else:
		#vprom=vprom-tara
		Rs = 1000 * ((4.9-vprom)/vprom)
		Ro = 2517.3611
		Relr = Rs/Ro
		alcohol = 0.4091 * pow(Rs/Ro,-1.497)
		alcbac = ((alcohol * 0.29) / 1.38) - 0.0005
		promile = alcbac * 1000


	"""
	#algoritmo 2
	if (vprom<tara):
		Relr=0
		alcohol=0.000
		alcbac=0.000

	else:
		Relr=0
		vprom=vprom-tara
		alcohol=alcohol+(vprom/2)
		alcbac=alcohol/5

	"""
	"""
	#algoritmo 3 
	
	if (vprom<tara):
		Relr=0
		alcohol=0.000
		alcbac=0.000
		promile=0.000
		led_r.ChangeDutyCycle(0)
		led_g.ChangeDutyCycle(dt_col)
		led_b.ChangeDutyCycle(0)
	else:
		#vprom=vprom-tara
		Rs=1000*((4.9-vprom)/vprom)
		Ro=2517.3611
		Relr=Rs/Ro
		alcohol=alcohol+0.4091*pow(Rs/Ro,-1.497)+0.11
		if alcohol<0.34:
		   vprom1=vprom-tara
		   alcohol=(vprom1/2)+0.012
		alcbac=((alcohol*0.29)/1.38)-0.0005
		promile=alcbac*1000
		led_r.ChangeDutyCycle(dt_col)
		led_g.ChangeDutyCycle(0)
		led_b.ChangeDutyCycle(0)
	print("Alcohol dtmq3: "+str(alcohol))
	alcohol=0.000
	"""
	return alcohol, alcbac
