from pyscript import document

def gen_rec(event):
    text = document.querySelector("#box1").value
    answer = separator.join(text)

    document.querySelector("#output").innerText = (
        "Result: " + str(answer)
    )