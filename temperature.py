from pyscript import document

def farh(cel):
    return (float(cel) *(9/5)) + 32
        
    
def convert(event):
    
    input_text = document.querySelector("#celsius")
    celsius = input_text.value
    result= farh(celsius)
    output_div = document.querySelector("#fahrenheit")
    output_div.innerText = result
