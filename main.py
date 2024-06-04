from pyscript import window, display, document, when
from pyscript.ffi import create_proxy
import time
import random
import asyncio

def operation_select():
    operation = document.getElementById("operation").value
    if operation == "addition":
        return " + "
    elif operation == "subtraction":
        return " - "
    elif operation == "multiplication":
        return " &#183 "
    else:
        return " / "

@when('click', "#reset")
def reset(event):
    document.getElementById("play").disabled = False
    document.getElementById("difficulty").disabled = False
    document.getElementById("operation").disabled = False
    document.getElementById("svar").value = ""
    document.getElementById("oppg").innerHTML = ""
    
def regnestykke(a, b, op): 
    if op == " + ":
        document.getElementById("oppg").innerHTML = str(a) + op + str(b) + " = "
    elif op == " - ":
        document.getElementById("oppg").innerHTML = str(max(a,b)) + op + str(min(a,b)) + " = "
    elif op == " &#183 ":
        document.getElementById("oppg").innerHTML = str(a) + " &#183 " + str(b) + " = "
    else:
        document.getElementById("oppg").innerHTML = str(a*b) + op + str(b) + " = "
    return document.getElementById("oppg").innerHTML


@when('click', "#play")
def start_spill(event):
    global operasjon
    operasjon = operation_select()
    global maks
    maks = int(document.getElementById("difficulty").value)
    global start_tid
    start_tid = time.time()
    
    document.getElementById("play").disabled = True
    document.getElementById("difficulty").disabled = True
    document.getElementById("operation").disabled = True
    document.getElementById("svar").disabled = False
    ny_oppgave(operasjon, maks)

@when('keydown', "#svar")
def submit_svar(event):
    if event.key == "Enter":
        document.getElementById("svarfelt").innerHTML = ""
        svar_tekst = document.getElementById("svar").value
        document.getElementById("svar").value = ""
        event.preventDefault()
        fasit_tekst = document.getElementById("oppg").innerHTML[:-3].replace("·", "*")
        if int(svar_tekst) == eval(fasit_tekst):
            ny_oppgave(operasjon, maks)
        else:
            display("Feil. Prøv igjen.", target="svarfelt")
        

    
def ny_oppgave(operasjon, maks):
    a = random.randint(1,maks)
    b = random.randint(1,maks)
    oppg = regnestykke(a, b, operasjon)
    document.getElementById('svar').focus()
