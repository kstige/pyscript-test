from js import document,alert

def farh(cel):
    return (float(cel) *(9/5)) + 32
        
    
def convert(*ags, **kws):
    
    celsius = document.getElementById('celsius').value
    result= farh(celsius)
    pyscript.write("Fahrenheit",result)  
